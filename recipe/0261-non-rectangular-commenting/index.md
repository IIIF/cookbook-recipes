---
title: Non-Rectangular Comment Polygon
id: 261
layout: recipe
tags: [images, commenting, annotation]
summary: "tbc"
---

## Use Case

For a IIIF resource, you'd like to add a simple annotation to the resource, where the area of the resource you'd like to highlight is not a rectangle. The shape of the focus area needs to be delineated with precision to highlight only the portion of the image that is relevant to the annotation.

## Implementation Notes

The [prezi3][IIIF Presentation 3.0 API] does not itself discuss non-rectangular annotations, incorporating them from the [W3 Web Annotation Data Model](http://w3.org/TR/annotation-model/) by reference. For a full description of this and other web annotations used in IIIF annotations, we recommend you read that document.

The W3 data model requires non-rectangular polygonal annotations to be described as Scalable Vector Graphic (SVG) markup. This recipe is not the place to discuss how to create this markup, but we can note that many software tools exist that can handle it. Among others, third-party graphics editors may have this capability, as well as a Mirador instance properly configured.

When reviewing your SVG data, remove all styling and transformation features, per [the W3 data model](https://www.w3.org/TR/annotation-model/#svg-selector). To ensure your SVG is valid markup, you can use the [W3 validator](https://validator.w3.org/).

Sizing and placement of the SVG polygon in relation to its `target` takes some special attention. It's best here to quote from the IIIF Presentatin 2 API:
<blockquote>
If the section of an image is mapped to part of a canvas, as in the example below, then the target in on must be the rectangular bounding box in which the SVG viewport should be placed. If the entire canvas is the target, then the SVG viewport is assumed to cover the entire canvas. If the dimensions of the viewport and the bounding box or canvas are not the same, then the SVG must be scaled such that it covers the region. This may result in different scaling ratios for the X and Y dimensions.
</blockquote>

## Restrictions

This approach should not be used to describe non-rotated rectangular regions.

## Example

In this manifest, we are highlighting the statue on the top of a fountain in Göttingen, and imagining that we want to be fairly precise in our highlight. Because we want to put the polygon in a particular place on the Canvas, we need to use the fragment selector syntax to describe its bounding box. The bounding box should not show up on the image in any way.

No current viewers support this form of annotation for IIIF Presentation v3.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

