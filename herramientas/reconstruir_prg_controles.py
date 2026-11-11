#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconstruye los PRG TEST01/02/03 a partir del PRG COPY SOFT verificado.

Uso:
    python herramientas/reconstruir_prg_controles.py "oils well.prg" --salida PRG/pruebas

No modifica el juego original. Comprueba SHA-256 de entrada y de cada salida.
"""
from pathlib import Path
import argparse
from hashlib import sha256

ORIGINAL_SHA256 = "26f5ff6d362f5018e74761d73c6e273ecc332d36e0b6992c65126683474520bd"
SHA_TEST = {
 "TEST01": "effbffa3146218d26615ee318da0b1ea667e102b5d52f05eaf3cfa4627f4bbd0",
 "TEST02": "10fa3a4e16670516352fbef6c8b06aba3b483f3cb486ffcad1abc1d406ed7122",
 "TEST03": "10d771c17498342a975d4fca2d706a6ed77a5c956b5d00db650a27d0aa568269",
}
NOMBRES = {
 "TEST01": "OILS_WELL_TEST01_TECLADO_WASD_SPACE.prg",
 "TEST02": "OILS_WELL_TEST02_WASD_AUTO_RETRACCION.prg",
 "TEST03": "OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg",
}
PATCH_REGION = {
 "TEST01": (
  "0878ad00dc8dfa08ad02dc8dfb08ad03dc8dfc08a9ff8d00dc8d02dca9008d03dc"
  "ad01dc8dfd088dfe08a9fd8d00dcad01dc4dfd088dff08adff082902f008adfe"
  "0829fe8dfe08adff082920f008adfe0829fd8dfe08adff082904f008adfe0829fb"
  "8dfe08a9fb8d00dcad01dc4dfd082904f008adfe0829f78dfe08a97f8d00dc"
  "ad01dc4dfd082910f008adfe0829ef8dfe08adfa088d00dcadfb088d02dcadfc"
  "088d03dcadfe082809006048204708aa6860000000000000"
 ),
 "TEST02": (
  "0878ad00dc8dfa08ad02dc8dfb08ad03dc8dfc08a9ff8d00dc8d02dca9008d03dc"
  "ad01dc8dfd088dfe08a9fd8d00dcad01dc4dfd088dff08adff082902f008adfe"
  "0829fe8dfe08adff082920f008adfe0829fd8dfe08adff082904f008adfe0829fb"
  "8dfe08a9fb8d00dcad01dc4dfd082904f008adfe0829f78dfe08a97f8d00dc"
  "ad01dc4dfd082910f008adfe0829ef8dfe08adfa088d00dcadfb088d02dcadfc"
  "088d03dcadfe082809006048204708aa6860000000000000"
 ),
 "TEST03": (
  "0878ad00dc8dfa08ad02dc8dfb08ad03dc8dfc08a9ff8d00dc8d02dca9008d03dc"
  "ad01dc8dfd088dfe08a9fd8d00dcad01dc4dfd088dff08adff082902f008adfe"
  "0829ef8dfe08adff082920f008adfe0829fd8dfe08adff082904f008adfe0829fb"
  "8dfe08a9fb8d00dcad01dc4dfd082904f008adfe0829f78dfe08a97f8d00dc"
  "ad01dc4dfd082910f008adfe0829ff8dfe08adfa088d00dcadfb088d02dcadfc"
  "088d03dcadfe082809006048204708aa6860000000000000"
 ),
}
COMMON = {
 0x2E8: "20f308", 0x300: "20f308",
 0x6FC: "204708", 0x711: "204708",
 0x809: "204708", 0x169D: "204708", 0x469D: "204708",
}
AUTO_EXTRA = {
 0x10C3: "2047089848a0",
 0x10CA: "b110c95c9016c96cb012a429adfe0839eb8fd008adfe0829ef8dfe0868a8adfe086008040102",
}

def parchear(datos, offset, codigo_hex):
    bloque = bytes.fromhex(codigo_hex)
    assert 0 <= offset <= len(datos) - len(bloque)
    datos[offset:offset + len(bloque)] = bloque

def generar(original, test):
    datos = bytearray(original)
    parchear(datos, 72, PATCH_REGION[test])
    for offset, codigo in COMMON.items():
        parchear(datos, offset, codigo)
    parchear(datos, 0x6EF, "20c28f" if test == "TEST02" else "204708")
    if test == "TEST02":
        for offset, codigo in AUTO_EXTRA.items():
            parchear(datos, offset, codigo)
    return bytes(datos)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("--salida", type=Path, default=Path("PRG/pruebas"))
    args = parser.parse_args()
    original = args.original.read_bytes()
    real = sha256(original).hexdigest()
    if real != ORIGINAL_SHA256:
        raise SystemExit(f"PRG incompatible: SHA-256={real}; esperado={ORIGINAL_SHA256}")
    productos = []
    for test, nombre in NOMBRES.items():
        resultado = generar(original, test)
        real = sha256(resultado).hexdigest()
        if real != SHA_TEST[test]:
            raise RuntimeError(f"Checksum falló para {test}: {real}")
        productos.append((nombre, resultado))
    args.salida.mkdir(parents=True, exist_ok=True)
    for nombre, data in productos:
        ruta = args.salida / nombre
        ruta.write_bytes(data)
        print(f"OK: {ruta}, SHA-256={sha256(data).hexdigest()}")

if __name__ == "__main__":
    main()
