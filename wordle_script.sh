#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]; 
then
    echo "Python 3 is not installed. Please install Python 3 to play Wordle."
    echo "You can download Python 3 from the official website:"
    echo "https://www.python.org/downloads/"
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/main.py
deactivate