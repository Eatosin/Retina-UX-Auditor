# Contributing to Retina

Thank you for your interest in building the future of UI Engineering.

## 🛠️ Development Workflow
1.  **Fork** the repository.
2.  **Clone** your fork locally.
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a Branch:** `git checkout -b feat/my-feature`

## ✅ Quality Standards
This repo enforces strict quality gates via GitHub Actions.
*   **Linting:** Code must pass `ruff check .`.
*   **Type Safety:** Code must pass `mypy src/`.
*   **Tests:** New features must include unit tests in `tests/`.

## 📦 Pull Request Process
1.  Ensure all local tests pass.
2.  Update documentation if you changed logic.
3.  Submit PR with a clear description of the "Physics" or "Logic" changed.