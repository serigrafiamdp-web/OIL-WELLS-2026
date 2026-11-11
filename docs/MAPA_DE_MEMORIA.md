# Mapa de memoria — Oil's Well C64 (variante COPY SOFT)

**Ámbito:** únicamente `oils well.prg` proporcionado para el análisis, SHA-256 `26f5ff6d362f5018e74761d73c6e273ecc332d36e0b6992c65126683474520bd`. Las direcciones se refieren **a la imagen ejecutándose tras la reubicación**, salvo que se indique otra cosa.

## 1. Cargador

- PRG con cabecera `$0801`, línea BASIC `10 SYS(2084)`, entrada `$0824`.
- El cargador copia `$0900–$59FF` a `$8000–$D0FF`.
- El código reubicado contiene la firma CBM80 a partir de `$8004` y entrada desde `$8009`.
- Los bytes de la ROM/imagen reubicada no coinciden directamente con las direcciones de carga del PRG.

**Fórmula de offset para cualquier dirección reubicada `$8000–$D0FF`:**

```text
desplazamiento dentro del PRG = (direccion_reubicada - $8000) + $0101
```

La suma `$0101` corresponde a dos bytes de cabecera PRG y al punto `$0900` dentro de la carga original desde `$0801`.

## 2. Mapas de los niveles

| Nivel | Dirección en la imagen reubicada | Offset de archivo PRG original | Archivo recuperado |
| ---: | ---: | ---: | --- |
| 1 | `$A000–$A3FF` | `$2101` | `LEVEL_01_MAP_1024_ORIGINAL.bin` |
| 2 | `$A400–$A7FF` | `$2501` | `LEVEL_02_MAP_1024_ORIGINAL.bin` |
| 3 | `$A800–$ABFF` | `$2901` | `LEVEL_03_MAP_1024_ORIGINAL.bin` |
| 4 | `$AC00–$AFFF` | `$2D01` | `LEVEL_04_MAP_1024_ORIGINAL.bin` |
| 5 | `$B000–$B3FF` | `$3101` | `LEVEL_05_MAP_1024_ORIGINAL.bin` |
| 6 | `$B400–$B7FF` | `$3501` | `LEVEL_06_MAP_1024_ORIGINAL.bin` |
| 7 | `$B800–$BBFF` | `$3901` | `LEVEL_07_MAP_1024_ORIGINAL.bin` |
| 8 | `$BC00–$BFFF` | `$3D01` | `LEVEL_08_MAP_1024_ORIGINAL.bin` |

Cada bloque contiene **1.024 bytes**; el mapa visible de **40×25 = 1.000 bytes** ocupa los primeros 1.000. Preservamos los 24 bytes restantes del bloque original y **no asumimos** que puedan descartarse al reinsertarlo en el motor.

- `$22`: índice interno del nivel (0–7), observado en el análisis posterior.
- `$23`: índice escalado ×4, usado por la lógica de niveles.
- `$8E80`: rutina relacionada con la preparación del mapa.
- `$8B62`: rutina de avance de nivel.

Los offsets y esas rutinas pertenecen a esta variante del PRG; confirmar mediante desensamblado si se trabaja sobre otro crack.

## 3. Charset y VIC-II

| Dirección / registro | Significado |
| --- | --- |
| `$9A00–$9DFF` | Charset real: 128 × 8 bytes = 1.024 bytes |
| `$7000` | Destino del charset en el visualizador estático |
| `$6000` | Mapa de pantalla del visualizador estático |
| `$D018=$8C` | Configuración del visualizador estático |
| `$D011=$3B`, `$D016=$08` | Fase de bitmap hires documentada para el original |
| `$D011=$1B`, `$D016=$18` | Fase de caracteres multicolor del original |

El original utiliza un split raster entre modos gráficos. El JSON de LVLLVL solo conserva la **capa de caracteres**.

## 4. Colores originales (TEST03 LVLLVL)

| Dirección | Interpretación extraída |
| --- | --- |
| `$963D + nivel * 4` | Registros D020–D023 por nivel, usados por manejador raster |
| `$965D + nivel * 4` | Colores de sprites y bandas de Color RAM |
| `$967D + nivel * 4` | Excepciones decorativas de color |
| `$828B–$82BD` | Actualización de registros de color durante el raster |
| `$8EB7–$8F34` | Rutina para Color RAM de los bloques de pantalla |

`nivel` en estas fórmulas está entre 0 y 7. Según el análisis, la banda superior abarca **7 filas (280 celdas)** y la inferior **18 filas (720 celdas)**. Los 1.000 valores de cada nivel están guardados en `colores/LEVEL_XX_COLOR_RAM_40x25.bin` y los registros de paleta en `colores/PALLETAS_ORIGINALES.json`.

Los colores corresponden a datos recuperados del ensamblador; un frame LVLLVL no reproduce necesariamente el fotograma exacto de VICE.

## 5. Control / joystick y teclado

La CIA #1 / puerto joystick 1 se consulta mediante `$DC01`, activo en bajo. **No sustituir indiscriminadamente todas esas lecturas**: algunas forman parte del escaneo de teclado en otras zonas del programa.

| Dirección de ejecución | Offset PRG | Uso inferido |
| --- | --- | --- |
| `$81E7` | `$02E8` | Lector joystick/teclado en bucle |
| `$81FF` | `$0300` | Lector joystick posterior al escaneo |
| `$85EE` | `$06EF` | Bit `$10`: FIRE, retracción del brazo |
| `$85FB` | `$06FC` | Bits `$03`: eje vertical |
| `$8610` | `$0711` | Bits `$0C`: eje horizontal |
| `$8708` | `$0809` | Selección/transición |
| `$959C` | `$169D` | FIRE con debounce |
| `$C59C` | `$469D` | Lógica de FIRE adicional |
| `$C0E3`, `$C0FD` | `$41E4`, `$41FE` | Escaneo de teclado de texto, no sustituir |

En los PRG modificados se interceptaron llamadas concretas con `JSR` a código añadido, conservando la semántica de joystick. **No interpretar este listado como un mapa completo de todos los accesos a CIA.**

La zona previa al código reubicado contiene NOP y permitió insertar la rutina de TEST01–03; validar que no sea sobrescrita en variantes nuevas.

## 6. Buenas prácticas para seguir modificando

1. Conservar la fuente original y sus hashes.
2. Trabajar sobre el último PRG confirmado PASS (`TEST03_W_FIRE_SAD_MOVIMIENTO`).
3. Dejar intactos los ocho bloques de mapas y su charset salvo si la prueba trata específicamente de gráficos.
4. Inspeccionar el programa en VICE monitor antes de reubicar rutinas o cambiar control de IRQ.
5. No confundir la salida estática de una pantalla con la lógica jugable, enemigos o colisiones.
