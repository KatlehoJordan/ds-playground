<!-- markdownlint-disable MD029 -->

# Data Science Playground

This repository is meant to provide quick ways to get started in reproducible data-science docker containers for:

- `python`
- `r`

## Getting started

1. Fork the repository
2. Clone the repository locally
3. Decide if you would like to use a `python` or an `r` container, then open a new VS Code session in `python-playground` or `r-playground` depending on which language you would like to use.
4. Follow the `README.md` instructions in the respective `<language>-playground` folder.

## Backlog

- Find a way to build images that are smaller
  - Tried putting images onto GHCR then pulling from there, but they were still 2.01 GB (python) and very slow to pull (10 minutes). Plus, I believe there is a cost for hosting images.
