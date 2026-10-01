#!/usr/bin/env python3
"""
Gera a versão navegável (HTML) do BROTHERCAST MASTER 1.0 a partir do Markdown.

Fonte da verdade:  docs/BROTHERCAST-MASTER-1.0.md
Saída:             manual/index.html

Uso:
    pip install markdown
    python3 tools/build_manual.py
"""

from __future__ import annotations

import html
import pathlib
import re
import unicodedata

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "BROTHERCAST-MASTER-1.0.md"
OUTPUT = ROOT / "manual" / "index.html"


def slugify(text: str, _sep: str = "-") -> str:
    """Slug compatível com o GitHub, para que as âncoras do Markdown e do HTML batam."""
    text = unicodedata.normalize("NFC", text).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s_]+", "-", text).strip("-")


TEMPLATE = """<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta
      name="description"
      content="BrotherCast Master 1.0 — documento oficial de marca, filosofia e produção do BrotherCast."
    />
    <meta name="theme-color" content="#0d1117" />
    <title>BrotherCast Master 1.0 | Documento oficial</title>

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap"
      rel="stylesheet"
    />

    <style>
      :root {{
        --night: #0d1117;
        --night-deep: #080b10;
        --surface: #131a23;
        --surface-2: #19212c;
        --mustard: #e5a93d;
        --mustard-light: #f1c56b;
        --wood: #9c7247;
        --paper: #f4f1ed;
        --muted: #a0aab5;
        --line: rgba(244, 241, 237, 0.12);
        --display: "Playfair Display", Georgia, serif;
        --body: "Manrope", system-ui, sans-serif;
        --mono: "JetBrains Mono", ui-monospace, monospace;
      }}

      *, *::before, *::after {{ box-sizing: border-box; }}
      html {{ scroll-behavior: smooth; scroll-padding-top: 90px; }}

      body {{
        margin: 0;
        background: var(--night);
        color: var(--paper);
        font-family: var(--body);
        font-size: 17px;
        line-height: 1.72;
        -webkit-font-smoothing: antialiased;
      }}

      body::after {{
        position: fixed;
        inset: 0;
        z-index: 60;
        pointer-events: none;
        content: "";
        opacity: 0.03;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
      }}

      :focus-visible {{ outline: 3px solid var(--mustard-light); outline-offset: 4px; }}

      /* ---------- topbar ---------- */
      .topbar {{
        position: sticky;
        top: 0;
        z-index: 40;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        padding: 16px 28px;
        border-bottom: 1px solid var(--line);
        background: rgba(8, 11, 16, 0.88);
        backdrop-filter: blur(14px);
      }}

      .topbar a.brand {{
        font-family: var(--display);
        font-size: 1.1rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        color: var(--paper);
        text-decoration: none;
      }}

      .topbar .version {{
        padding: 4px 12px;
        border: 1px solid rgba(229, 169, 61, 0.45);
        border-radius: 999px;
        color: var(--mustard);
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
      }}

      .topbar .links {{ display: flex; align-items: center; gap: 18px; }}
      .topbar .links a {{
        color: var(--muted);
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.06em;
        text-decoration: none;
      }}
      .topbar .links a:hover {{ color: var(--mustard-light); }}

      /* ---------- hero ---------- */
      .hero {{
        position: relative;
        padding: 96px 28px 72px;
        overflow: hidden;
        border-bottom: 1px solid var(--line);
        background:
          radial-gradient(900px 420px at 18% -10%, rgba(229, 169, 61, 0.18), transparent 70%),
          radial-gradient(700px 380px at 92% 110%, rgba(156, 114, 71, 0.22), transparent 72%),
          var(--night-deep);
      }}

      .hero-inner {{ width: min(100%, 860px); margin-inline: auto; }}

      .hero .kicker {{
        margin: 0 0 18px;
        color: var(--mustard);
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.26em;
        text-transform: uppercase;
      }}

      .hero h1 {{
        margin: 0 0 18px;
        font-family: var(--display);
        font-size: clamp(2.6rem, 7vw, 4.4rem);
        font-weight: 700;
        line-height: 1.04;
        letter-spacing: -0.015em;
      }}

      .hero h1 em {{ display: block; color: var(--mustard); font-style: italic; font-weight: 400; }}

      .hero p {{ max-width: 58ch; margin: 0; color: var(--muted); font-size: 1.04rem; }}

      .hero .meta {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 30px;
      }}

      .hero .meta span {{
        padding: 7px 14px;
        border: 1px solid var(--line);
        border-radius: 999px;
        background: rgba(244, 241, 237, 0.04);
        font-size: 0.74rem;
        font-weight: 600;
        letter-spacing: 0.08em;
      }}

      /* ---------- layout ---------- */
      .layout {{
        display: grid;
        grid-template-columns: 278px minmax(0, 1fr);
        gap: 52px;
        width: min(100%, 1240px);
        margin-inline: auto;
        padding: 56px 28px 120px;
      }}

      .toc {{ position: sticky; top: 92px; align-self: start; max-height: calc(100vh - 130px); overflow-y: auto; }}
      .toc h2 {{
        margin: 0 0 14px;
        color: var(--muted);
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.22em;
        text-transform: uppercase;
      }}
      .toc ul {{ margin: 0; padding: 0; list-style: none; border-left: 1px solid var(--line); }}
      .toc li a {{
        display: block;
        padding: 7px 0 7px 16px;
        margin-left: -1px;
        border-left: 2px solid transparent;
        color: var(--muted);
        font-size: 0.84rem;
        line-height: 1.4;
        text-decoration: none;
      }}
      .toc li a:hover {{ color: var(--paper); border-left-color: var(--wood); }}
      .toc li a.active {{ color: var(--mustard); border-left-color: var(--mustard); font-weight: 600; }}
      .toc ul ul {{ display: none; }}

      /* ---------- document ---------- */
      .doc {{ min-width: 0; max-width: 80ch; }}

      .doc h1 {{ display: none; }}

      .doc h2 {{
        margin: 68px 0 22px;
        padding-top: 26px;
        border-top: 1px solid var(--line);
        font-family: var(--display);
        font-size: clamp(1.7rem, 3.4vw, 2.3rem);
        font-weight: 700;
        line-height: 1.18;
        letter-spacing: -0.01em;
      }}
      .doc h2:first-of-type {{ margin-top: 0; border-top: 0; padding-top: 0; }}

      .doc h3 {{
        margin: 44px 0 14px;
        font-size: 1.16rem;
        font-weight: 700;
        letter-spacing: 0.01em;
        color: var(--mustard-light);
      }}

      .doc h4 {{ margin: 30px 0 10px; font-size: 1rem; font-weight: 700; color: var(--paper); }}

      .doc p {{ margin: 0 0 18px; }}
      .doc a {{ color: var(--mustard); text-decoration-color: rgba(229, 169, 61, 0.4); text-underline-offset: 3px; }}
      .doc a:hover {{ color: var(--mustard-light); }}
      .doc strong {{ color: #fff; font-weight: 700; }}

      .doc ul, .doc ol {{ margin: 0 0 20px; padding-left: 22px; }}
      .doc li {{ margin-bottom: 8px; }}
      .doc li::marker {{ color: var(--mustard); }}

      .doc blockquote {{
        position: relative;
        margin: 28px 0;
        padding: 24px 28px;
        border: 1px solid rgba(229, 169, 61, 0.26);
        border-left: 3px solid var(--mustard);
        border-radius: 0 12px 12px 0;
        background: linear-gradient(100deg, rgba(229, 169, 61, 0.08), rgba(229, 169, 61, 0.01));
      }}
      .doc blockquote p {{ margin-bottom: 10px; }}
      .doc blockquote p:last-child {{ margin-bottom: 0; }}
      .doc blockquote strong {{ color: var(--mustard-light); }}
      .doc blockquote hr {{ margin: 16px 0; border: 0; border-top: 1px solid rgba(229, 169, 61, 0.25); }}

      .doc hr {{ margin: 52px 0; border: 0; border-top: 1px solid var(--line); }}

      .table-wrap {{ margin: 0 0 26px; overflow-x: auto; border: 1px solid var(--line); border-radius: 12px; }}
      .doc table {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; }}
      .doc thead th {{
        padding: 13px 16px;
        border-bottom: 1px solid var(--line);
        background: var(--surface-2);
        color: var(--mustard);
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        text-align: left;
        white-space: nowrap;
      }}
      .doc tbody td {{ padding: 13px 16px; border-bottom: 1px solid rgba(244, 241, 237, 0.07); vertical-align: top; }}
      .doc tbody tr:last-child td {{ border-bottom: 0; }}
      .doc tbody tr:nth-child(even) {{ background: rgba(244, 241, 237, 0.025); }}

      .doc code {{
        padding: 2px 6px;
        border-radius: 5px;
        background: rgba(229, 169, 61, 0.12);
        color: var(--mustard-light);
        font-family: var(--mono);
        font-size: 0.86em;
      }}

      .doc pre {{
        margin: 0 0 26px;
        padding: 22px 24px;
        overflow-x: auto;
        border: 1px solid var(--line);
        border-radius: 12px;
        background: var(--night-deep);
        line-height: 1.55;
      }}
      .doc pre code {{ padding: 0; background: none; color: var(--muted); font-size: 0.8rem; }}

      .doc input[type="checkbox"] {{ margin-right: 8px; accent-color: var(--mustard); }}
      .doc ul:has(> li > input[type="checkbox"]) {{ list-style: none; padding-left: 2px; }}

      /* ---------- footer ---------- */
      .footer {{
        padding: 48px 28px 64px;
        border-top: 1px solid var(--line);
        background: var(--night-deep);
        text-align: center;
      }}
      .footer .sig {{
        margin: 0 0 8px;
        font-family: var(--display);
        font-size: 1.5rem;
        font-weight: 700;
      }}
      .footer .tag {{ margin: 0 0 24px; color: var(--mustard); font-style: italic; }}
      .footer .quote {{ margin: 0 auto; max-width: 46ch; color: var(--muted); font-size: 0.92rem; }}

      @media (max-width: 960px) {{
        .layout {{ grid-template-columns: 1fr; gap: 0; padding-top: 36px; }}
        .toc {{
          position: static;
          max-height: none;
          margin-bottom: 44px;
          padding-bottom: 28px;
          border-bottom: 1px solid var(--line);
        }}
      }}

      @media (max-width: 620px) {{
        body {{ font-size: 16px; }}
        .topbar {{ padding: 14px 18px; }}
        .topbar .links a:not(.ghsrc) {{ display: none; }}
        .hero {{ padding: 64px 18px 52px; }}
        .layout {{ padding-inline: 18px; }}
      }}

      @media print {{
        body {{ background: #fff; color: #111; }}
        .topbar, .toc, .hero .meta {{ display: none; }}
        .doc {{ max-width: none; }}
      }}
    </style>
  </head>
  <body>
    <header class="topbar">
      <a class="brand" href="#inicio">BrotherCast</a>
      <nav class="links">
        <a href="#1-a-regra-que-vem-antes-de-todas-as-outras">Regra Zero</a>
        <a href="#2-manifesto">Manifesto</a>
        <a href="#10-ecossistema-de-conteúdo">Ecossistema</a>
        <a href="#15-briefing-curto-para-ias-e-colaboradores">Briefing</a>
        <span class="version">Master 1.0</span>
      </nav>
    </header>

    <section class="hero" id="inicio">
      <div class="hero-inner">
        <p class="kicker">Documento oficial · versão 1.0</p>
        <h1>BrotherCast Master <em>o que é, o que não é e como produzir.</em></h1>
        <p>
          Marca, filosofia, público, tom de voz, identidade visual, regras editoriais e ecossistema de
          conteúdo. Fonte única da verdade para editor, designer, produtor, convidado ou IA.
        </p>
        <div class="meta">
          <span>Outubro de 2025</span>
          <span>Status: vigente</span>
          <span>17 seções</span>
          <span>Descoberta conceitual encerrada</span>
        </div>
      </div>
    </section>

    <main class="layout">
      <aside class="toc" aria-label="Sumário">
        <h2>Sumário</h2>
        {toc}
      </aside>

      <article class="doc" id="conteudo">
        {content}
      </article>
    </main>

    <footer class="footer">
      <p class="sig">BrotherCast</p>
      <p class="tag">Experiências que conectam. Conversas que destravam.</p>
      <p class="quote">“O ontem ensina. O amanhã inspira. Mas é hoje que a vida acontece.”</p>
    </footer>

    <script>
      // Destaca no sumário a seção visível.
      const links = [...document.querySelectorAll(".toc a")];
      const byId = new Map(links.map((a) => [decodeURIComponent(a.hash.slice(1)), a]));
      const headings = [...document.querySelectorAll(".doc h2")].filter((h) => byId.has(h.id));

      if (headings.length) {{
        const observer = new IntersectionObserver(
          (entries) => {{
            entries.forEach((entry) => {{
              if (!entry.isIntersecting) return;
              links.forEach((a) => a.classList.remove("active"));
              byId.get(entry.target.id)?.classList.add("active");
            }});
          }},
          {{ rootMargin: "-88px 0px -72% 0px", threshold: 0 }}
        );
        headings.forEach((h) => observer.observe(h));
      }}
    </script>
  </body>
</html>
"""


