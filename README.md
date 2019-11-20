# IIIF cookbook recipes repository

This repository is the source location for the IIIF 3.0 recipes. The aim is to show how to model various use cases in workable IIIF presentation assets.

## Contributing

Please see the [Cookbook Process](recipe/index.md).

## Jekyll Variables

To make the process of making the manifests resolvable during all stages of the deployment (local, test and preview deployment) there are a number of Jekyll variables available for use in JSON files. These include:

 * `id.url` - the current resolvable URL for this resource e.g. https://preview.iiif.io/cookbook/master/recipe/0001-mvm-image/manifest.json
 * `id.path` - the URL to the current directory of the file e.g. https://preview.iiif.io/cookbook/master/recipe/0001-mvm-image/. This can be useful for linking to annotation or collection JSON in the current directory. 

For an example of these in variables in practice please see:

https://github.com/IIIF/cookbook-recipes/blob/master/recipe/0001-mvm-image/manifest.json

## Fixtures

There are a number of fixtures held centrally to help assist you in creating a recipe. This includes Audio and Video files and also a IIIF Image server. To see details of these fixtures please go to:

https://fixtures.iiif.io/

## Live site

The cookbook site is available at:

https://preview.iiif.io/cookbook/master

**Note:** in the future this will be merged into the https://iiif.io website. 

## To build locally:

```bundle install```

```bundle exec jekyll serve```

Then connect to [http://localhost:4000/](http://localhost:4000/)

## Preview links

This repository can be viewed using the following pattern:

```https://preview.iiif.io/cookbook/<branch_name>/```

for all branches but master. For example see the themed version:

[https://preview.iiif.io/cookbook/themed/](https://preview.iiif.io/cookbook/themed/)

