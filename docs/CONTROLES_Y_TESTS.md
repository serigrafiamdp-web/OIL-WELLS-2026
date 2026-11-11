# Controles — historial de pruebas

## Base

`oils well.prg` (COPY SOFT, 38.405 bytes) es el punto de partida de los prototipos. Los tres PRG de controles son de **igual longitud**: 38.405 bytes. Los parches se pueden reproducir mediante `herramientas/reconstruir_prg_controles.py`. Los binarios modificados están disponibles directamente en [`PRG/jugables/`](../PRG/jugables/).

| Prueba | Archivo / objetivo | SHA-256 de salida | Estado documentado |
| --- | --- | --- | --- |
| TEST00 | Análisis estático, control desde CIA1 / joystick 1; sin modificar PRG | — | Análisis realizado |
| TEST01 | `OILS_WELL_TEST01_TECLADO_WASD_SPACE.prg` · entrada WASD y SPACE | `effbffa3146218d26615ee318da0b1ea667e102b5d52f05eaf3cfa4627f4bbd0` | PRG generado; comportamiento exacto en VICE a reconfirmar |
| TEST02 | `OILS_WELL_TEST02_WASD_AUTO_RETRACCION.prg` · retracción automática | `10fa3a4e16670516352fbef6c8b06aba3b483f3cb486ffcad1abc1d406ed7122` | PRG generado; comportamiento exacto en VICE a reconfirmar |
| TEST03 | `OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg` · W/FIRE y movimiento con S/A/D | `10d771c17498342a975d4fca2d706a6ed77a5c956b5d00db650a27d0aa568269` | PRG generado; comportamiento exacto en VICE a reconfirmar |

No debe confundirse **TEST03 de controles** con **TEST03 de colores de LVLLVL**: son dos líneas de pruebas diferentes.

## Técnica de los parches

Se aprovecha una región inicialmente rellenada con NOP cerca de `$0847–$08FF` para instalar código auxiliar. Algunas lecturas seleccionadas de joystick se interceptan mediante instrucciones JSR de 3 bytes, conservando la longitud del PRG.

La variante TEST02 añade modificaciones en una segunda región del programa. Todos los cambios exactos quedan especificados y verificados por SHA en el reconstructor.

## Recomendación de regresión en VICE

Verificar separadamente:
1. Inicio y presentación del juego.
2. Desplazamiento horizontal y vertical con las teclas previstas.
3. Acción FIRE/SPACE de acuerdo con cada versión.
4. Retracción automática del brazo en TEST02.
5. Funcionamiento del joystick original y otras teclas del menú.
6. Comportamiento tras morir, pasar de nivel y reiniciar.
7. PAL/NTSC y presencia de bloqueos o corrupción.

No declarar ningún TEST como PASS global del juego sin haber revisado las regresiones importantes.
