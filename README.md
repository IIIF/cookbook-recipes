# IIIF cookbook recipes

The issues of this repository are used to identify and discuss cookbook recipes, prior to their inclusion in the cookbook section of the API repository. 

Anyone is welcome to submit a recipe idea. Sometimes the person who raises the recipe issue then goes on to write the recipe, but this doesn't have to be the case. The need for a recipe may be expressed before its form is known; the comments on the recipe issue are where the recipe is discussed and elaborated.

For further details, see the _[Process](https://preview.iiif.io/api/image-prezi-rc2/api/cookbook/#process)_ section of the API site.

Before a pull request to the API repository is opened, the recipe is developed in this cookbook-recipes repository. This allows for a greater number of committers and easier tracking of recipe development through project boards and milestones.

Each issue has a corresponding directory in this repository (the recipe issue number is the directory name). Under this directory, index.md is the home page of the issue. The recipe should be accompanied by complete JSON-LD files, with working links to content and other resources. Large binary resources such as videos can be uploaded to the shared recipe S3 bucket. Where a working Image Service is required, the _reference image server_ may be used (TBC).

These issues should only be candidate recipes. Issues about the cookbook itself (e.g., format, how it works) should be raised and discussed in the regular API repository.

## Suggested recipe checklist

This checklist can be added to the issues and new issue template:

- [ ] Use case clear
- [ ] Example(s) pass validation
- [ ] Example(s) Presentation resources and annotations are available as referenced JSON in recipe directory
- [ ] All linked resources are dereferenceable; static images may be included with recipe JSON, but video and audio are in S3 bucket
