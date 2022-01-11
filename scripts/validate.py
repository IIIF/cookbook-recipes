#!/usr/bin/env python3 

import os 
import json
import sys

import urllib.request, json 
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError, SchemaError
from schema import schemavalidator
import frontmatter
import yaml

ignore = ['scripts']
def findFilesToValidate(dirname, extension):
    validation_files = []
    for root,d_names,files in os.walk(dirname):
        for filename in files:
            if filename.endswith(extension) and not 'scripts' in root:
                validation_files.append(os.path.join(root, filename))
    

    return validation_files

def printPath(pathObj, fields):
    path = ''
    for item in pathObj:
        if isinstance(item, int):
            path += u'[{}]'.format(item)
        else:
            path += u'/'    
            path += item

    path += '/[{}]'.format(fields)
    return path    


def validateIIIF(jsonData, filepath):
    result = schemavalidator.validate(json.dumps(jsonData), '3.0', filepath)
    if result['okay'] != 1:
        print ('*************************')
        print ('Failed validation: {}'.format(filepath))
        # Failed validation
        for error in result['errorList']:
            print ('# {}'.format(error['title']))
            print ('Detail: {}'.format(error['detail']))
            print ('Path: {}'.format(error['path']))
            print ('Description: {}'.format(error['description']))
            print ('context:')
            print (json.dumps(error['context'], indent=4))

        print ('*************************')
        return False
    else:    
        return True

def loadYAML(location):
    with open(location, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == "__main__":
    allPassed = True
    files = findFilesToValidate("../recipe", ".md");
    ignore = ["../recipe/index.md", "../recipe/matrix.md", "../recipe/all.md"]
    
    topics = loadYAML("../_data/topics.yml")
    ignoreFromViewerMatrix = loadYAML("../_data/viewer_ignore.yml")
    for recipepath in files:
        if recipepath not in ignore:
            recipe = frontmatter.load(recipepath)
            if not 'topic' in recipe:
                print ('Missing topic in {}'.format(recipepath))
                allPassed = False
            else:
                if isinstance(recipe['topic'], list): 
                    for topic in recipe['topic']:
                        if topic not in topics:
                            print ('Topic {} in recipe {} not in list of topics in _data/topics.yml ({})'.format(recipe['topic'], recipepath, ",".join(topics.keys())))
                            allPassed = False
                else: 
                    if recipe['topic'] not in topics:
                        print ('Topic {} in recipe {} not in list of topics in _data/topics.yml ({})'.format(recipe['topic'], recipepath, ",".join(topics.keys())))
                        allPassed = False

            if 'viewers' not in recipe:
                ignoreViewer = False
                for ignorePath in ignoreFromViewerMatrix:
                    if ignorePath in recipepath:
                        ignoreViewer = True
                        break
                if not ignoreViewer:
                    print ('Recipe {} is missing a `viewers` entry either add it or add the name of the recipe to _data.viewer_ignore.yml'.format(recipepath))
                    allPassed = False
                    
                


    files = findFilesToValidate("../_site", ".json")
    # Get JSON Schema
    for jsonFilename in files:
        errorJsonFilename = jsonFilename.replace('../_site/','')
        with open(jsonFilename) as json_file:
            try:
                jsonData = json.load(json_file)
            except ValueError as err:
                print ('{}: Failed to load JSON due to: {}'.format(errorJsonFilename, err))
                continue

            if 'type' in jsonData:
                if jsonData['type'] in ['Manifest', 'Collection']:
                    passed = validateIIIF(jsonData, jsonFilename)
                    if not passed:
                        allPassed = False
                    # else it passed    
                else:
                    print ('{}: Do not know how to validate JSON with type: {}'.format(errorJsonFilename, jsonData['type']))
            else:
                print ('{}: No type found in JSON so not validating'.format(errorJsonFilename))
    if allPassed:
        sys.exit(0)
    else:
        print ('Failing build due to validation error')
        sys.exit(1)
