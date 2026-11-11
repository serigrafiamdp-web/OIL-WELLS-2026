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

## PRG visualizadores

Los ocho `PRG/visores_estaticos/*` son pequeños ejecutables propios (2.198 bytes cada uno) que muestran mapas estáticos. Se pueden montar en VICE. No incorporan el motor del juego, la lógica de puntuación ni todas las características raster del original.

**Los últimos 24 bytes de cada mapa de 1024 B** se conservaron en los PRG; no corresponden a las 1000 celdas visibles y deben preservarse si se hace roundtrip.

## Validaciones conocidas

- Todos los JSON individuales tienen 1 frame de 40×25 y tileset 8×8.
- El JSON combinado tiene 8 frames.
- Los PRG visores se reconstruyeron y verificaron byte a byte contra el archivo histórico `OILS_WELL_8_PRG_ESTATICOS_TEST01.zip`.
- No hay registro de PASS visual final en una ejecución nueva de VICE para todos los artefactos.
