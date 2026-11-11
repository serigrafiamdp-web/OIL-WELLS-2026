#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprueba los recursos VIGENTES de OIL-WELLS-2026, sin modificar archivos.
Uso desde la raíz: python3 tools/verificar_recursos.py
El archivo manifest/archivos_sha256.json es histórico (incluye rutas retiradas).
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRG_HASHES = {
    "OILS_WELL_TEST01_TECLADO_WASD_SPACE.prg": "effbffa3146218d26615ee318da0b1ea667e102b5d52f05eaf3cfa4627f4bbd0",
    "OILS_WELL_TEST02_WASD_AUTO_RETRACCION.prg": "10fa3a4e16670516352fbef6c8b06aba3b483f3cb486ffcad1abc1d406ed7122",
    "OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg": "10d771c17498342a975d4fca2d706a6ed77a5c956b5d00db650a27d0aa568269",
}

def main():
    errores = []
    comprobados = 0

    def archivo(rel, tamano=None, checksum=None):
        nonlocal comprobados
        f = ROOT / rel
        if not f.is_file():
            errores.append(f"FALTA: {rel}")
            return None
        b = f.read_bytes()
        comprobados += 1
        if tamano is not None and len(b) != tamano:
            errores.append(f"TAMAÑO ERRÓNEO: {rel} ({len(b)} != {tamano})")
        if checksum and hashlib.sha256(b).hexdigest() != checksum:
            errores.append(f"SHA-256 ERRÓNEO: {rel}")
        return b

    for nombre, hash_esperado in PRG_HASHES.items():
        archivo("PRG/jugables/" + nombre, 38405, hash_esperado)

    prgs = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
                  if p.is_file() and p.suffix.lower() == ".prg")
    correctos = sorted("PRG/jugables/" + n for n in PRG_HASHES)
    if prgs != correctos:
        errores.append(f"PRG EN REPOSITORIO DISTINTOS DE LOS TRES JUGABLES: {prgs}")

    archivo("charset/TILESET_REAL_128_CHAR_9A00.bin", 1024)
    archivo("charset/TILESET_256_CHAR_PADDED.bin", 2048)

    for n in range(1, 9):
        prefix = f"LEVEL_{n:02d}"
        archivo(f"mapas/{prefix}_MAP_1024_ORIGINAL.bin", 1024)
        archivo(f"mapas/{prefix}_MAP_40x25.bin", 1000)
        archivo(f"colores/{prefix}_COLOR_RAM_40x25.bin", 1000)

        raw = archivo(f"LVLLVL/niveles/NIVEL_{n:02d}.json")
        if raw is not None:
            try:
                obj = json.loads(raw)
                frames = obj["tileMap"]["layers"][0]["frames"]
                assert len(frames) == 1, "no contiene un único frame"
            except (ValueError, KeyError, IndexError, TypeError, AssertionError) as err:
                errores.append(f"JSON INDIVIDUAL INVÁLIDO: nivel {n}: {err}")

    raw = archivo("LVLLVL/OILS_WELL_8_FRAMES_TEST03_COLORES_POR_NIVEL.json")
    if raw is not None:
        try:
            obj = json.loads(raw)
            assert len(obj["tileMap"]["layers"][0]["frames"]) == 8
            assert len(obj["tileSet"]["tiles"]) == 256
            assert obj["tileMap"]["layers"][0]["gridWidth"] == 40
            assert obj["tileMap"]["layers"][0]["gridHeight"] == 25
        except (ValueError, KeyError, IndexError, TypeError, AssertionError) as err:
            errores.append(f"PROYECTO LVLLVL PRINCIPAL INVÁLIDO: {err}")

    archivo("colores/PALLETAS_ORIGINALES.json")
    print(f"Recursos vigentes comprobados: {comprobados}")
    if errores:
        for error in errores:
            print("ERROR:", error)
        return 1
    print("PASS — tres PRG jugables (hash exacto), ocho mapas, charset, colores y estructura LVLLVL.")
    print("NOTA — este verificador no prueba jugabilidad real: eso requiere VICE.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
