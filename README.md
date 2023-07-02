<!-- markdownlint-disable MD029 -->

# Data Science Playground

This repository is meant to provide quick ways to get started in reproducible data-science docker containers for:

- `python`
- `r`

## Getting started

1. Fork the repository
2. Clone the repository locally
3. Decide if you would like to use a `python` or an `r` container then follow the `README.md` instructions in the respective `<language>-playground` folder.

## Ongoing work

1. Split python and r into own docker images, because putting them into one becomes way too large
   1. Starting with `python`

## Backlog

- Try building docker images with docker buildkit?: <https://jpetazzo.github.io/2021/11/30/docker-build-container-images-antipatterns/>
- publish the finished image on GitHub for easier retrieval and faster building
  - Tests so far were not convincing -> without build kit I published a python-playground image to ghcr and then pulled it, which took 10 minutes... Building it locally also took about 10 minutes. So the overhead of having 2 docker files (one for publishing to ghcr, and another for pulling from ghcr when developing locally in a dev container) seems like it might not be worthwhile
