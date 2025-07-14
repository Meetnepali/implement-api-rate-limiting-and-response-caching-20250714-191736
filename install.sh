#!/bin/bash
set -e

# Install system dependencies
sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv

# Setup virtual environment if not already
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt