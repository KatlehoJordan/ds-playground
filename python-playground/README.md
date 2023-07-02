<!-- markdownlint-disable MD029 -->

# `python` playground for data science

This container is meant to be used for rapid development of data science projects.

## Getting started

1. Fork the repository
2. Clone the repository locally
3. Use VS Code Dev containers to build a base container
4. From a terminal, run `bash .devcontainer/install-vs-code-extensions.sh` to install the VS Code Extensions.

- If any extensions indicate that a reload is required, reload.

5. From a terminal, use `sudo python main.py` to verify you have root user access and that `python` is working.

7. Open `demo.ipynb` and run the cells to ensure that the following are working as expected:

- `jupyter` notebook
- `seaborn` and `plotly`
- `pandas`, `sklearn`, and `lazypredict`
- `tensorflow`
  is setup and all common DS packages are installed
  
8. Ensure `pytest` is working by running `pytest` from a terminal
9. Ensure `pytest` integration with VS Code is working by navigating to the testing tab. Then:
    - Running the tests
    - Add a break point in a test and run them again
10. Ensure you can debug:
    - A standalone file with `python`
    - A module from any file with `python`

## Next steps

- simplify python instructions to single file going through the features like done with r
- ensure that python linting is working with black and isort
  - Black format on save is not converting long strings that are split with slashes into strings wrapped in parenthesis)
  - Pylint is not respecting when I try to update the max line length argument, still complaining even if I bump it up a a lot
  - Black is not complaining even though I have set line length very low
- Get the python REPL to automatically send an entire block of code instead of just the line and then advance to the next line. [This discussion indicates the issue is currently being ignored](https://github.com/microsoft/vscode-python/issues/18105).
