# Daily Log

## Date: [05-05-2025]

### What I Learned:
- Markdown Mastery: Gained hands-on experience with advanced Markdown features, including syntax for lists, links, images, and fenced code blocks.

- Mermaid Diagrams: Learned how to create and render sequence diagrams using Mermaid syntax inside MkDocs with the proper plugin and Markdown formatting.

- Draw.io for Architecture: Used Draw.io to visually map out a 3-tier architecture and system design, reinforcing the importance of visual communication.

- Documentation Structure: Understood how to organize technical documents using mkdocs.yml navigation, and split content into logical files.

- MkDocs Configuration: Practiced setting up mkdocs-material, configuring plugins like search and mermaid2, and customizing the theme using overrides/.

- Static Site Hosting: Learned how to preview the documentation locally and serve it on a static site using mkdocs serve.

### What Confused Me:
- Filename and Navigation Mismatch: At times, issues like case sensitivity or missing files in mkdocs.yml nav: section led to 404 errors, which were tricky to debug.

- Preview vs. Build Differences: There were slight differences in rendering during mkdocs serve and the final build, making it harder to validate fixes quickly

## Date: [06/07-05-2025]

### What I Learned:
- Python Packaging & CLI
How to create and structure a reusable Python package (helloworld_nikita) with a CLI tool (many_hellos) using Typer.

Packaging the module using pyproject.toml, and installing it in editable mode with pip install -e.

Reusing the say_hello logic as a library and invoking it from multiple places.

- Config Management
Used environment variable CONFIG_PATH to dynamically load YAML config files from an external location.

Implemented a fallback mechanism when the config file is not found—ensuring the app still runs with defaults.

Learned how to set environment variables in PowerShell ($env:CONFIG_PATH="...").

- Logging
Set up proper logging using Python’s logging module.

Controlled the logging level dynamically via PYTHONLOGLEVEL environment variable.

- Debugging & Interpretation
Interpreted warnings like No config file found...using defaults not as errors, but as graceful fallback behavior.

Ensured user-friendly messages with logging instead of exceptions.

- Git & File Management
Understood Git’s limit on staging more than 100 files and resolved it by adding the folder directly (git add folder_name/).

Learned to manage .gitignore, clean untracked files with git clean -fd, and better organize project structure.




### What Confused Me:
- Config Path Handling: Unsure whether to run the $env:CONFIG_PATH=... in the many_hellos or helloworld_nikita terminal (answer: run it where you execute the CLI).

- Editable Installation: Thought the pip install -e should be run inside the inner package folder—instead, it must point to the root where pyproject.toml lives.

- Warning as Errors: Initially perceived WARNING:helloworld_nikita.config:No config file found... as an error. But it's actually an intentional fallback that shows the program is robust to missing config files.

- Git Limitation: Misunderstood Git’s “try fewer than 100 files” message as a hard error—later realized you can still add a folder at once without issue.

---