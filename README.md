# BrotherCast

Podcast de conversas honestas com pessoas reais sobre dificuldades reais — e o **Movimento 1%**, que transforma essas conversas em um passo praticável por dia.

> **Experiências que conectam. Conversas que destravam.**

---

## 🔒 Público × interno

Este repositório tem duas camadas. **Só `site/` vai para o ar.**

| | Pasta | Vai para o ar? | Conteúdo |
|---|---|---|---|
| **Público** | `site/` | ✅ sim | Propósito, manifesto, host, episódios, convidados, Movimento 1% |
| **Interno** | `docs/`, `internal/`, `tools/` | ❌ **não** | Master, Temporada, regras, estratégia, edição, distribuição, métricas |

A separação é garantida pelo `netlify.toml` (`publish = "site"`). As páginas internas levam `noindex` e faixa de aviso.

> ⚠️ Antes de publicar qualquer coisa: *isto é propósito e história (público) ou é método e critério (interno)?*

---

## 📘 Documentos oficiais

| # | Documento | Arquivo | Status |
|---|---|---|---|
| **1** | **BrotherCast Master** (v1.3) | [`docs/BROTHERCAST-MASTER-1.0.md`](docs/BROTHERCAST-MASTER-1.0.md) | ✅ vigente |
| **2** | **Temporada 1** (v1.3) | [`docs/TEMPORADA-1.md`](docs/TEMPORADA-1.md) | ✅ vigente |
| **2.1** | **Piloto E01 — roteiro de direção** (v1.0) | [`docs/PILOTO-E01.md`](docs/PILOTO-E01.md) | ✅ vigente |
| 2.1 | Roteiro de direção do piloto (E01) | — | ▢ próximo |
| 2.2 | Lista inicial de convidados | — | ▢ |
| 2.3 | Plano de gravação do Bloco A | — | ▢ |
| 3 | Sistema de Conteúdo | — | ▢ |
| 4 | Kit Visual Definitivo | — | ▢ |
| 4.1 | Manifesto BrotherCast (peça pública) | — | ▢ |
| 5 | Lançamento de 30 Dias | — | ▢ depende do Bloco A gravado |

O **Master** é a fonte única da verdade; a **Temporada 1** deriva dele. Em caso de conflito, o Master vence.

> ⚠️ Não existe versão paralela desses documentos em outra ferramenta. Mudança de diretriz se faz **aqui**, com registro no changelog.

**Precisa briefar alguém rápido?** Copie o bloco da seção *15 — Briefing curto para IAs e colaboradores* do Master. Para um colaborador externo, mande a ficha específica do trabalho dele, não o documento inteiro.

---

## 🗂 Estrutura do repositório

```
.
├── site/                           # 🌐 PÚBLICO — única pasta publicada
│   └── index.html
├── docs/                           # 🔒 fonte da verdade (markdown)
│   ├── BROTHERCAST-MASTER-1.0.md
│   ├── TEMPORADA-1.md
│   └── PILOTO-E01.md
├── internal/manual/                # 🔒 versão navegável (gerada)
│   ├── index.html                  #    Master
│   ├── temporada-1.html            #    Temporada 1
│   └── piloto-e01.html             #    Piloto E01
├── tools/build_manual.py           # gera internal/manual/ a partir de docs/
└── netlify.toml                    # publish = "site"
```

## 🔧 Rodando localmente

```bash
# site público (igual ao que o Netlify publica)
python3 -m http.server 8000 --directory site

# manual interno
python3 -m http.server 8001 --directory internal/manual
```

## ♻️ Regerando o manual

O HTML em `internal/manual/` é **gerado**. Edite sempre o Markdown em `docs/`, nunca o HTML.

```bash
pip install markdown
python3 tools/build_manual.py
```

---

> O ontem ensina. O amanhã inspira. Mas é hoje que a vida acontece.
