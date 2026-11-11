# Historial de pruebas y estado de aceptación

**Convención**: un **PASS confirmado** viene de la sesión de prueba del juego/editor; una verificación estructural o una simulación de código 6502 **no implica PASS visual/funcional en VICE**.

## A. Modificaciones de jugabilidad

| Test | Archivo | Cambio | Estado |
| --- | --- | --- | --- |
| TEST00 | `docs/ANALISIS_CONTROL_TEST00.txt` | Localización de accesos a `$DC01` y rutas de control, sin cambiar PRG | Análisis estático |
| TEST01 | `prg/controles/OILS_WELL_TEST01_TECLADO_WASD_SPACE.prg` | Primer control por teclado W/A/S/D y SPACE en experimento | Versión histórica, no master |
| TEST02 | `prg/controles/OILS_WELL_TEST02_WASD_AUTO_RETRACCION.prg` | Experimento con retracción automática / ajustes de control | Versión histórica, no master |
| **TEST03** | **`prg/controles/OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg`** | **W sustituye FIRE para retraer; S avanza/baja; A/D lateral; SPACE desactivado; joystick conservado** | **PASS funcional informado** |

Los nombres de archivo TEST01 y TEST02 describen fases de desarrollo; para retomar la jugabilidad elegir TEST03, sin suponer que los anteriores son más completos.

**Verificación binaria**: los tres PRG tienen el mismo tamaño (38.405 bytes, encabezado LOAD `$0801`). Respecto del PRG fuente se cambian unas lecturas concretas de `$DC01` y una zona de rutinas. TEST03 difiere de TEST01 solo en dos bytes dentro de esa zona; consultar el mapa de memoria antes de parchar.

**No confirmado**: compatibilidad completa con cada joystick físico, todas las situaciones de menú/pausa y todos los niveles jugados de principio a fin.

## B. Recuperación de niveles / editor gráfico

| Test | Entregable | Estado |
| --- | --- | --- |
| Extracción TEST00 | Candidatos de charset y bloques binarios 1.024 bytes | Recuperado |
| Mapas TEST01 | 8 niveles de 1.024 B + vistas 40×25 y charset | Estructuralmente verificado |
| Visores estáticos TEST01 | 8 PRG de 2.198 B con una pantalla fija | Simulación 6510 PASS; ejecución real VICE no documentada |
| LVLLVL TEST01 | 8 niveles, índices de char originales y colores provisionales | Exportador histórico; no es el master de colores |
| LVLLVL TEST02 | 8 frames en modo multicolor, ajustes sobre TEST01 | Paso intermedio |
| **LVLLVL TEST03** | **JSON de 8 frames, Color RAM y colores D020–D023 por nivel** | **PASS de recuperación y exportación** |

El **JSON TEST03** es la referencia más completa para trabajar los niveles en LVLLVL, pero no contiene el raster completo, los sprites, los enemigos ni colisiones dinámicas.

## Últimos PASS recuperados

1. **Juego / controles:** `OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg`.
2. **Editor / gráficos:** `OILS_WELL_8_FRAMES_LVLLVL_TEST03_COLORES_POR_NIVEL.json`.
3. **Extracción:** ocho `LEVEL_XX_MAP_1024_ORIGINAL.bin`, ocho `LEVEL_XX_MAP_40x25.bin`, Color RAM por nivel y charset real.

**No hemos confirmado un TEST04 jugable posterior** sobre Oil's Well; no adjudicar PASS a tests de otro proyecto, como LVLLVL/scroll o EPYX.

## Prueba de regresión sugerida

- Cargar TEST03 en VICE (preferentemente `x64sc` PAL).
- En menú y en juego verificar que se acepten comandos sin atascar el escaneo de teclado.
- Durante juego: W = retracción, S = descenso, A y D = movimiento lateral; SPACE no se utiliza para retraer.
- Probar joystick 1 original y verificar que los enemigos y cambios de nivel se mantengan.
- Comparar sha256 del PRG antes y después de editarlo.
- Para gráficos: importar JSON TEST03 a LVLLVL; recorrer frames 1–8 y comprobar mapa, tileset y color original por nivel.
- Para los ocho visores PRG, tomar captura real antes de registrar PASS de VICE.

## Identificación del original

- `oils well.prg` aportado para el análisis: 38.405 B, SHA-256 `26f5ff6d362f5018e74761d73c6e273ecc332d36e0b6992c65126683474520bd`.
- El repositorio documenta modificaciones y derivados; no adjudicar autoría del juego base al proyecto.
