// Worker de Cloudflare delante de GitHub Pages: a quien pide Markdown (Accept: text/markdown) le da la versión .md
// de la página que generó herramientas/generar_paginas.py; a todos los demás, la página de siempre. Pages no puede
// mirar el Accept, por eso esto vive en el borde. Ver agentes/README.md.

const MD = "text/markdown; charset=utf-8";

// Cuánto prefiere el cliente cada tipo, según el Accept (q=0 es "no"). Sin Accept, se asume HTML.
export function prefiereMarkdown(accept) {
  if (!accept) return false;
  let md = 0, html = 0;
  for (const parte of accept.split(",")) {
    const [tipo, ...params] = parte.trim().toLowerCase().split(";");
    const qp = params.map((p) => p.trim()).find((p) => p.startsWith("q="));
    const q = qp ? Number(qp.slice(2)) : 1;
    if (Number.isNaN(q)) continue;
    if (tipo === "text/markdown" || tipo === "text/x-markdown") md = Math.max(md, q);
    else if (tipo === "text/html" || tipo === "application/xhtml+xml") html = Math.max(html, q);
  }
  return md > 0 && md >= html;
}

// Dónde puede estar el .md de una ruta, en orden.
export function candidatos(ruta) {
  if (ruta.endsWith("/")) return [ruta + "index.md"];
  if (ruta.endsWith(".html")) return [ruta.slice(0, -5) + ".md"];
  if (ruta.endsWith(".md")) return [ruta];
  if (/\.[a-z0-9]+$/i.test(ruta.split("/").pop())) return []; // .xml, .txt, imágenes: no tienen versión Markdown
  return [ruta + ".md", ruta + "/index.md"];
}

function conVary(headers) {
  const h = new Headers(headers);
  const vary = (h.get("Vary") || "").split(",").map((v) => v.trim()).filter(Boolean);
  if (!vary.some((v) => v.toLowerCase() === "accept")) vary.push("Accept");
  h.set("Vary", vary.join(", "));
  return h;
}

function markdown(cuerpo, status, canonical) {
  const h = new Headers({ "Content-Type": MD, "Vary": "Accept", "Cache-Control": "public, max-age=600",
    "X-Content-Type-Options": "nosniff" });
  if (canonical) h.set("Link", `<${canonical}>; rel="canonical"`);
  return new Response(cuerpo, { status, headers: h });
}

export default {
  async fetch(request, env, ctx, origen = fetch) {
    const url = new URL(request.url);
    const metodo = request.method;
    if ((metodo === "GET" || metodo === "HEAD") && prefiereMarkdown(request.headers.get("Accept"))) {
      for (const ruta of candidatos(url.pathname)) {
        const r = await origen(new URL(ruta, url).toString(), { headers: { Accept: "text/markdown" } });
        if (r.ok) {
          const canonical = new URL(url.pathname.replace(/\.md$/, "").replace(/\/index$/, "/"), url).toString();
          return markdown(metodo === "HEAD" ? null : await r.text(), 200, canonical);
        }
      }
      // ¿Existe como otra cosa (un .xml, una imagen)? Se entrega tal cual.
      const tal = await origen(request);
      if (tal.status !== 404) return new Response(tal.body, { status: tal.status, headers: conVary(tal.headers) });
      const no = await origen(new URL("/404.md", url).toString());
      const cuerpo = no.ok ? await no.text()
        : "# No encontramos esa página\n\nMirá https://vueltito.legios.com.ar/llms.txt\n";
      return markdown(metodo === "HEAD" ? null : cuerpo, 404, null);
    }
    const r = await origen(request);
    return new Response(r.body, { status: r.status, statusText: r.statusText, headers: conVary(r.headers) });
  },
};
