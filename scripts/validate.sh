#!/bin/bash

if [ ! -d "scripts/schema" ]; then
    git clone https://github.com/IIIF/presentation-validator.git presentation-validator
    mv presentation-validator/schema scripts
    rm -rf presentation-validator
fi

cd scripts
python ./validate.py
