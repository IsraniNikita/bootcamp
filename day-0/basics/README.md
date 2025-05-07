# nikitaisrani-hello 🐍

This Python package was developed as part of a learning journey covering Python packaging, publishing, using third-party libraries, and building command-line tools.

## 🛠️ Project Breakdown

This project is structured across three exercises:

1.  **📦 ex-basics-1: Package Setup & Publishing**
2.  **✨ ex-basics-2: Enhanced Output with `rich`**
3.  **⌨️ ex-basics-3: CLI Application with `typer`**

---

## ✅ ex-basics-1: Package Setup & Publishing

-   Initialized the application using `uv init`.
-   Created a virtual environment with `uv venv` and activated it.
-   Developed a Python module named `nikitaisrani_hello` containing code that greets a provided name or "world" by default.
-   Packaged the module for distribution.
-   Published the package to [TestPyPI](https://test.pypi.org/project/nikitaisrani-hello/) for testing.

    🔗 **TestPyPI Link:** [nikitaisrani-hello on TestPyPI](https://test.pypi.org/project/nikitaisrani-hello/)

## 🎬 Video Demo: ex-basics-1

[**Link to Video Demo of Package Setup & Publishing**](https://drive.google.com/file/d/1oxyK8UfN3_IGIBvFBOq7mPnRSxsN1PXN/view?usp=sharing)
*(This video demonstrates the package creation, setup, and publishing to TestPyPI.)*

## ✨ ex-basics-2: Enhanced Output with `rich`

-   Installed the `rich` library:
    ```bash
    uv pip install rich
    ```
-   Modified the `nikitaisrani_hello` module to use `rich` for styled console output.

    ```python
    from rich.console import Console

    console = Console()
    console.print("Hello, [bold magenta]world[/bold magenta]!", style="green")
    ```

## 🎬 Video Demo: ex-basics-2

[**Link to Video Demo of Rich Integration**](https://drive.google.com/file/d/1plqhg9YzTJdtABRvncv5OEOX9NspJ-jG/view?usp=sharing)
*(This video demonstrates the enhanced output using the `rich` library.)*

## ⌨️ ex-basics-3: CLI Application with `typer`

-   Installed the `typer` library:
    ```bash
    uv pip install typer
    ```
-   Used `typer` to build a command-line interface within the `nikitaisrani_hello` module.
-   Configured the CLI application in `pyproject.toml` for automatic installation with the package.

    **CLI Usage:**
    ```bash
    nikitaisrani-hello hello --name [Your Name]
    ```

    **Example:**
    ```bash
    nikitaisrani-hello hello --name Nikita
    ```

    **Sample Output:**
    ```
    Hello, Nikita!
    ```

## 🎬 Video Demo: ex-basics-3

[**Link to Video Demo of Typer CLI**](https://drive.google.com/file/d/1F5a-Bn2vvtMUW_sz9er2S_UuLCLCNaYf/view?usp=sharing)
*(This video demonstrates the installation of the package and running the Typer command-line application.)*

---

## ⚙️ Development Setup

1.  **Initialize project (if not already done):**
    ```bash
    uv init
    ```

2.  **Create and activate virtual environment:**
    ```bash
    uv venv
    source .venv/bin/activate  # macOS/Linux
    .\.venv\Scripts\activate   # Windows
    ```

3.  **Install the package in editable mode:**
    ```bash
    uv pip install -e .
    ```

## 📦 Installation

You can install this test package from TestPyPI using pip:

```bash
pip install -i [https://test.pypi.org/simple/](https://test.pypi.org/simple/) nikitaisrani-hello