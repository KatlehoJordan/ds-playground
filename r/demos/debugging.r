# Debugging ####

# Debugging R inVS Code will require additional installations including:
# - The debian tools `libharfbuzz-dev`, `libfribidi-dev`, `libtiff5-dev`:
#     ```sh
#     sudo apt install libharfbuzz-dev -y && \
#     sudo apt install libfribidi-dev && \
#     sudo apt install libtiff5-dev -y
#     ```
# - The `r` package `devtools` (`install.packages('devtools')`)
# - The non-standard `r` package `vscDebugger`:
#     `devtools::install_github("ManuelHentschel/vscDebugger")`


## Debug R-File will pause at errors in the current file ####

# Launch debugger with F5
# Place breakpoints with F9
# Add items to the watch list to observe them at different points

function_1 <- function(i) {
    (1:10)[[i]]
}

inputs <- c(4, 5, 2, 9, 0, 8)

for (x in inputs) {
    function_1(x)
}

## Alternative R-Debugger configurations ####

# One can add more configurations to .vscode/launch.json
# for initiating the debugger in a specific file, function, package,
# or other options. However it will require more configuration.
