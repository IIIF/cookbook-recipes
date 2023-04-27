---
title: Image in annotations
id: 377
layout: recipe
tags: [annotation]
summary: "Provides an image in an annotation"
viewers:
  - Annona
topic: 
 - basic
---

## Use Case

Provides an image which adds details or shows a different view about a particular feature/area in the main content.

- You have a group picture of many people. The image quality doesn't allow you to recognize all of them, so you annotate each face with the name of the person and an individual photo of that person.  
- You have a picture of an architect's plan for a building which has been built. You want to show, for the different diagrams in the plan, how it looks once built. So you annotate some features (for example, the patio) with an actual photo.
- You have a Manifest with a video showing an old building at the time of his creation. Sometimes when the video shows a different part of the building, you want to annotate the video with a photo of how this part looks now. Annotations may be just one image or contain a description like, "This wall faces north, you can see there is more moss there."

## Implementation Notes

Our supplementary image is not part of the Canvas content, thus it must not have the motivation `painting` and is placed in the `annotations` section of the Canvas. Following the [W3C Web Annotation model](https://www.w3.org/TR/annotation-model/#external-web-resources), we have a simple image body referencing our image, and a text body to provides a caption related to the image.

## Example

The main content is a photo of a square in Göttingen, which shows, among others things, a fountain. We wanted to show the lights on the fountain during the night, so we associated the part of the canvas containing the fountain with an Annotation consisting of a picture of the fountain at night and a text comment.

{% include manifest_links.html viewers="Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='49-66'" %}

## Related Recipes

* [Simplest Annotation][0266]
* [Annotate specific images or layers][0326]
  * in our case, we had only one image so we annotated the main canvas
* [Annotation with a Non-Rectangular Polygon][0261]
  * we could have drawn the contours of the fountain
* !! [Tagging with an External Resource][0258]

{% include acronyms.md %}
{% include links.md %}

