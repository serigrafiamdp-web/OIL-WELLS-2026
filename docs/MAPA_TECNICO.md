# Mapa técnico — memoria, datos y controles

## PRG fuente utilizado en el análisis

`oils well.prg` COPY SOFT, **38.405 bytes**, carga C64 `$0801`, fin `$9E04`. SHA-256:

`26f5ff6d362f5018e74761d73c6e273ecc332d36e0b6992c65126683474520bd`

Entrada BASIC en línea 10: `SYS 2084` (`$0824`). El cargador copia `$0900–$59FF` a `$8000–$D0FF` y salta indirectamente a reset mediante `JMP ($FFFC)`. Esta secuencia es específica de la copia analizada.

## Tablas de gráficos

| Elemento | Dirección C64 tras reubicación | Tamaño | Significado |
| --- | --- | --- | --- |
| Tileset | `$9A00–$9DFF` | 1024 bytes | 128 glifos 8×8; se rellenan hasta 256 para LVLLVL |
| Nivel 1 | `$A000` | 1024 bytes | Primeras 1000 posiciones = 40×25 |
| Nivel 2 | `$A400` | 1024 bytes | Mapa |
| Nivel 3 | `$A800` | 1024 bytes | Mapa |
| Nivel 4 | `$AC00` | 1024 bytes | Mapa |
| Nivel 5 | `$B000` | 1024 bytes | Mapa |
| Nivel 6 | `$B400` | 1024 bytes | Mapa |
| Nivel 7 | `$B800` | 1024 bytes | Mapa |
| Nivel 8 | `$BC00` | 1024 bytes | Mapa |

En el PRG COPY SOFT, el primer bloque de mapa empieza en **offset de archivo $2101**, los demás siguen a intervalos de $400 bytes. Los últimos 24 bytes de cada bloque **no deben descartarse** si se pretende reconstruir el PRG exacto.

## Colores por nivel (TEST03)

Extraídos de tablas y rutinas de la versión estudiada:
- `$963D + 4*nivel`: configuración `D020/D021/D022/D023` (borde, fondo, multicolor 1 y 2).
- `$965D + 4*nivel`: multicolores de sprites y bandas de Color RAM.
- `$967D + 4*nivel`: excepciones decorativas estáticas.

La salida LVLLVL reproduce el estado cromático determinista por nivel, **no** el efecto visual completo de raster/movimiento. La fuente alterna **bitmap HIRES** y **caracteres multicolor** en distintas zonas del cuadro.

## Controles CIA1, joystick puerto 1

Las lecturas de `$DC01` son activas en bajo. Bits 0/1: arriba/abajo; 2/3: izquierda/derecha; 4: FIRE. El punto central de manejo está cerca de `$85EE`, y parte de la lógica llama a `$8BF4`.

Offsets del PRG reubicado estudiados:
`$02E8`, `$0300`, `$06EF`, `$06FC`, `$0711`, `$0809`, `$169D`, `$469D`.

**Precaución:** otras lecturas de `$DC01` sirven para la matriz de teclado (por ejemplo cerca de `$C0E3/$C0FD`). No parchearlas sin distinguir su finalidad.
