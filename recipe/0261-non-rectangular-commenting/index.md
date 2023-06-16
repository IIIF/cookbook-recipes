---
title: Annotation with a Non-Rectangular Polygon (Updated)
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

The W3C data model requires non-rectangular annotations to be described in the Scalable Vector Graphic (SVG) markup format and to use the `SvgSelector`. Note that viewer parsing of SVG varies, and valid SVG may not display as you expect. SVGs have the potential to be highly complex; this example is highly simplified for the purpose of demonstrating an entry point into IIIF affordances.

When reviewing your SVG data, remove all styling and transformation features, per [the W3C data model](https://www.w3.org/TR/annotation-model/#svg-selector). To ensure your SVG markup is valid, you can use the [W3C validator](https://validator.w3.org/). SVG can be valid markup as absolute points in a coordinate space or as relative points along a path. 

Sizing and placement of the SVG polygon in relation to its `target` takes some special attention. If the `target` is the entire Canvas, then the SVG viewport is assumed to cover the entire Canvas. On the other hand, if the SVG's coordinates are mapped to a part of a Canvas, then its `target` must be the rectangular bounding box of the Canvas in which the SVG viewport should be placed. If the dimensions of the viewport and its target region (either the bounding box or the entire Canvas) are not the same, then the SVG must be scaled such that it covers the region. This may result in different scaling ratios for the X and Y dimensions.

### Additional Notes on SVG

Community feedback on the original version of this recipe led to conversations and thence to the decision to expand its discussion of SVG. If you have comments on this or any recipe, speak up in the `#cookbook` channel on the [IIIF Slack workspace](https://iiif.slack.com/).

SVG implementations and affordances occupy a large and complex space. Not all implementations have the same affordances, and not all affordances are present in all implementations. To take just one facet of SVG creation software, the output from one such tool may set an origin point at the upper left corner of a bounding box while another may set an origin in the lower left corner. Conventional browser support is equally complex: All major browsers natively [provide basic support](https://caniuse.com/svg), though tiles don't scale properly in MS Edge and important details such as `img` vs `object` container support are not considered "basic", at least by this common matrix.

#### For Viewers
Browser-based IIIF viewers often hand off SVG rendering to the containing browser, but it might be helpful to non-browser–based viewers to detail recommended SVG feature support. In view of the complexity described above, and acknowledging that expecting viewers to implement the full SVG specification on a Canvas is impractical as well as contrary to the W3C Web Annotation specification, this recipe suggests that viewers handling SVG rendering themselves support at least the following features:
+ named shapes
	+ `circle`
	+ `ellipse`
	+ `line`
	+ `polyline`
	+ `polygon`
+ `viewBox`
+ `g` 
+ `path`, including multiple `path`s inside a `g`

Viewers may occasionally encounter manifests in which there is a conflict between the dimensions values for a resource or IIIF property and the dimensions given within the SVG markup of an `SvgSelector` property. To anticipate these cases, it is suggested that viewers privilege the dimensional information contained in IIIF properties other than `SvgSelector` over the SVG dimensions where these conflict. 

#### For Manifest Creators
Manifest creators should ensure, for maximum compatibility with viewers, that any non-rectangular annotations are limited to the above list as well. Going beyond this list, or keeping to the SVG features contained therein but adding interaction or multiplicity of them, risks your non-rectangular annotations not appearing in a viewer. In the case of SVG non-rectangular annotations, it may not be feasible for viewers to display only the supported features and discard the rest, as they can do for manifests more generally.

## Restrictions

This approach should not be used to describe non-rotated rectangular regions.

## Example

In this Manifest, we are highlighting a fountain with a statue on top of it and imagining that we want to be fairly precise in our highlight. The client should not show the bounding box on the image.

{% include manifest_links.html viewers="Mirador,Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Simple Annotation - Tagging][0021]

{% include acronyms.md %}
{% include links.md %}

