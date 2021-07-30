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

+ Need fragment to show where the SVG will go
+ Non-rectangular polygon described by SVG
+ Need to create SVG in 3rd party program

/My questions for authors/

SVG validation?

Anything other than SVG?

Viewer?


## Restrictions

None known.

## Example

In this manifest, we are highlighting the statue on the top of a fountain in Göttingen, and imagining that we want to be fairly precise in our highlight. We need to use the fragment selector syntax to describe a rectangle for the annotation's placement, but the annotation itself will not be a rectangle. The placement fragment should not show up on the image in any way.

No current viewers support this form of annotation for IIIF Presentation v3 by default.

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

