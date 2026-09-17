# OKF source catalog (maintainers)

**This folder is not the recommended install path for ChatGPT, Gemini, Claude, or other end users.**

Consumers should grab ready-to-load files from [`packaging/`](../packaging/):

- `packaging/compiled/dignified-language.md` or `trauma-informed.md` (any model)
- `packaging/chatgpt/`, `packaging/gemini/`, or `packaging/releases/` for platform-specific installs

`okf/` is the machine-readable source catalog. Maintainers edit here; `scripts/build.py` renders into `packaging/`. The weekly test bench scores against these rule files.

## Bundle contents

See [index.md](index.md) for the bundle directory listing and [load-order.md](load-order.md) for sequencing guidance when you need fine-grained control (custom loaders, scoring, or contributing).
