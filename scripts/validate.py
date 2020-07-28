#!/usr/bin/env python3 

import os 
import json
import sys

import urllib.request, json 
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError, SchemaError
from schema import schemavalidator

ignore = ['scripts']
def findFilesToValidate(dirname):
    validation_files = []
    for root,d_names,files in os.walk(dirname):
        for filename in files:
            if filename.endswith('json') and not 'scripts' in root:
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


def validate(jsonData, filepath):
    print ('*************************')
    print ('Testing: {}'.format(filepath))
    result = schemavalidator.validate(json.dumps(jsonData), '3.0', filepath)
    if result['okay'] != 1:
        # Failed validation
        for error in result['errorList']:
            print ('# {}'.format(error['title']))
            print ('Detail: {}'.format(error['detail']))
            print ('Path: {}'.format(error['path']))
            print ('Description: {}'.format(error['description']))
            print ('context:')
            print (json.dumps(error['context'], indent=4))

    print ('*************************')
    return result['okay'] == 1

if __name__ == "__main__":
    files = findFilesToValidate("../_site")
    # Get JSON Schema
    allPassed = True
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
                    passed = validate(jsonData, jsonFilename)
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
