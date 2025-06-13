# 📦 Flet App Template

```
⬆️ (Replace above with your app's name)
```

Description of the app ...

## 🔧 Setup Instructions

### 1. Clone & Create Virtual Environment

This projects uses uv as package manager,
Make sure you have `uv` installed (`pip install uv`).

```bash
make venv
```

### 2. Install Dependencies

```bash
source .venv/bin/activate
make install
```

---

## ▶️ Run the App

```bash
make start
```

Or if you like doing things the long, inefficient way:

```bash
flet run main.py
```

---

## 📚 Makefile Usage

```bash
make help
```

This will show you all the available make commands:

- `make venv` — Create a virtual environment using `uv`
- `make install` — Sync dependencies from `pyproject.toml`
- `make start` — Launch the app
- `make clean` — Delete `.venv`, caches, and other junk

Don't forget to activate the virtual environment:

```bash
source .venv/bin/activate
```

To deactivate:

```bash
deactivate
```
