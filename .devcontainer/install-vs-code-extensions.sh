#!/bin/bash

# Run this script after first building the dev container:
# bash .devcontainer/install-extensions.sh
extensions=(
  "ms-python.vscode-pylance@2023.6.10"
  "ms-python.black-formatter@2023.2.0"
  "ms-toolsai.jupyter@2023.5.1001582324"
  "VisualStudioExptTeam.vscodeintellicode@1.2.30"
  "VisualStudioExptTeam.intellicode-api-usage-examples@0.2.7"  
  # This comes last because previous extensions will install a newer version
  # that has bugs
  "ms-python.python@2023.8.0"
)

for extension in "${extensions[@]}"; do
  code --install-extension "$extension"
done
