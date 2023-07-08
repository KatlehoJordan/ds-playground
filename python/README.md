<!-- markdownlint-disable MD029 -->

# `python` playground for data science

This container is meant to be used for rapid development of data science projects.

## Getting started

1. Fork the repository
2. Clone the repository locally
3. Use VS Code Dev containers to build a base container
4. Open `main.py` to start getting an introduction to the functionality.

## Using alias `python-playground`

This alias should open a VS Code session in the correct location. Then use VS Code to restart the Dev Container.

```sh
python-playground
```

### Running `ipython` from within the container

Ensure that Docker desktop is running. Then:

```sh
docker run --rm -i --name python-playground python-playground
```

This will build a container based on the cached docker image `python-playground` and then remove the container after it finishes.

Alternatively, if you have the alias in your shell profile:

```sh
ipython
```

## Next steps

- Create demo notebook for Autoviz
- [Create demo for Django](https://code.visualstudio.com/docs/python/tutorial-django)
- [Create demo for Flask](https://code.visualstudio.com/docs/python/tutorial-flask)
- ensure that python linting is working with black and isort
  - Black format on save is not converting long strings that are split with slashes into strings wrapped in parenthesis)
  - Black is not complaining even though I have set line length very low
  - Pylint is not respecting when I try to update the max line length argument, still complaining even if I bump it up a a lot
- Get the python REPL to automatically send an entire block of code instead of just the line and then advance to the next line. [This discussion indicates the issue is currently being ignored](https://github.com/microsoft/vscode-python/issues/18105).