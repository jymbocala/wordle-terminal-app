#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]; 
then
    echo "Python 3 is not installed. Please install Python 3 to play Wordle."
    # Provide a link to install Python 3
    echo "You can download Python 3 from the official website:"
    echo "https://www.python.org/downloads/"
    exit 1
fi

