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

## Next steps

1. CodeGPT extension: https://codegpt.co/
2. Get the python REPL to automatically send an entire block of code instead of just the line
3. Get the python REPL to advance the cursor after running some code
4. Add R
  - with radian
  - with VS Code Debugger
  - with Jupyter Notebook support


## Not yet tried

- R Markdown support
