# Wi-Fi Scanner & Connector (Arch Linux)

A simple Python script that lists all available Wi-Fi networks around you on **Arch Linux** (or any Linux with NetworkManager), lets you choose one, enter the password, and attempts to connect.

## Features
- Lists all visible Wi-Fi networks with signal strength.
- Lets you choose a network by number.
- Prompts for a password and tries to connect.
- Works entirely from the terminal.

## Requirements
- **Python 3** installed
- **NetworkManager** installed and running
- `nmcli` command available (comes with NetworkManager)

## Installation
1. Install NetworkManager (if not already installed):
    ```bash
    sudo pacman -S networkmanager
    ```
2. Enable and start NetworkManager:
    ```bash
    sudo systemctl enable --now NetworkManager
    ```
3. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

## Usage
Run the script with:
```bash
python wifi_connect.py
