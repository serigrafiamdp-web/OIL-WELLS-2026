# Próximos pasos / backlog

## Fase 1 — Congelar y reproducir los PASS

- [x] Recuperar PRG TEST01/02/03 de controles y huellas SHA.
- [x] Recuperar los ocho mapas originales, capas 40×25 y charset.
- [x] Recuperar Color RAM por nivel y JSON LVLLVL TEST03 con ocho frames.
- [ ] Verificar nuevamente TEST03 jugable en VICE x64sc y guardar una captura/VSF con versión.
- [x] Retirar los ocho PRG visores estáticos y dejar únicamente TEST01, TEST02 y TEST03 jugables.
- [ ] Comprobar importación de los ocho frames en la versión concreta de LVLLVL usada por el proyecto.

## Fase 2 — Editor gráfico a juego real

- [ ] Documentar qué bytes de mapa se usan para decoración y cuáles para colisiones/objetos.
- [ ] Validar la reconstrucción de los 24 bytes finales de cada bloque de `$400`.
- [ ] Implementar un inyector controlado de mapas/charset en el PRG de la misma variante COPY SOFT.
- [ ] Comparar resultados contra mapa/color originales antes de permitir editar colisiones.
- [ ] Reconciliar split raster, bitmap hires y multicolor con el editor LVLLVL.
- [ ] Mantener backups y rollback por TEST. No desactivar controles ni limitaciones arbitrariamente.

## Fase 3 — Mejoras del juego

- [ ] Decidir controles opcionales (WASD/joystick), preservando TEST03.
- [ ] Medir colisiones, trayectorias y FPS de la retracción tras cada cambio.
- [ ] Investigar soporte para nuevos mapas sin destruir tablas internas o scroll.
- [ ] Probar en PAL y NTSC si se modifican interrupciones/raster o temporización.

## Políticas

- No sobrescribir un TEST marcado PASS.
- Cada parche debe ser localizable por dirección y fichero, con hash y desensamblado.
- Separar el derecho de uso del código original del código de herramientas propio. Es un proyecto de investigación sobre un juego comercial existente.
