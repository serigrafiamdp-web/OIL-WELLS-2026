# OIL WELLS 2026 — Commodore 64

**Proyecto de investigación, modificación de controles, recuperación de gráficos y exportación de los ocho niveles de _Oil's Well_ a LVLLVL.**

> Proyecto independiente de preservación y experimentación sobre la edición C64 (1983, Sierra On-Line). No es un port completo, una reimplementación ni una edición oficial.

## ¿Qué se hizo?

Trabajamos sobre un PRG concreto de la edición **COPY SOFT** de Oil's Well. Recuperamos sus ocho mapas, el charset original y sus paletas. También preparamos variantes del juego con controles de teclado y un exportador que genera JSON compatibles con **LVLLVL**.

**Resultados verificados en las sesiones de trabajo:**

- **Controles — TEST03 PASS:** `W` retrae el brazo, `S` baja/avanza y `A`/`D` mueven lateralmente; ya no es necesario pulsar SPACE para retraer. Se preserva el control original por joystick.
- **Gráficos — TEST03 PASS:** ocho mapas originales exportados como **ocho frames** a LVLLVL, con la paleta y color RAM correspondientes a cada nivel.
- **Herramientas de recuperación:** mapas originales completos, vistas de 40×25, 128 caracteres de 8×8, archivos COLOR RAM y visualizadores PRG por nivel.
- **Pendiente:** validación exhaustiva de todos los PRG visualizadores en VICE, importación/regreso de LVLLVL al motor, y reconstrucción de las capas raster, sprites y elementos dinámicos.

El nombre `TEST03` se usó en **dos líneas de trabajo independientes**, por eso este README habla de _TEST03 controles_ y _TEST03 LVLLVL colores_. No confundirlos.

## Archivos del proyecto

```text
README.md
docs/
  MAPA_DE_MEMORIA.md
  TESTS_Y_ESTADO.md
  FORMATO_GRAFICOS_Y_LVLLVL.md
  REPRODUCIR_Y_VALIDAR.md
  SIGUIENTES_PASOS.md
  ANALISIS_CONTROL_TEST00.txt
prg/
  controles/
    OILS_WELL_TEST01_TECLADO_WASD_SPACE.prg
    OILS_WELL_TEST02_WASD_AUTO_RETRACCION.prg
    OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg
  visores-estaticos/
    OILS_WELL_NIVEL_01_ESTATICO.prg ... NIVEL_08
mapas/
  LEVEL_01_MAP_1024_ORIGINAL.bin ... LEVEL_08...
  LEVEL_01_MAP_40x25.bin ... LEVEL_08...
charset/
  TILESET_REAL_128_CHAR_9A00.bin
  TILESET_256_CHAR_PADDED.bin
colores/
  LEVEL_01_COLOR_RAM_40x25.bin ... LEVEL_08...
  PALLETAS_ORIGINALES.json
lvllvl/
  OILS_WELL_8_FRAMES_LVLLVL_TEST03_COLORES_POR_NIVEL.json
  niveles/LEVEL_01.json ... LEVEL_08.json
previews/
  VISTA_8_NIVELES.png
  VISTA_PALETAS_8_NIVELES.png
  niveles/LEVEL_01.png ... LEVEL_08.png
tools/
  exportador_historico_test01.py
  exportador_historico_web/index.html
  exportador_historico_web/app.js
manifest/
  archivos_sha256.json
```

**[DESCARGAR TODOS LOS ARCHIVOS DEL PROYECTO (ZIP)](archivos/OIL_WELLS_2026_REPOSITORIO_COMPLETO.zip)**

**Importante:** el ZIP de recuperación puede contener archivos que todavía no estén publicados individualmente en GitHub; consultar el estado de publicación y el manifiesto. El archivo original `oils well.prg` no es una versión modificada propia y no se incluye como «master redistribuible» en este proyecto.

## Cómo probar el juego con controles nuevos

1. Abrir **VICE x64sc** (modo PAL si es posible).
2. Cargar `prg/controles/OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg`.
3. Iniciar la carga como PRG C64. Con la carga habitual en BASIC, usar `RUN` si no arranca automáticamente.
4. Comprobar `W` para retraer, `S` para avanzar y `A`/`D` para mover lateralmente.
5. Verificar que el joystick original siga funcionando y que SPACE ya no sea necesario para retraer.

