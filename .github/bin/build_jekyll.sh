#!/bin/bash 

bundle config path vendor/bundle
if [ $? -eq 1 ];then
    echo "Failed adding config path"
    exit 1
fi

bundle install
if [ $? -eq 1 ];then
    echo "Failed bundle install"
    exit 1
fi

echo "Running config: $CONFIG"
bundle exec jekyll build  --baseurl $BASE_URL $CONFIG
if [ $? -eq 1 ];then
    echo "Failed jekyll build"
    exit 1
fi

