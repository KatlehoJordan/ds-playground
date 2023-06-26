<!-- markdownlint-disable MD029 -->

# Python for ds container

This container is meant to be used for rapid development of data science projects.

## Getting started

1. Fork the repository
2. Clone the repository locally
3. Use VS Code Dev containers to build a base container
4. From a terminal, run `bash .devcontainer/install-vs-code-extensions.sh` to install the VS Code Extensions.

- If any extensions indicate that a reload is required, reload.

5. From a terminal, use `sudo python main.py` to verify you have root user access and that `python` is working.
6. Go to `main.py` and use `shift + enter` to try to initiate the REPL in `ipython`.

- If the REPL does not work at all, perhaps the wrong version of the python extension is being used. See if a reload fixes.
- If the REPL does not open in `ipython`, either it is not installed, or the settings are not configured to open it in `ipython`

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
    - A standalone file
    - A module from any file  

## Next steps

1. Validate R works with:

- with VS Code Debugger
- with Jupyter Notebook support
- with R Markdown support
- building a Shiny app

2. Publish the finished image on GitHub for easier retrieval and faster building

3. As your project gets more complex, get python linters playing well together starting with black, then isort
   1. Black format on save is not converting long strings that are split with slashes into strings wrapped in parenthesis)
   2. Pylint is not respecting when I try to update the max line length argument, still complaining even if I bump it up a a lot
   3. Black is not complaining even though I have set line length very low
4. Get the python REPL to automatically send an entire block of code instead of just the line and then advance to the next line. [This discussion indicates the issue is currently being ignored](https://github.com/microsoft/vscode-python/issues/18105).
