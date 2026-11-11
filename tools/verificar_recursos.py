#!/usr/bin/env python3
"""Verifica integridad de los recursos recuperados mediante SHA-256 (sin modificar archivos)."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest/archivos_sha256.json"

def main():
    entries = json.loads(MANIFEST.read_text(encoding="utf-8"))
    problems=[]
    for rel,meta in sorted(entries.items()):
        f=ROOT/rel
        if not f.is_file():
            problems.append(f"FALTA {rel}")
            continue
        data=f.read_bytes()
        if len(data)!=meta["bytes"] or hashlib.sha256(data).hexdigest()!=meta["sha256"]:
            problems.append(f"ERROR {rel}")
    print(f"Recursos verificados: {len(entries)-len(problems)}/{len(entries)}")
    for problem in problems: print(problem)
    return bool(problems)

if __name__=="__main__":
    sys.exit(main())
