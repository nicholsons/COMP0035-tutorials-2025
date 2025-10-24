# 1. Docstrings

Python docstrings are special strings used to document your code.

A docstring appears as the first statement in a Python module, function, class, or method.

Using docstrings is considered good practice:

- Helps others, and yourself, understand what your code does without digging into the implementation.
- Supports documentation tools such as Sphinx or IDEs that can extract docstrings to generate user-friendly
  documentation.
- They can facilitate testing. Python's doctest module can run examples embedded in docstrings as tests.
- The can encourage good design as writing a docstring forces you to think clearly about the purpose and behavior of
  your code.

[PEP 257](https://peps.python.org/pep-0257/) is a Python standard that outlines conventions for writing docstrings such
as:

- Use triple double quotes ("""), even for one-liners.
- Start with a short summary line.
- Optionally follow with a more detailed description.
- Include descriptions of parameters and return values.

PEP 257 does not mandate a particular style of docstring. There are several popular styles such as:

- [Google-style docstring](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Numpy-style docstring]()
- [Sphinx/reStructuredText](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

It does not matter for this course which style you adopt, however when you choose one then you should be consistent in
its use.

## Docstrings and genAI

Writing a clear docstring facilitates the use of gen-AI tools to write the corresponding code.

Conversely, gen-AI can also be used to generate docstrings from code in your IDE, e.g. `/doc Google-style docstring`.

## Activity: Docstring

1. Open [cs_docstring.py](../../src/activities/starter/cq_docstring.py) and consider the docstring style. Is there a
   style you prefer to adopt in your own code?
2. Go to the `generate_histogram()` function and follow the guidance in the comment to use copilot (or other) generate a
   docstring from the code.
3. Go to the `describe()` function and follow the guidance to copilot (or other) complete the code from the docstring.


[Next activity](3-02-linting.md)