#!/bin/bash

# Run this script after first building the dev container:
# bash .devcontainer/install-extensions.sh
extensions=(
    "ms-python.python@2023.10.1"
    "ms-python.vscode-pylance@2023.6.21"
    "ms-toolsai.jupyter@2023.5.1001582324"
    "VisualStudioExptTeam.vscodeintellicode@1.2.30"
    "VisualStudioExptTeam.intellicode-api-usage-examples@0.2.7"
    "ms-python.black-formatter@2023.2.0"
    "ms-python.isort@2022.8.0"
    "ms-python.pylint@2023.4.0"
    "njpwerner.autodocstring@0.6.1"
)

for extension in "${extensions[@]}"; do
  code --install-extension "$extension"
done
