# OIL'S WELL 2026 — Modificación y preservación (C64)

Proyecto técnico para estudiar, modificar y preservar el funcionamiento de **Oil's Well en Commodore 64**, incluyendo controles, niveles y exportación de sus gráficos al editor **LVLLVL**.

**Idioma de trabajo y documentación: español.** Este repositorio está pensado para que otro programador pueda continuar el desarrollo sin depender de conversaciones anteriores.

## Estado actual

- **Ocho niveles originales extraídos** del PRG de referencia: mapas de caracteres 40×25.
- **Tileset original** de 128 caracteres de 8×8; el exportador completa 256 entradas para LVLLVL.
- **TEST03 de gráficos:** proyecto LVLLVL de **8 frames con paletas y Color RAM estáticas recuperadas por nivel**, más exportaciones individuales.
- **Modificaciones de controles:** prototipos TEST01 (WASD/SPACE), TEST02 (retracción automática) y TEST03 (W/FIRE y movimiento), documentados con sus diferencias de bytes.
- **PRG de visualización estática por nivel:** ocho visores de mapa; no son ejecutables del juego completo.

> **Importante:** los tests del juego tienen archivos PRG construidos, pero esta documentación no convierte automáticamente su existencia en PASS de jugabilidad. El resultado de cada prueba en VICE debe registrarse por separado. Los JSON han pasado comprobaciones de estructura y extracción; LVLLVL no reproduce por sí solo todos los efectos raster del juego.

## Por dónde empezar

| Necesidad | Archivo |
| --- | --- |
| Editar todos los mapas juntos | [Proyecto LVLLVL de 8 frames](LVLLVL/OILS_WELL_8_FRAMES_TEST03_COLORES_POR_NIVEL.json) |
| Editar un nivel individual | [Carpeta de 8 JSON individuales](LVLLVL/niveles/) |
| Comprender cómo se extrajeron | [Mapa técnico de memoria](docs/MAPA_TECNICO.md) |
| Revisar qué se modificó | [Controles y pruebas](docs/CONTROLES_Y_TESTS.md) |
| Regenerar PRG de prueba desde una copia personal del juego | [Reconstructor de parches](herramientas/reconstruir_prg_controles.py) |
| Continuar como desarrollador | [Guía para programadores](docs/GUIA_PROGRAMADORES.md) |
| Ver pendientes e ideas | [Plan de trabajo](docs/ROADMAP.md) |

## Cómo abrir los niveles en LVLLVL

1. Abrir [LVLLVL](https://github.com/jaammees/lvllvl) o nuestra versión de trabajo compatible.
2. Importar `LVLLVL/OILS_WELL_8_FRAMES_TEST03_COLORES_POR_NIVEL.json`.
3. Verificar los **8 frames** y el **tileset 8×8**. Cada frame corresponde a un nivel.
4. Para editar por separado, utilizar los ocho JSON de `LVLLVL/niveles/`.

Se conservan los índices originales de caracteres. **No** se han incorporado enemigos, sprites ni lógica de colisión en el JSON.

## Estructura del repositorio

```text
OIL-WELLS-2026/
├── README.md
├── LVLLVL/
│   ├── OILS_WELL_8_FRAMES_TEST03_COLORES_POR_NIVEL.json
│   └── niveles/
│       ├── NIVEL_01.json
│       └── ... NIVEL_08.json
├── herramientas/
│   └── reconstruir_prg_controles.py
└── docs/
    ├── GUIA_PROGRAMADORES.md
    ├── MAPA_TECNICO.md
    ├── CONTROLES_Y_TESTS.md
    ├── FORMATOS_Y_LIMITACIONES.md
    └── ROADMAP.md
```

## Referencias y preservación

El juego original es software histórico de terceros. El repositorio se centra en **análisis técnico, metadatos, exportaciones para edición y parches reproducibles**. No se sube aquí una copia completa del juego original ni se presume permiso de redistribución. Las modificaciones de controles pueden reconstruirse localmente desde un PRG original compatible y verificado por SHA-256.

La **base de comparación** es el PRG denominado `oils well.prg` (edición COPY SOFT, 38.405 bytes, carga $0801). El archivo original no se modifica al aplicar parches; se producen salidas nuevas.

Este trabajo se desarrolla como proyecto de investigación y modernización; no es una edición oficial de los autores originales.
