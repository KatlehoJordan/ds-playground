<!-- markdownlint-disable MD029 -->

# Data Science Playground

This repository is meant to provide quick ways to get started in reproducible data-science docker containers for:

- `python`
- `r`

## Getting started

1. Fork the repository
2. Clone the repository locally
3. Open a new VS Code session in `python` or `r` depending on which language you would like to use.
4. Follow the `README.md` instructions in the respective folder.

## Strengths and Weakness of the languages

**Strengths for `python`:**

- More users, so:
  - More extensions with easier setup
  - More tutorials and useful hints from GitHub Copilot
  - More standardized formatting rules
- More modular imports when building own packages
- Less overhead to build own packages
- Fewer dependencies to get it running for use in Jupyter
- Much smaller diskspace and memory footprint

**Strengths for `r`:**

- The piping syntax from `tidyverse` can make data analysis very fast
- The documentation is more standardized and easier to retrieve (`?<function name>`)

## Next steps

- See if you can find a way to make all of your packages 'slim'?
  - YouTube videos by 'slim.ai' called 'SlimDevOps', and use 'DockerSlim' to try to reduce the docker container sizes
