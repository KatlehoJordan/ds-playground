# Detect cores to use for parallel installations
cores_to_use <- max(parallel::detectCores() - 2, 1)

# Enables installation of specific versions of other packages
install.packages("remotes", Ncpus = cores_to_use)

# Create a dictionary-like list of packages and version numbers to install
packages <- c(
    # "covr" = "3.6.1",
    "testthat" = "3.1.6",
    # "DT" = "0.27"
)

# Install your packages
for (pkg in names(packages)) {
    remotes::install_version(pkg, packages[pkg], Ncpus = cores_to_use)
}
