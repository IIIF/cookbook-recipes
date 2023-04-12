---
title: Annotation with a Non-Rectangular Polygon
id: 261
layout: recipe
tags: [images, commenting, annotation]
summary: "For a IIIF resource, you would like to add a simple annotation to the resource, where the area of the resource you would like to highlight is not a rectangle."
viewers:
 - Mirador
 - Annona
topic: annotation
---

## Use Case

For a IIIF resource, you would like to add a simple annotation to the resource, where the area of the resource you would like to highlight is not a rectangle. The shape of the focus area needs to be delineated with precision to highlight only the portion of the image that is relevant to the annotation.

## Implementation Notes

The [IIIF Presentation 3.0 API][prezi3] does not itself discuss non-rectangular annotations, incorporating them from the [W3C Web Annotation Data Model](http://w3.org/TR/annotation-model/) by reference. For a full description of this and other web annotations used in IIIF annotations, we recommend you read that document.

The W3C data model requires non-rectangular polygonal annotations to be described in the Scalable Vector Graphic (SVG) markup format. Note that client parsing of SVG varies, and valid SVG may not display as you expect. SVGs have the potential to be highly complex, incorporating multiple `path` elements and/or `mask` elements; this example is highly simplified for the purpose of demonstrating an entry point into IIIF affordances.

When reviewing your SVG data, remove all styling and transformation features, per [the W3C data model](https://www.w3.org/TR/annotation-model/#svg-selector). To ensure your SVG markup is valid, you can use the [W3C validator](https://validator.w3.org/). SVG can be valid markup as absolute points in a coordinate space or as relative points along a path. 

Sizing and placement of the SVG polygon in relation to its `target` takes some special attention. If the `target` is the entire Canvas, then the SVG viewport is assumed to cover the entire Canvas. On the other hand, if the SVG's coordinates are mapped to a part of a Canvas, then its `target` must be the rectangular bounding box of the Canvas in which the SVG viewport should be placed. If the dimensions of the viewport and its target region (either the bounding box or the entire Canvas) are not the same, then the SVG must be scaled such that it covers the region. This may result in different scaling ratios for the X and Y dimensions.

### Additional Notes on SVG

Community feedback on the original version of this recipe led to conversations and thence to the decision to expand its discussion of SVG. If you have comments on this or any recipe, speak up in the `#cookbook` channel on the [IIIF Slack workspace](https://iiif.slack.com/).

SVG implementations and affordances occupy a large and complex space. Not all implementations have the same affordances, and not all affordances are present in all implementations. To take just one paired example of SVG creation software in MacOS, SVG paths exported from GIMP 2.10 will set an origin at the upper left corner of a bounding box while one generated in Acorn 7 will set an origin in the lower left corner. Conventional browser support is equally complex: All major browsers natively [provide basic support](https://caniuse.com/svg), though tiles don't scale properly in MS Edge and important details such as `img` vs `object` container support are not considered "basic", at least by this common matrix.

In view of this complexity, and acknowledging that requiring viewers to implement the full SVG specification on a Canvas is impractical, this recipe suggests the following guidelines. As a baseline, viewers should accomodate IIIF annotations in SVG that use the following features:
+ basic shapes [or does `path` cover all of these]
	+ `rect`
	+ `circle`
	+ `ellipse`
	+ `line`
	+ `polyline`
	+ `polygon`
+ `clipPath`, including path references to one or more
+ `viewBox`
+ `path`s with any valid coordinate labeling and textual formatting
+ multiple `path`s in an `svg` element

For maximum compatibility with viewers, manifest creators should ensure that any non-rectangular annotations are limited to the above list as well. Going beyond this list, or keeping to the SVG features contained therein but adding interaction or multiplicity of them, risks your non-rectangular annotations not appearing in a viewer. In the case of SVG non-rectangular annotations, it may not be feasible for viewers may to display only the supported features and discard the rest, as they can do for manifests more generally.

Viewer accommodation SVG creation tools' coordinate arrangement output is a thornier matter. 

## Restrictions

This approach should not be used to describe non-rotated rectangular regions.

## Example

In this Manifest, we are highlighting a fountain with a statue on top of it in Göttingen, and imagining that we want to be fairly precise in our highlight. The client should not show the bounding box on the image.

{% include manifest_links.html viewers="Mirador,Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Simple Annotation - Tagging][0021]

{% include acronyms.md %}
{% include links.md %}

