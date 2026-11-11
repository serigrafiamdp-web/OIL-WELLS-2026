# Formato LVLLVL y limitaciones visuales

## JSON

El proyecto principal representa ocho niveles con estas propiedades:
- `version: 1`; claves `tileSet`, `colorPalette`, `tileMap`.
- `tileMap.frames`: **8**.
- Una capa de `40×25` celdas por frame.
- `tileSet.tiles`: **256** entradas de 8×8; solo las primeras 128 proceden del juego; las demás son relleno.
- `screenMode: c64multicolor`; Color RAM y valores de paleta distintos según nivel.
- Índices de caracteres del mapa preservados: no se reorganizaron ni se sustituyeron.

Los ocho archivos `LVLLVL/niveles/NIVEL_XX.json` contienen el mismo nivel individual para editar y exportar por separado.

## Fidelidad y límites

El juego original utiliza división por raster entre **bitmap HIRES** y **caracteres multicolor**. Un único layer de caracteres en LVLLVL no reproduce completamente:
- La parte bitmap HIRES del fondo.
- Sprites y animación de enemigos.
- Colores cambiados por lógica o raster durante la partida.
- Colisiones, comportamiento de los niveles, sonido y elementos dinámicos.

Por eso **TEST03 colores** significa una extracción más fiel de las **tablas de colores estáticos**, no una copia píxel por píxel de la pantalla de juego.

## Datos originales y visores históricos

Los ocho PRG que mostraban solo mapas estáticos fueron retirados del repositorio actual. Se conservaron los ocho mapas originales de 1.024 bytes en `mapas/`, sus vistas 40×25 y los niveles editables de LVLLVL. Los únicos PRG publicados son los tres jugables de `PRG/jugables/`.

**Los últimos 24 bytes de cada mapa de 1024 B** permanecen en los archivos `mapas/LEVEL_XX_MAP_1024_ORIGINAL.bin`; no corresponden a las 1000 celdas visibles y deben preservarse si se hace roundtrip.

## Validaciones conocidas

- Todos los JSON individuales tienen 1 frame de 40×25 y tileset 8×8.
- El JSON combinado tiene 8 frames.
- Los ocho antiguos visores son un hito histórico retirado, no un recurso disponible en la rama actual.
- TEST03 controles tiene PASS funcional informado en las sesiones originales; queda pendiente una nueva regresión completa en VICE.
