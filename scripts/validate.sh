#!/bin/bash

if [ ! -d "scripts/schema" ]; then
    git clone https://github.com/IIIF/presentation-validator.git presentation-validator
    mv presentation-validator/schema scripts
    rm -rf presentation-validator
fi

cd scripts
python3 ./validate.py
if [ $? -eq 1 ];then
    echo "Failed to run validator script"
    exit 1
fi
