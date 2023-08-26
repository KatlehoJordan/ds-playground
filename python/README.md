<!-- markdownlint-disable MD029 -->

# `python` playground for data science

This container is meant to be used for rapid development of data science projects using `python`.

There are two ways to try to run this:

1. Locally in an Ubuntu machine using `poetry`. [See instructions below](#getting-started-locally-in-an-ubuntu-machine-using-poetry).
2. Using VS Code Dev Containers. [See instructions below](#getting-started-using-vs-code-dev-containers); this may be limited since I stopped developing in this way)

## Getting started locally in an Ubuntu machine using `poetry`

1. Verify you have python installed with `python --version`. If this is not installed, then you will need to install it. Tested version is `Python 3.11.4`
2. Verify you have `poetry` installed with `poetry --version`. If this is not installed, then you will need to install it. Tested version is `poetry 1.6.1`
3. Open a VS Code session in the `python` directory.
4. Install poetry dependencies with `poetry install`. If you encounter errors, consider that your shell profile may need to be configured differently.

## Getting started using VS Code Dev Containers

1. Open a new VS Code workspace in `python`
2. Use VS Code Dev containers to build a base container
3. Open `main.py` to start getting an introduction to the functionality.

### Using alias `python-playground`

This alias should open a VS Code session in the correct location. Then use VS Code to restart the Dev Container.

```sh
python-playground
```

#### Running `ipython` from within the container

Ensure that Docker desktop is running. Then:

```sh
docker run --rm -i --name python-playground python-playground
```

This will build a container based on the cached docker image `python-playground` and then remove the container after it finishes.

Alternatively, if you have the alias in your shell profile:

```sh
ipython
```

## Ongoing work

- Completing notebooks for w3 schools

## Next steps

- Solve why the IntelliCode find examples on GitHub is not always working, as tracked in [this GitHub issue](https://github.com/MicrosoftDocs/intellicode/issues/466)
  - Similarly, as seen in the screenshots taken for that issue, the full language service does not seem to work in jupyter notebooks, as the function signatures come through, but not the docstrings.
- Create demo notebook for Autoviz
- [Create demo for Django](https://code.visualstudio.com/docs/python/tutorial-django)
- [Create demo for Flask](https://code.visualstudio.com/docs/python/tutorial-flask)
- ensure that python linting is working with black and isort
  - Black format on save is not converting long strings that are split with slashes into strings wrapped in parenthesis)
  - Black is not complaining even though I have set line length very low
  - Pylint is not respecting when I try to update the max line length argument, still complaining even if I bump it up a a lot
- Get the python REPL to automatically send an entire block of code instead of just the line and then advance to the next line. [This discussion indicates the issue is currently being ignored](https://github.com/microsoft/vscode-python/issues/18105).