**No usar los `NIVEL_XX_ESTATICO.prg` para probar jugabilidad.** Son programas independientes que muestran mapas y charset, sin enemigos, colisiones, animación, sprites ni la lógica del juego.

## Cómo editar los ocho niveles en LVLLVL

1. Abrir LVLLVL (editor de gráficos de caracteres Commodore).
2. Importar `lvllvl/OILS_WELL_8_FRAMES_LVLLVL_TEST03_COLORES_POR_NIVEL.json`.
3. La línea de tiempo contiene **8 frames**, uno por nivel, todos de **40 columnas × 25 filas**.
4. Cada celda conserva el **índice original del carácter** del juego y su color. El tileset compartido conserva 128 caracteres originales; para compatibilidad se exportan 256 entradas y la mitad superior está vacía.
5. Modificar mapas o fuentes en el editor. **Todavía no hay un reintegrador probado** que vuelva a escribir esas modificaciones en el juego funcional.

### Lo que LVLLVL sí reproduce y lo que no

El juego original combina **bitmap hires**, **caracteres multicolor**, **split raster** y **sprites/datos dinámicos**. Un único layer convencional de LVLLVL no reproduce el fotograma completo del juego. El JSON TEST03 representa **la capa de mapas de caracteres con los colores extraídos**, no un clon exacto píxel a píxel de todo lo que dibuja VIC-II. No inferir colisiones ni lógica de enemigos solamente a partir del mapa.

## Datos técnicos indispensables para un coder

| Tema | Dirección / dato |
| --- | --- |
| PRG estudiado | carga `$0801`, arranque BASIC `SYS 2084` (`$0824`) |
| Cargador COPY SOFT | copia `$0900–$59FF` hacia `$8000–$D0FF` |
| Charset original en imagen reubicada | `$9A00–$9DFF`, **128 × 8 bytes** |
| Mapas | `$A000–$BFFF`, ocho bloques de **1.024 bytes** |
| Primer mapa | `$A000` |
| Mapa 8 | `$BC00` |
| Uso visible por nivel | primeros **1.000 bytes** de cada bloque: **40×25** |
| Modos VIC | bitmap hires y caracteres multicolor alternados por raster |
| CIA1 joystick puerto 1 | `$DC01`, entradas activas en bajo |
| Lector de joystick principal | `$85EE`, `$85FB`, `$8610` (y otras lecturas) |
| Tablas de paleta | `$963D`, `$965D`, `$967D`, cuatro bytes por nivel |

Dirección de un mapa de nivel `n` (1–8):

```text
mapa[n] = $A000 + (n - 1) * $0400
offset en PRG original = $2101 + (n - 1) * $0400
```

**Atención:** el `offset` anterior depende del PRG COPY SOFT que hemos analizado. No se debe aplicar automáticamente a otro crack, imagen de disco o versión.

La memoria de los gráficos es **solo una parte del motor**. No modificar bytes de colisión o tablas cercanas sin trazar las referencias de la rutina que los lee. Consultar [el mapa completo de memoria](docs/MAPA_DE_MEMORIA.md).

## Estado y procedencia

- **TEST03 controles:** PASS informado durante las pruebas, último PRG de jugabilidad documentado.
- **TEST03 LVLLVL colores:** PASS de exportación con ocho frames y colores por nivel.
- **8 visores estáticos:** comprobados por simulación de 6510; **no equivalen a PASS visual de VICE**.
- **Original COPY SOFT:** SHA-256 `26f5ff6d362f5018e74761d73c6e273ecc332d36e0b6992c65126683474520bd`.

Los hashes de los archivos recuperados figuran en `manifest/archivos_sha256.json`. Las transformaciones son propias; el juego base y sus gráficos pertenecen a sus titulares originales. No se reivindica titularidad de los recursos del juego.

## Guía para continuar

Para retomar el trabajo, empezar por **[TESTS_Y_ESTADO](docs/TESTS_Y_ESTADO.md)** y **[MAPA_DE_MEMORIA](docs/MAPA_DE_MEMORIA.md)**. Preservar los PRG que dieron PASS, crear **TEST04** para cualquier cambio de jugabilidad posterior y verificarlo en VICE antes de sustituir nada. Para gráficos, la referencia actual es **LVLLVL TEST03 colores por nivel**.