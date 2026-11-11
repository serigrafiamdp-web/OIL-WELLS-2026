# Guía para quien retome el desarrollo

## Punto de partida

**Juego:** Oil's Well, Commodore 64. **Trabajo:** modificación experimental de controles y extracción de los ocho mapas editables a LVLLVL. El código de juego no fue reescrito ni portado; se estudiaron regiones 6510 concretas y se generaron pruebas.

Las tres variantes TEST de juego están publicadas en `PRG/jugables/` y verificadas por SHA-256. Los ocho antiguos visores estáticos PRG ya no se conservan en el árbol actual; los mapas y niveles LVLLVL sí.

## Reproducción rápida

### A. Trabajar con los mapas
1. Importar `LVLLVL/OILS_WELL_8_FRAMES_TEST03_COLORES_POR_NIVEL.json` en LVLLVL.
2. Abrir un frame por nivel. La escena tiene 40×25 caracteres (320×200 píxeles en grilla 8×8).
3. El tileset presenta 256 entradas: las primeras 128 pertenecen al juego y el resto son relleno para compatibilidad.
4. Si se desea un único nivel, importar el correspondiente `LVLLVL/niveles/NIVEL_XX.json`.
5. Preservar índices y dimensiones si se pretende después reinyectar datos al juego.

### B. Probar mapas en VICE
Los antiguos visores estáticos fueron retirados; para inspeccionar mapas se deben usar los JSON en `LVLLVL/` y las imágenes en `previews/`.

### C. Regenerar controles
Los tres PRG modificados están listos en `PRG/jugables/`. Si necesitás reconstruirlos desde el PRG original, partir de una copia propia del PRG COPY SOFT que tenga el SHA-256 esperado. Ejecutar:

```bash
python herramientas/reconstruir_prg_controles.py "oils well.prg" --salida "PRG/pruebas"
```

El script verifica SHA de origen y SHA de cada salida. No modifica el original. La existencia de un PRG generado **no equivale a PASS de VICE**.

## Cómo registrar nuevos tests

Cada cambio debe tener TEST incremental y un registro con: nombre del PRG, SHA-256, archivo de partida, offsets y bytes cambiados, qué comportamiento se espera, qué ocurrió realmente en VICE (PAL/NTSC, joystick, teclado), capturas y estado **PASS / FAIL / PENDIENTE**.

Si se produce un fallo, conservar el último TEST confirmado; no sustituirlo. No interceptar globalmente `$DC01`: esa dirección también interviene en el escaneo del teclado.

## Integración con LVLLVL

El proyecto `OIL-WELLS-2026` conserva **datos editables del nivel**, no un nuevo motor completo. Para un roundtrip juego↔LVLLVL, falta diseñar un exportador que transforme frames editados a 8 bloques de 1024 bytes conservando campos fuera de las 1000 celdas visibles y tablas de color; todavía no está implementado.
