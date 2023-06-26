# Get the list of available CRAN mirrors
cran_mirrors <- getCRANmirrors()

# Select the mirror you want to use (e.g., the first mirror in the list)
selected_mirror <- cran_mirrors[1, "URL"]

# Set the selected mirror as the default
options(repos = selected_mirror)

# Enables installation of specific versions of other packages
install.packages("renv")

packages <- c(
    # Enables VS Code extension features but takes a long time to install
    "languageserver@0.3.14",
    # Enables piping and dplyr data-manipulation verbs
    "tidyr@1.2.1",
    # For plotting, shiny, and R Markdown in VS Code
    "httpgd@1.3.1",
    "ggplot2@3.4.0",
    "svglite@2.1.1",
    "plotly@4.10.1",
    "shiny@1.7.3",
    "rmarkdown@2.18",
    # For Debugger VS Code extension
    "devtools@2.4.5"
)

for (package in packages) {
    renv::install(package)
}


# Install package for debugging
devtools::install_github("ManuelHentschel/vscDebugger")
