#!/bin/bash

echo "🔧 Setting up AI Research Agent 2.0 environment..."

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Download NLTK data for newspaper3k
python3 -m nltk.downloader punkt

echo "✅ Setup complete! Activate your environment using:"
echo "source venv/bin/activate"
echo "Then run: python main.py"
