# ds_playground

Steps taken to create this repo:
1. Create `Dockerfile` with `FROM jupyter/datascience-notebook:r-4.2.2`.
2. Build as dev container using options 'From Dockerfile' and do not bother to install other features.
3. Create a GitHub Codespace.
4. Reopen the codespace with VS Code locally.
5. Update `Dockerfile` with details for `radian`
6. Update `devcontainer/devcontainer.json` with details to get root access so can make changes to `.bashrc`
