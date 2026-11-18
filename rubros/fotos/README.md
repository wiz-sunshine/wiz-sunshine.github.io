# Fotos de los sistemas por rubro

Cada página de rubro muestra hasta tres capturas. Aparecen solas cuando subís el archivo con el nombre justo; sin
ninguna, la sección "Así se ve" no se muestra.

| Página | Archivos |
|---|---|
| `/rubros/arquitectos` | `arquitectos-1.jpg` (va grande, arriba), `arquitectos-2.jpg`, `arquitectos-3.jpg` |
| `/rubros/laboratorios` | `laboratorios-1.jpg`, `laboratorios-2.jpg`, `laboratorios-3.jpg` |
| `/rubros/medicos` | `medicos-1.jpg`, `medicos-2.jpg`, `medicos-3.jpg` |

- Formato 16:10, idealmente 1600 × 1000 px y menos de 300 KB (`sips -Z 1600 -s formatQuality 80 foto.png --setProperty format jpeg --out arquitectos-1.jpg`).
- Sin datos reales de clientes ni de pacientes: usar datos de ejemplo.
- El texto alternativo y el epígrafe de cada foto están en `herramientas/contenido.py` (`"fotos"`); si la captura
  muestra otra cosa, cambiarlo ahí y correr `python3 herramientas/generar_paginas.py`.
