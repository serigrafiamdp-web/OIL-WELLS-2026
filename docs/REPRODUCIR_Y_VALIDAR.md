# Reproducción y verificación técnica

## Requisitos

- VICE (preferiblemente x64sc); entorno C64 PAL como referencia.
- LVLLVL para importar y editar JSON de caracteres.
- Python 3 para verificar archivos y utilizar el exportador histórico.

## Prueba del último PRG de jugabilidad

```text
PRG: prg/controles/OILS_WELL_TEST03_W_FIRE_SAD_MOVIMIENTO.prg
LOAD address: $0801
BASIC: 10 SYS(2084)
```

En VICE: montar/cargar el PRG como programa C64, ejecutar `RUN` si corresponde y comprobar W/S/A/D. El controlador de joystick original debe seguir operativo; no cambiar todas las lecturas de `$DC01` indiscriminadamente.

**Advertencia:** el PRG original de referencia es COPY SOFT; otros empaquetados o cracks pueden desplazar las direcciones.

## Prueba de los visores

```text
prg/visores-estaticos/OILS_WELL_NIVEL_01_ESTATICO.prg
...
prg/visores-estaticos/OILS_WELL_NIVEL_08_ESTATICO.prg
```

Cada visor es un PRG independiente con BASIC `10 SYS2061`, carga en `$0801`, imagen estática en `$6000` y charset en `$7000`, color blanco temporal. Sin lógica de juego. La simulación de CPU 6510 confirmó la copia del mapa/charset; registrar PASS visual en VICE solo si se ejecuta realmente.

## Prueba LVLLVL

Importar `lvllvl/OILS_WELL_8_FRAMES_LVLLVL_TEST03_COLORES_POR_NIVEL.json` y comprobar:
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

El verificador toma `manifest/archivos_sha256.json` y compara tamaño y SHA-256 de cada recurso recuperado.

## Reproducción desde el PRG de origen

El exportador histórico TEST01, `tools/exportador_historico_test01.py`, analiza `oils well.prg` (COPY SOFT) para extraer ocho mapas y tileset con una vista previa. No restaura por sí mismo los colores TEST03.

**La diferencia entre el MASTER de controles y el MASTER gráfico es intencional:** uno es un PRG jugable, el otro es el JSON LVLLVL con ocho niveles. No se ha confirmado una reinserción que una ambas ramas.

## Reportar nuevos TEST

Para cada prueba posterior registrar fecha, base exacta SHA-256, parches, nivel, comandos probados, pantalla de error y resultado (PASS VICE, PASS estructural, FAIL). Mantener copias históricas.
