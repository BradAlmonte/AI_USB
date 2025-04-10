#!/bin/bash

# Detect OS
OS=$(uname -s)

if [[ "$OS" == "Darwin" || "$OS" == "Linux" ]]; then
    echo "Running on macOS/Linux..."

    # Install dependencies for macOS/Linux (using Homebrew)
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found. Please install Homebrew first."
        exit 1
    fi

    echo "Installing Cybersecurity Tools..."

#!/bin/bash

# Detect OS
OS=$(uname -s)

if [[ "$OS" == "Darwin" || "$OS" == "Linux" ]]; then
    echo "Running on macOS/Linux..."

    # Install Homebrew if not found
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found, installing..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi

    echo "Installing Cybersecurity Tools..."

    # Install tools with Homebrew
    brew install nmap wireshark burpsuite john sqlmap aircrack-ng hashcat metasploit nikto curl wget
    echo "✅ All tools downloaded successfully!"
