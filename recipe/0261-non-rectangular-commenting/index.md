---
title: Annotation with a Non-Rectangular Polygon
id: 261
layout: recipe
tags: [images, commenting, annotation]
summary: "For a IIIF resource, you would like to add a simple annotation to the resource, where the area of the resource you would like to highlight is not a rectangle."
---

## Use Case

For a IIIF resource, you would like to add a simple annotation to the resource, where the area of the resource you would like to highlight is not a rectangle. The shape of the focus area needs to be delineated with precision to highlight only the portion of the image that is relevant to the annotation.

## Implementation Notes

The [prezi3][IIIF Presentation 3.0 API] does not itself discuss non-rectangular annotations, incorporating them from the [W3C Web Annotation Data Model](http://w3.org/TR/annotation-model/) by reference. For a full description of this and other web annotations used in IIIF annotations, we recommend you read that document.

The W3C data model requires non-rectangular polygonal annotations to be described in the Scalable Vector Graphic (SVG) markup format. Note that client parsing of SVG varies, and valid SVG may not display as you expect.

When reviewing your SVG data, remove all styling and transformation features, per [the W3C data model](https://www.w3.org/TR/annotation-model/#svg-selector). To ensure your SVG markup is valid, you can use the [W3C validator](https://validator.w3.org/). SVG can be valid markup as absolute points in a coordinate space or as relative points along a path. 

Sizing and placement of the SVG polygon in relation to its `target` takes some special attention. It's best here to refer to the [IIIF Presentation 2.1 API](https://iiif.io/api/presentation/2.1/#non-rectangular-segments), noting that references to particular manifest properties may have changed with 3.0.

## Restrictions

This approach should not be used to describe non-rotated rectangular regions.

## Example

In this Manifest, we are highlighting a fountain with a statue on top of it in Göttingen, and imagining that we want to be fairly precise in our highlight. The client should not show the bounding box on the image.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Simple Annotation - Tagging][0021]

{% include acronyms.md %}
{% include links.md %}
