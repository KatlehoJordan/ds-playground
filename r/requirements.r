# Use max of 1 or number of cores minus 2 while installing packages
cores_to_use <- max(1, parallel::detectCores() - 2)

# Get the list of available CRAN mirrors and use the first mirror for installs
selected_mirror <- getCRANmirrors()[1, "URL"]

options(Ncpus = cores_to_use, repos = selected_mirror)

packages <- c(
    # Enables VS Code extension features but takes a long time to install
    "languageserver",
    # Enables piping and dplyr data-manipulation verbs
    "tidyr",
    # For plottingin VS Code
    "httpgd",
    "ggplot2",
    "svglite",
    "plotly",
    # For running in jupyter notebooks
    "IRkernel"
)

install.packages(packages)

# Setup IRkernel for using r in jupyter notebooks
IRkernel::installspec()
