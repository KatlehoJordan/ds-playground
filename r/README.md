<!-- markdownlint-disable MD029 -->

# `r` playground for data science

This container is meant to be used for rapid development of data science projects using `r`.

## Getting started

1. Open a new VS Code workspace in `r-playground`
2. Use VS Code Dev containers to build a base container
3. Open `main.r` to start getting an introduction to the functionality.

## Using alias `r-playground`

This alias should open a VS Code session in the correct location. Then use VS Code to restart the Dev Container.

```sh
r-playground
```

### Running `radian` from within the container

Ensure that Docker desktop is running. Then:

```sh
docker run --rm -i --name r-playground r-playground
```

This will build a container based on the cached docker image `r-playground` and then remove the container after it finishes.

Alternatively, if you have the alias in your shell profile:

```sh
r
```

## Next steps

- Include tidymodels tutorial
- Find way to install r dependencies in parallel, and to automatically install system-wide dependencies
  - Attempts to use renv with pak failed since pak installations failed over and over again
- Provide example using r unit testing
- Provide instructions for setting up r package
- Ensure all linting is working
