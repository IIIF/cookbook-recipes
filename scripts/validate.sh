#!/bin/bash

if [ ! -d "scripts/schema" ]; then
    git clone https://github.com/IIIF/presentation-validator.git presentation-validator
   # cd presentation-validator
   # git checkout issue-154
   # cd ..
    mv presentation-validator/schema scripts
    rm -rf presentation-validator
fi

cd scripts
python3 ./validate.py
if [ $? -eq 1 ];then
    echo "Failed to run validator script"
    exit 1
fi

cd ..
echo "Looking for incorrect jpg mime types:"
grep -R "image/jpg" recipe/*
if [ $? -eq 0 ]; then
    echo "Mime type for a jpeg files should be 'image/jpeg' not 'image/jpg' in:"
    grep -lR "image/jpg" recipe/*
    exit 1
fi