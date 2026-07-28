# 8b-is — Standard Galactic Raw Research Repository & MCP Tooling

> **8b-is**: Open research vault for graph-theoretic foundations of quantum calculus, Erdős phase transitions, BitNet b1.58 ternary quantization, spectral rigidity, and agentic loop engineering.

---

## 🏛️ Repository Overview

This repository hosts raw research papers, mathematical proofs, LaTeX blueprints, and Model Context Protocol (MCP) server tooling for **AXIOM QUANT**.

- **Admin Collaborator:** `@standardgalactic`
- **Owner:** `@peterlodri-sec`
- **MCP Server Tool:** `mcp/raw_research_mcp.py`
- **Raw Research Directory:** `raw_research/`

---

## 📂 Directory Structure

```
8b-is/
├── README.md                     # Repository Overview & Quickstart
├── raw_research/                 # Raw research papers, LaTeX notes & blueprints
│   ├── README.md                 # Contribution Guide for Researchers & Agents
│   ├── paper_template.md         # Markdown / LaTeX research template
│   └── 01-sample-blueprint.md   # Sample raw research document
└── mcp/                          # Custom Model Context Protocol (MCP) Server
    ├── raw_research_mcp.py       # MCP Server implementation
    └── requirements.txt          # Python dependencies
```

---

## 🤖 MCP Server Integration (`raw_research_mcp`)

This repository provides an MCP server (`mcp/raw_research_mcp.py`) allowing AI agents (Claude, Antigravity, Antigravity CLI) to dynamically interact with `raw_research/`:

### Available MCP Tools
- `submit_raw_research(title, author, content, tags)`: Submits a new raw research paper to `raw_research/`.
- `list_raw_research()`: Lists all raw research papers in the vault.
- `search_raw_research(query)`: Searches across paper titles, tags, and LaTeX equations.
