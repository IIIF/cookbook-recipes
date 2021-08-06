---
title: Non-Rectangular Comment Polygon
id: 261
layout: recipe
tags: [images, commenting, annotation]
summary: "tbc"
---

## Use Case

For a IIIF resource, you'd like to add a simple annotation to the resource, where the area of the resource you'd like to highlight is not a rectangle.

## Implementation Notes

The IIIF Presentation 3.0 API does not itself discuss non-rectangular annotations, incorporating them from the W3C Web Annotation Data Model by reference. For a full description of this and other web annotations used in IIIF annotations, we recommend you read that document.

IIIF requires non-rectangular polygonal annotations to be described as Scalable Vector Graphic (SVG) markup. This recipe is not the place to discuss how to create this markup, but we can note that many software tools exist that can handle it. Among others, third-party graphics editors may have this capability, as well as a Mirador instance properly configured.



+ Need fragment to show where the SVG will go

/My questions for authors/

SVG validation?
	But also IIIF asks for a subset of SVG
	https://validator.w3.org/#validate_by_input+with_options (but needs a schema)

Anything other than SVG?
	No

Viewer?
	Annotation version of mirador
	
	Try to make it work with 
	
	
Link to spec where the SVG elements are delimited


## Restrictions

None known.

## Example

In this manifest, we are highlighting the statue on the top of a fountain in Göttingen, and imagining that we want to be fairly precise in our highlight. We need to use the fragment selector syntax to describe a rectangle for the annotation's placement, but the annotation itself will not be a rectangle. The placement fragment should not show up on the image in any way.

No current viewers support this form of annotation for IIIF Presentation v3 by default.

Shows in 


{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

