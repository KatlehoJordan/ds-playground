<!-- markdownlint-disable MD029 -->

# Data Science Playground

This repository is meant to provide quick ways to get started in reproducible data-science docker containers for:

- `python`
- `r`

## Getting started

1. Fork the repository
2. Clone the repository locally
3. Decide if you would like to use a `python` or an `r` container then follow the `README.md` instructions in the respective `<language>-playground` folder.

## Publishing new images

The images used for the 'playgrounds' are published on GitHub Container Registry (GHCR). The

## Ongoing work

1. Split python and r into own docker images, because putting them into one becomes way too large
   1. Starting with `python` - reducing image size by only having minimal packages to start with

## Backlog

- Find a way to build images that are smaller
  - Tried putting images onto GHCR then pulling from there, but they were still 2.01 GB (python) and very slow to pull (10 minutes). Plus, I believe there is a cost for hosting images.