def build() -> None:
    text = SOURCE.read_text(encoding="utf-8")

    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"slugify": slugify, "toc_depth": "2-2"}},
    )
    content = md.convert(text)

    # Tabelas roláveis no mobile.
    content = content.replace("<table>", '<div class="table-wrap"><table>').replace(
        "</table>", "</table></div>"
    )

    # Checkboxes do checklist viram inputs reais.
    content = re.sub(
        r"<li>\[ \]\s*", '<li><input type="checkbox" disabled /> ', content
    )
    content = re.sub(
        r"<li>\[x\]\s*", '<li><input type="checkbox" checked disabled /> ', content
    )

    # O sumário manual do Markdown é redundante na versão web: remove-o.
    content = re.sub(
        r'<h2 id="sumário">.*?</ol>\s*', "", content, count=1, flags=re.DOTALL
    )

    # O item "Sumário" não existe mais no corpo da página web.
    toc = re.sub(r'<li><a href="#sumário">.*?</a></li>\s*', "", md.toc, count=1)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEMPLATE.format(toc=toc, content=content), encoding="utf-8")
    print(f"ok  {OUTPUT.relative_to(ROOT)}  ({len(OUTPUT.read_text(encoding='utf-8')):,} bytes)")


if __name__ == "__main__":
    build()
