<!-- markdownlint-disable MD029 -->

# `python` playground for data science

This container is meant to be used for rapid development of data science projects.

## Ongoing work

1. Minimize the image size for building this so as to speed up installation
   1. Using poetry now
   2. Want scikit learn and seaborn, but all else should non-standard dependencies that have their own instructional jupyter notebooks to show how to use them (lazypredict, tensorflow, autoviz, pytest)
   3. Then improve the documentation below

## Getting started

1. Fork the repository
2. Clone the repository locally
3. Use VS Code Dev containers to build a base container
4. Open `main.py` to start getting an introduction to the functionality.

## Next steps

- Create demo notebook for Autoviz
- [Create demo for Django](https://code.visualstudio.com/docs/python/tutorial-django)
- [Create demo for Flask](https://code.visualstudio.com/docs/python/tutorial-flask)
- ensure that python linting is working with black and isort
  - Black format on save is not converting long strings that are split with slashes into strings wrapped in parenthesis)
  - Black is not complaining even though I have set line length very low
  - Pylint is not respecting when I try to update the max line length argument, still complaining even if I bump it up a a lot
- Get the python REPL to automatically send an entire block of code instead of just the line and then advance to the next line. [This discussion indicates the issue is currently being ignored](https://github.com/microsoft/vscode-python/issues/18105).
