# Gráficos: mapas, tileset y exportación LVLLVL

## Archivos recuperados

| Recurso | Ubicación | Tamaño por archivo |
| --- | --- | ---: |
| Mapa original completo | `mapas/LEVEL_XX_MAP_1024_ORIGINAL.bin` | 1.024 B |
| Mapa visible C64 | `mapas/LEVEL_XX_MAP_40x25.bin` | 1.000 B |
| Charset real | `charset/TILESET_REAL_128_CHAR_9A00.bin` | 1.024 B |
| Charset ampliado | `charset/TILESET_256_CHAR_PADDED.bin` | 2.048 B |
| Color RAM por nivel | `colores/LEVEL_XX_COLOR_RAM_40x25.bin` | 1.000 B |
| Paletas originales | `colores/PALLETAS_ORIGINALES.json` | Ocho entradas |
| Proyecto de ocho frames | `lvllvl/OILS_WELL_8_FRAMES_LVLLVL_TEST03_COLORES_POR_NIVEL.json` | 8 frames |
| Nivel individual | `lvllvl/niveles/LEVEL_XX.json` | 1 frame |
| Visor de nivel | `prg/visores-estaticos/OILS_WELL_NIVEL_XX_ESTATICO.prg` | 2.198 B |

`XX` va del `01` al `08`.

### Mapa

Cada nivel ocupa un bloque de `$400` bytes. Los primeros 1.000 bytes codifican las celdas de 40 columnas × 25 filas, en orden de filas:

```python
indice = mapa[y * 40 + x]  # 0 <= x < 40, 0 <= y < 25
```

**No descartar los 24 bytes finales** del bloque de origen si se planea reinserción.

### Charset

128 caracteres, 8 bytes por carácter, un byte por fila. El carácter `n` empieza en `charset[n * 8]`. Para LVLLVL se amplió a 256 índices: 0–127 son originales, 128–255 se rellenaron con ceros. No se reordenan los índices de los mapas.

### Colores

La versión TEST01 usaba colores provisionales blancos. TEST03 extrae datos específicos de las tablas del programa, separando Color RAM de las 7 filas superiores y las 18 inferiores y considerando excepciones decorativas.

La configuración global D020, D021, D022 y D023 cambia por nivel. La información exacta está en `colores/PALLETAS_ORIGINALES.json`.

### JSON

El JSON combinado tiene las propiedades raíz `version`, `tileSet`, `colorPalette`, `tileMap` y metadatos `ricoInfo`. `tileMap.layers[0].frames` contiene **8 entradas**. Cada una tiene `data` de 25×40 celdas con índice de tile `t`, color de frente `fc` y atributos de frame (borde, fondo y multicolores).

**Limitación del editor:** el juego utiliza varias técnicas VIC-II simultáneas o alternadas por raster. El JSON representa la capa de caracteres y sus colores, sin emular el split ni los sprites/datos dinámicos. **No** se debe utilizar la vista exportada como imagen exacta de la partida en VICE.

## Cómo continuar

1. Abrir/importar el JSON combinado TEST03 en LVLLVL.
2. Cambiar a frames 1–8, inspeccionar los colores y editar el tileset/mapa.
3. Exportar y guardar el JSON resultante como nueva versión, sin reemplazar el TEST03.
4. Antes de reinsertar en el juego, diseñar un serializador que conserve índices, 1.024 bytes por bloque y referencias funcionales a mapas/celdas; aún no existe un reintegrador validado.

## Herramientas históricas

`tools/exportador_historico_test01.py` y la interfaz web adyacente reconstruyen la **fase TEST01** a partir del PRG COPY SOFT. Para conservar los colores reales de TEST03, usar el JSON y los Color RAM ya recuperados. **No afirmar** que el exportador histórico TEST01 genera TEST03 automáticamente.
