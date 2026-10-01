# BrotherCast

Podcast de conversas honestas com pessoas reais sobre dificuldades reais — e o **Movimento 1%**, que transforma essas conversas em um passo praticável por dia.

> **Experiências que conectam. Conversas que destravam.**

---

## 📘 Documento oficial

| Documento | Arquivo | Status |
|---|---|---|
| **BrotherCast Master 1.0** | [`docs/BROTHERCAST-MASTER-1.0.md`](docs/BROTHERCAST-MASTER-1.0.md) | ✅ vigente |
| Temporada 1 | — | ▢ próximo |
| Sistema de Conteúdo | — | ▢ |
| Kit Visual Definitivo | — | ▢ |
| Lançamento de 30 Dias | — | ▢ |

O **Master 1.0** é a fonte única da verdade: manifesto, posicionamento, arquitetura da marca, público, tom de voz, pilares, identidade visual, regras editoriais, ecossistema e sistema de produção.
Qualquer pessoa — editor, designer, produtor, convidado ou IA — deve conseguir ler só esse arquivo e saber **o que é, o que não é e como produzir BrotherCast**.

> ⚠️ Não existe versão paralela desse documento em outra ferramenta. Mudança de diretriz se faz **aqui**, com registro no changelog.

**Precisa briefar alguém rápido?** Copie o bloco da seção *15 — Briefing curto para IAs e colaboradores*.

---

## 🗂 Estrutura do repositório

```
.
├── index.html                      # landing page pública
├── manual/index.html               # Master 1.0 em versão navegável (gerado)
├── docs/BROTHERCAST-MASTER-1.0.md  # fonte da verdade
├── tools/build_manual.py           # gera manual/ a partir de docs/
└── netlify.toml
```

## 🔧 Rodando localmente

```bash
python3 -m http.server 8000
# landing page → http://localhost:8000/
# manual       → http://localhost:8000/manual/
```

## ♻️ Regerando o manual

O `manual/index.html` é **gerado**. Edite sempre o Markdown, nunca o HTML.

```bash
pip install markdown
python3 tools/build_manual.py
```

---

> O ontem ensina. O amanhã inspira. Mas é hoje que a vida acontece.
