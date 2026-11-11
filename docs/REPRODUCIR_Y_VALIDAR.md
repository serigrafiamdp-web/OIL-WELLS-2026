# Reproducción y verificación técnica

## Requisitos

- VICE (preferiblemente x64sc); entorno C64 PAL como referencia.
- LVLLVL para importar y editar JSON de caracteres.
- Python 3 para verificar archivos y utilizar el exportador histórico.

## Prueba del último PRG de jugabilidad

```text
PRG: PRG/jugables/OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg
LOAD address: $0801
BASIC: 10 SYS(2084)
```

En VICE: montar/cargar el PRG como programa C64, ejecutar `RUN` si corresponde y comprobar W/S/A/D. El controlador de joystick original debe seguir operativo; no cambiar todas las lecturas de `$DC01` indiscriminadamente.

**Advertencia:** el PRG original de referencia es COPY SOFT; otros empaquetados o cracks pueden desplazar las direcciones.

## Visores estáticos retirados

Se eliminaron los ocho PRG que solo mostraban niveles. Para revisar mapas, utilizar `LVLLVL/`, `mapas/` y `previews/`. Los únicos PRG del repositorio son los tres TEST jugables.

## Prueba LVLLVL

Importar `LVLLVL/OILS_WELL_8_FRAMES_TEST03_COLORES_POR_NIVEL.json` y comprobar:
- grid 40×25 y ocho frames;
- mapa e índices originales (no reorganizados);
- tileset de 256 entradas, originales 0–127;
- propiedades de paleta diferentes según nivel;
- archivos `.bin` de respaldo conservados.

## Verificación de integridad SHA-256

En Python (desde raíz del proyecto):

```bash
python tools/verificar_recursos.py
```

El verificador comprueba los SHA-256 exactos de los **tres PRG jugables**, las longitudes de los mapas/charset/colores y la estructura básica de los nueve JSON LVLLVL. El archivo `manifest/archivos_sha256.json` es un inventario **histórico** y contiene referencias a recursos retirados: no usarlo como inventario de la rama actual. Esta prueba estructural no sustituye una sesión de VICE.

## Reproducción desde el PRG de origen

El exportador histórico TEST01, `tools/exportador_historico_test01.py`, analiza `oils well.prg` (COPY SOFT) para extraer ocho mapas y tileset con una vista previa. No restaura por sí mismo los colores TEST03.

**La diferencia entre el MASTER de controles y el MASTER gráfico es intencional:** uno es un PRG jugable, el otro es el JSON LVLLVL con ocho niveles. No se ha confirmado una reinserción que una ambas ramas.

## Reportar nuevos TEST

Para cada prueba posterior registrar fecha, base exacta SHA-256, parches, nivel, comandos probados, pantalla de error y resultado (PASS VICE, PASS estructural, FAIL). Mantener copias históricas.
