---
title: Addressing a Region
id: 299
layout: recipe
tags: [fragment]
summary: "Presenting a region of an image independently"
viewers:
topic: 
 - basic
---

## Use Case

You would like to display a **[visual]** section of a IIIF resource independently.

## Implementation Notes

This recipe requires you to keep in mind two distinctions between a Canvas and a IIIF resource.

For one, to display only a region of a resource on your Canvas, the Canvas dimensions should relate to the region you want to display, not to the whole resource. Note, however (as discussed in [recipe 4][0004]) that the Canvas is a dimensionless set of coordinates. If desired, the dimensions of the Canvas may be different numeric values than the region you are displaying, but must be the same proportions if you want the region displayed with an  unchanged dimension ratio.

The other significant pertinent distinction is that the process used to retrieve the desired region uses a `selector` of type ImageApiSelector because the process uses the [IIIF Image API](https://iiif.io/api/image/). When addressing a portion of a Canvas, however, an Annotation would use a `selector` of type [FragmentSelector](https://www.w3.org/TR/annotation-model/#fragment-selector) because the Annotation is using the [IIIF Presentation API](https://iiif.io/api/presentation/3.0/#53-canvas) in conformance with the [W3C Web Annotation data model](https://www.w3.org/TR/annotation-model/).

When retrieving a region of an image to display, the Annotation `body` containing the resource is constructed as a `SpecificResource` that in turn contains a `source` with the resource's details.

## Restrictions

No known restrictions

## Example

In this example we use an ImageApiSelector on the `body` of the Manifest's sole Annotation to retrieve a 1260x1239 selection from an image of Göttingen, Germany. The region contains the city's Gänsenliesel fountain with the eponymous goose girl sculpture atop it.

Note: Displaying a region of a Resource is not yet supported in viewers.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='14-15,25-46'" %}

## Related Recipes

* [Simple Image Manifest][0001]
* [Image and Canvas with Differing Dimensions][0004] for thinking through relative dimensioning of a resource and a Canvas
* [Introduction to IIIF Image Service][0005] for a basic example of image service use
* [Simple Annotation — Tagging][0021] to see the image region that should be displayed
* [Image Rotation Two Ways][0040] for another example of using a selector with a IIIF Image service

{% include acronyms.md %}
{% include links.md %}

