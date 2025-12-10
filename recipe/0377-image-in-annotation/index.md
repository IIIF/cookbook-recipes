---
title: Image in Annotations
id: 377
layout: recipe
tags: [annotation]
summary: "Provides an image in an annotation"
viewers:
  - Annona
  - Glycerine Viewer
  - Theseus
  - TIFY
topic:
 - basic
---

## Use Case

Provide an image that adds details about or shows a different view of a particular feature/area of the Resource.

- You have a group picture of many people. The image quality doesn't allow you to recognize all of them, so you annotate each face with the name of the person and an individual photo of that person.
- You have a picture of an architect's plan for a building which has been built. To show how the completed building looks, you decide to annotate specific features, such as the patio, with actual photographs.
- You have a Manifest with a video showing an old building at the time of its creation. In some instances, where the video shows a specific part of the building, you might want to annotate the video with a photo of how this part looks now. Annotations may be just one image or contain a description like, "This wall faces north, you can see there is more moss there."

## Implementation Notes

Our supplementary image is not part of the Canvas content, thus it must not have the motivation `painting` and is placed in the `annotations` section of the Canvas. Following the [W3C Web Annotation model](https://www.w3.org/TR/annotation-model/#external-web-resources), we have two separate objects that make up the Annotation body. One object is an image which is the supplementary image and the other is a textual body which acts as a caption for the supplementary image. Both of these objects together target the Resource.

## Example

The main content is a photo of a square in Göttingen, which shows, among others things, a fountain. We wanted to show the lights on the fountain during the night, so we associated the part of the Canvas containing the fountain with an Annotation consisting of a picture of the fountain at night and a text comment.

{% include manifest_links.html viewers="Annona, Glycerine Viewer, Theseus, TIFY" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='49-66'" %}

## Related Recipes

* [Simplest Annotation][0266]
* [Annotate specific images or layers][0326] to annotate only one of the images
* [Annotation with a Non-Rectangular Polygon][0261] to precisely draw the contours of the fountain
* [Tagging with an External Resource][0258]

{% include acronyms.md %}
{% include links.md %}
