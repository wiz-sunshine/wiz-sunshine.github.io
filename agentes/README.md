# Markdown para agentes

GitHub Pages siempre responde HTML. Para que un agente que pide `Accept: text/markdown` reciba Markdown (y un 404
en Markdown), `worker.js` corre en Cloudflare delante de Pages:

- `Accept: text/markdown` → la versión `.md` de la página (`/` → `/index.md`, `/about` → `/about.md`,
  `/rubros/` → `/rubros/index.md`), con `Content-Type: text/markdown` y `Vary: Accept`.
- Si no existe → `404` con el cuerpo de `/404.md`.
- Cualquier otro pedido → lo de siempre, con `Vary: Accept` agregado.

Los `.md` los escribe `herramientas/generar_paginas.py`; el de la portada sale a mano de ahí mismo, así que cuando
cambia `index.html` hay que revisar `index_md()`.

## Desplegar

```sh
cd agentes && npx wrangler deploy
```

## Verificar

```sh
curl -sS -i -H 'Accept: text/markdown' https://vueltito.legios.com.ar/            # 200, text/markdown, Vary: Accept
curl -sS -i -H 'Accept: text/html' https://vueltito.legios.com.ar/                # 200, text/html, Vary: Accept
curl -sS -i -H 'Accept: text/markdown' https://vueltito.legios.com.ar/no-existe   # 404, text/markdown
```
