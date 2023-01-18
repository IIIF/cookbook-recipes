---
title: Image in annotation
id: 377
layout: recipe
tags: [annotation]
summary: "Provides an image in an annotation"
viewers:
  - Mirador
  - Annona
topic: 
 - basic
---

## Use Case

Provides an image which add details or show a different view about a particular feature/area in the main content.

## Implementation Notes

Our supplementary image is not part of the Canvas content, thus it must not have the motivation `painting`, and so is to be placed in the `annotations` section of the manifest. Following the [W3C Web Annotation model](https://www.w3.org/TR/annotation-model/#external-web-resources), we have a simple image body referencing our image, and a text body to provides a comment/title about the image.

## Restrictions

**Unknown - Help Needed**

## Example

The main content is a photo of a square in Göttingen, which shows, among others things, a fountain. We wanted to show the lights on the foutain during the night, so we associated the part of the canvas containing the foutain with an Annotation consisting of a picture of the foutain at night and a text comment.

> Mirador can open this manifest, show the text body and the selected area of the annotation, but is not capable to show the associated image  
> {% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}

> Annona successfully open the manifest and show the image annotation, but only if the image body of the annotation use an `@id` field instead of `id` (which is part of an older specification, and if [IIIF Presentation asks for retrocompatibility](https://iiif.io/api/presentation/3.0/#48-keyword-mappings) for new clients, W3C Web Annotation doesn't specify anything)  
> It also search for `caption` and `attribution` properties in the image body of the annotation; properties which are not reproduced here because there were not found in the W3C Web Annotation data model  
> 
> *The following links will open a slighty different manifest from the one presented below*
> {% include manifest_links.html viewers="Annona" manifest="manifest_at_id.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='49-66'" %}

Fixtures used in this manifest:
- [main content](https://fixtures.iiif.io/info.html?file=/images/Glen/photos/gottingen.jpg)
- [image in annotation](https://fixtures.iiif.io/info.html?file=/images/Glen/photos/fountain.jpg)

## Related Recipes

* [Simplest Annotation][0266]
* [Annotate specific images or layers][0326]
  * in our case, we had only one image so we annotated the main canvas
* [Annotation with a Non-Rectangular Polygon][0261]
  * we could have drawn the contours of the foutain
* !! [Tagging with an External Resource][0258]

{% include acronyms.md %}
{% include links.md %}

