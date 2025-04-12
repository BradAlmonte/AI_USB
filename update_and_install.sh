#!/bin/bash

# Pull the latest changes from the repository
git pull https://github.com/BradAlmonte/AI_USB.git main

# Detect OS
OS=$(uname -s)

if [[ "$OS" == "Darwin" || "$OS" == "Linux" ]]; then
    echo "Running on macOS/Linux..."
    ./install-tools.sh
elif [[ "$OS" == "Windows" ]]; then
    echo "Running on Windows..."
    powershell.exe -ExecutionPolicy Bypass -File ./install-tools.ps1
else
    echo "Unsupported OS"
fi

