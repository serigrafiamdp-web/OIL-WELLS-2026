# Pendientes, ideas y prioridades

## Ya disponible
- [x] Localización de los ocho mapas y del charset original en el PRG COPY SOFT.
- [x] Extracción de 8 niveles a un proyecto LVLLVL de 8 frames.
- [x] Extracción de colores estáticos por nivel (TEST03 gráficos).
- [x] Ocho exportaciones JSON individuales y ocho visores PRG estáticos.
- [x] Tres modificaciones de controles como parches reproducibles desde la fuente verificada.
- [x] Documentación técnica en español.

## Próxima fase — validación
- [ ] Abrir el proyecto combinado en LVLLVL; verificar color y mapa de cada frame.
- [ ] Probar cada JSON individual y volver a guardar sin alterar índices.
- [ ] Probar los ocho visores estáticos en VICE.
- [ ] Repetir con condiciones controladas las pruebas TEST01/02/03 de controles.
- [ ] Registrar resultados en una matriz TEST/PASS/FAIL.

## Motor y gráficos
- [ ] Desensamblar completamente las rutinas de control y de retracción.
- [ ] Identificar y separar estados de juego, menú y teclado para evitar efectos secundarios.
- [ ] Documentar codificación de colisiones y elementos dinámicos de cada nivel.
- [ ] Diseñar un roundtrip LVLLVL→mapas de juego, conservando 24 bytes extra por bloque.
- [ ] Obtener estado raster exacto con VICE VSF/video y compararlo con el exportador.
- [ ] Exportar o reconstruir sprites e información de objetos si se decide editarlos.

## Optimizaciones (ideas, no implementadas)
- [ ] Controles remapeables sin romper joystick original.
- [ ] Mecanismo de retracción configurable.
- [ ] Selector de nivel para depuración.
- [ ] Herramienta automatizada que lea PRG de base y genere variantes con logs SHA.
- [ ] Integración del exportador LVLLVL y de pruebas de regresión del juego.

## Reglas
Cada mejora irá a un TEST nuevo; **no sobrescribir versiones que den PASS**. Documentar cambios de bytes/offsets, comportamiento esperado, comprobación visual y resultado. No añadir restricciones nuevas sin necesidad y sin su validación.
