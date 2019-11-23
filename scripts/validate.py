#!/usr/bin/env python3 

import os 
import json
import sys

import urllib.request, json 
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError, SchemaError

def findFilesToValidate(dirname):
    validation_files = []
    for root,d_names,files in os.walk(dirname):
        for filename in files:
            if filename.endswith('json'):
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


def validate(schema, jsonData):
    try:
        validator = Draft7Validator(schema)
        results = validator.iter_errors(jsonData)
    except SchemaError as err:    
        print('Problem with the supplied schema:\n')
        print(err)


    errors = sorted(results, key=lambda e: e.path)
    if errors:
        print('Validation Failed')
        errorCount = 1
        for err in errors:
            print('Error {} of {}.\n Message: {}'.format(errorCount, len(errors), err.message))
            if 'title' in err.schema:
                print (' Test message: {}'.format(err.schema['title']))
            if 'description' in err.schema:
                print (' Test description: {}'.format(err.schema['description']))
            print('\n Path for error: {}'.format(printPath(err.path, err.message)))
            context = err.instance
            if isinstance(context,dict): 
                for key in context:
                    if isinstance(context[key], list): 
                        context[key] = '[ ... ]'
                    elif isinstance(context[key], dict):
                        context[key] = '{ ... }'

            print (json.dumps(err.instance, indent=4))
            errorCount += 1

        return False
    else:
        return True

if __name__ == "__main__":
    files = findFilesToValidate("_site")
    # Get JSON Schema
    with urllib.request.urlopen("https://raw.githubusercontent.com/IIIF/presentation-validator/master/schema/iiif_3_0.json") as url:
        schema = json.loads(url.read().decode())
    allPassed = True
    for jsonFilename in files:
        errorJsonFilename = jsonFilename.replace('_site/','')
        with open(jsonFilename) as json_file:
            try:
                jsonData = json.load(json_file)
            except ValueError as err:
                print ('{}: Failed to load JSON due to: {}'.format(errorJsonFilename, err))
                continue

            if 'type' in jsonData:
                if jsonData['type'] in ['Manifest', 'Collection']:
                    passed = validate(schema, jsonData)
                    if not passed:
                        print ('{}: failed validation'.format(errorJsonFilename))
                        allPassed = False
                    else:    
                        print ('{}: passed validation'.format(errorJsonFilename))
                else:
                    print ('{}: Do not know how to validate JSON with type: {}'.format(errorJsonFilename, jsonData['type']))
            else:
                print ('{}: No type found in JSON so not validating'.format(errorJsonFilename))
    if allPassed:
        sys.exit(0)
    else:
        print ('Failed validation')
        sys.exit(1)
