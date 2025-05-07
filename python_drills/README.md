# Python Drills: Hello World and Beyond

This project contains a series of Python drills designed to explore various aspects of Python development, including library creation, command-line interfaces, configuration management, logging, and packaging.

## Hello World Project

This initial step involved creating a simple "hello world" project with the following structure:

-   A module exporting a function `say_hello(name)` that returns a greeting string.
-   A command-line interface using Typer that takes a name as an argument and prints the result of `say_hello()`.
-   Publication of this library and CLI to a development PyPI repository.

## Many Hellos Project

A second project, `many-hellos`, was created to demonstrate the reusability of the `helloworld` library. This project features a command-line program (built with Typer) that:

-   Imports the `helloworld.say_hello` function.
-   Takes multiple names as input.
-   Prints a personalized greeting for each name using the imported function.

### Running the Many Hellos Program

You can see the `many-hellos` program in action in the following video:

[![Many Hellos Demo](https://drive.google.com/file/d/1X7PtdEAVBmOD3_zBxmPtmI8cooxvJjL3/view?usp=sharing)
Note: If you see a message like this:
WARNING:helloworld_nikita.config:No config file found at G:\bootcamp-projects\projects\day2\python_drills\helloworld_nikita\helloworld_nikita\config.yaml, using defaults.
Don’t worry! This just means the application couldn’t find a custom config file, so it’s happily using the default settings. Everything will still work as expected. If you’d like to personalize your configuration, you can add your own config.yaml file, and the app will pick it up automatically.




## Extending the Library with Configuration

The `helloworld` library was extended to incorporate configuration via a `config.yaml` file.

-   The `say_hello` function now loads a `num_times` parameter from the configuration.
-   The greeting is repeated `num_times`.
-   The code searches for the `config.yaml` file in the following order:
    1.  The current working directory.
    2.  Paths specified in the `CONFIG_PATH` environment variable (colon-separated).
    3.  A default `config.yaml` file shipped with the module if none are found.
-   Configuration loading logic was encapsulated into a separate file within the library.

This enhanced library was packaged and republished to the development PyPI repository.

## Testing Configuration

The extended library's configuration loading was tested through the `many-hellos` CLI in several ways:

-   By placing a `config.yaml` file in the current working directory.
-   By using the `CONFIG_PATH` environment variable to specify a configuration file location.
-   By running the CLI without any explicit configuration file, ensuring the default configuration is loaded.

## Adding Logging

Logging was integrated into both the `sayhello` module and the configuration reader within the library using Python's `logging` module.

-   Demonstrations showed how to:
    -   Turn on logging during the execution of the `many-hellos` CLI.
    -   Turn off logging.
    -   Enable logging selectively for the configuration reader code.

## Core Python Proficiency Drills

Beyond the "hello world" project, various core Python concepts were explored, including:

1.  **Data Structures:** Lists, Dictionaries, Sets, Tuples and their operations.
2.  **Comprehensions and Generator Expressions:** Creating concise and efficient data structures.
3.  **Functions and Arguments:** Different ways to define and call functions.
4.  **Scope and Closures:** Understanding variable accessibility and function factories.
5.  **Error Handling:** Using `try/except/finally` blocks and custom exceptions.
6.  **Iterators and Generators:** Creating custom iterators and using generators for efficient iteration.

## Pythonic Idioms Drills

This section focused on writing more idiomatic and Pythonic code:

1.  **EAFP vs LBYL:** Comparing different approaches to handling potential errors.
2.  **Built-in Functions and Idioms:** Leveraging useful built-in functions like `enumerate`, `zip`, `any`, `all`, etc.
3.  **Inline Expressions and Shortcuts:** Writing more concise code using inline conditionals, the walrus operator, etc.
4.  **Context Managers and `with`:** Ensuring proper resource management.

## Object-Oriented Design Drills

Object-oriented programming principles were explored:

1.  **Classes and Objects:** Defining classes, creating objects, and working with attributes and methods.
2.  **Inheritance and `super()`:** Creating class hierarchies and reusing code.
3.  **Dunder (Magic) Methods:** Customizing object behavior.
4.  **Data Classes and Named Tuples:** Creating concise classes for data storage.
5.  **Static and Class Methods:** Understanding different types of methods within a class.

## Functional Tools Drills

Functional programming concepts in Python were covered:

1.  **First-Class Functions and Lambdas:** Treating functions as objects.
2.  **Decorators:** Modifying function behavior.
3.  `functools` Utilities: Using tools like `partial` and `lru_cache`.
4.  `itertools` Essentials: Working with efficient iterators.

## Standard Library Mastery Drills

Exploration of useful modules in the Python standard library:

1.  `collections`: Specialized container datatypes.
2.  Filesystem and Path Handling: Interacting with the file system.
3.  Date and Time: Working with dates and times.
4.  Serialization (`json`, `csv`, `pickle`): Encoding and decoding data.
5.  Subprocess and Concurrency: Running external commands and managing concurrent tasks.

## Data Validation and Code Clarity Drills

Techniques for ensuring data integrity and writing readable code:

1.  Data Classes and Manual Validation: Adding validation logic to data classes.
2.  Validation with `pydantic`: Using a dedicated validation library.
3.  Field Metadata and Readability: Adding descriptions and aliases to model fields.
4.  Logging Best Practices: Effective use of the `logging` module.
5.  Code Clarity and Naming: Writing understandable and maintainable code.

## Performance and Debugging Drills

Tools and techniques for optimizing and debugging Python code:

1.  Profiling and Timing: Measuring code performance.
2.  Lazy Evaluation and Efficiency: Using generators for memory efficiency.
3.  Debugging Tools and Practices: Utilizing `pdb`, `breakpoint`, and logging for debugging.
4.  Design for Observability: Making applications easier to monitor and debug.
5.  Packaging with `pyproject.toml`: Modern Python packaging.

This README provides a high-level overview of the exercises undertaken. Each section likely contains more specific details and code examples.
