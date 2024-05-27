#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_font_file>"
    exit 1
fi

python3 src/main.py "$1"
