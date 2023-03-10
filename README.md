# IIIF cookbook recipes repository

This repository is the source location for the IIIF 3.0 recipes. The aim is to show how to model various use cases in workable IIIF presentation assets.

## Contributing

Please see the [Cookbook Process](recipe/index.md).

## Jekyll Variables and Templates

### In Jekyll .md files:

There are some includes that are helpful to ensure a consistent style between recipes. These include:

### Front matter

The front matter is part of the Jekyll content management system and can be used to configure various aspects of the page and we also use some of these properties to drive separate pages like the [viewer matrix](recipe/matrix.md). The front matter is at the start of an `index.md` and a full example is given below:

```
---
layout: recipe
tags: [audio, video]
summary: "This manifest uses the 'start' property to specify a point in an audio or video object where a client application should begin playback."
viewers:
 - id: UV
   support: partial
 - Mirador  
topic: AV
property: start
---
```

The fields are as follows:
 * `layout` must be `recipe` for all recipes. This controls the layout of the page
 * `tags` this is used in the recipe listing page and is currently uncontrolled and optional. It is shown on the [full list of recipes](https://iiif.io/api/cookbook/recipe/all/)
 * `summary` a short summary of the recipe. It is shown on the [full list of recipes](https://iiif.io/api/cookbook/recipe/all/)
 * `viewers` see further details below but this drives the Viewer Matrix
 * `topic` a controlled list of headings that are used on the viewer matrix. Allowed values are **basic, property, structure, image, AV, annotation or geo-recipes**. A recipe may have multiple topics and these would be expressed as a list for example:
```
topic: 
 - basic
 - AV
```
 * `property` Include if the recipe is about a particular [IIIF Property](https://iiif.io/api/presentation/3.0/#3-resource-properties). This optional and multiple values are separate by commas. 

**Viewer Matrix**

This is generated using the `viewer` tag in the front matter. The simplest form is if the viewer fully supports the recipe and in this case the supporting viewers can be presented as a list like the following:

```
viewers:
 - UV
 - Mirador
```

If there is only partial support then this must be expressed using a map such as:

```
viewers:
 - id: UV
   support: partial
```

Combining partial support for one viewer and full support for another can be achieved by combining the list and map as seen the full Front Matter example above. If a viewer doesn't support this recipe then it should not appear in the list. If the recipe isn't supported by any viewer it should have an empty viewers field for example:

```
viewers:
topic: annotation
```

Currently the allowable viewers are:

 * UV
 * Mirador
 * Annona
 * Clover

but we would welcome other viewers. To see the requirements for adding other viewers please go to the Viewer Matrix page.

#### Include link to Viewers
This provides a standard link to the JSON and also to viewers. A full example is as follows:

```
{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}
```

and this would produce the following line:

[JSON-LD]() | [View in Universal Viewer]() | [View in Mirador]() | [View in Tify]() | [View in IIIF Curation Viewer]()

The `manifest` parameter allows you to pass a relative link to the manifest and the `viewers` parameter is a list of Viewer links to show. For the Viewers property you have the following options:

 * Include a comma seperated list of viewers. You must do this if there is partial support for one viewer. e.g [Simplest Manifest - Video](recipe/0002-mvm-audio/index.md) and [Metadata on any Resource](recipe/0002-mvm-audio/index.md) (Partial support example)
 * Leave the viewers property empty if no viewer supports this functionality. e.g. `viewers=""` e.g. [Load a Preview Image Before the Main Content](recipe/0013-placeholderCanvas/index.md)
 * Or if you want to take the list of supported viewers from the header `viewers` property remove this property. e.g. [Simplest Manifest - Single Image File](recipe/0001-mvm-image/index.md)

#### Include JSON Viewer
This will embed a JavaScript JSON viewer which will show line numbers and format the JSON. A basic example is as follows:

```
{% include jsonviewer.html src="manifest.json" %}
```

Where `src` is the relative path to the JSON file. It is also possible to add a `config` parameter if you would like to customise the view further. An example of this is to highlight the first 5 lines: 

```
{% include jsonviewer.html src="manifest.json" config='data-line="1-4"' %}
```

See the [prism.js](https://prismjs.com/#plugins) website for a full list of configuration options. 

### In JSON files:

To make the process of making the manifests resolvable during all stages of the deployment (local, test and preview deployment) there are a number of Jekyll variables available for use in JSON files. These include:

 * `id.url` - the current resolvable URL for this resource e.g. https://preview.iiif.io/cookbook/master/recipe/0001-mvm-image/manifest.json
 * `id.path` - the URL to the current directory of the file e.g. https://preview.iiif.io/cookbook/master/recipe/0001-mvm-image/. This can be useful for linking to annotation or collection JSON in the current directory. 

For an example of these variables in practice please see:

https://github.com/IIIF/cookbook-recipes/blob/master/recipe/0001-mvm-image/manifest.json

## Fixtures

There are a number of fixtures held centrally to help assist you in creating a recipe. This includes Audio and Video files and also a IIIF Image server. To see details of these fixtures please go to:

https://fixtures.iiif.io/

## Live site

The cookbook site is available at:

https://iiif.io/api/cookbook/

## To build locally:

```bundle install```

```bundle exec jekyll serve```

Then connect to [http://localhost:4000/](http://localhost:4000/)

## Preview links

This repository can be viewed using the following pattern:

```https://preview.iiif.io/cookbook/<branch_name>/```

for all branches but master. For example to see the themed version:

[https://preview.iiif.io/cookbook/themed/](https://preview.iiif.io/cookbook/themed/)

