---
title: Image Thumbnails on Canvases
id: 232
layout: recipe
tags: [image, presentation]
summary: "Display a thumbnail image for a Canvas resource, such that it can be used by clients to represent the object."
---

## Use Case

As a publisher of a Manifest, you can declare thumbnail images on each Canvas in order to optimize thumbnail generation and display by viewing clients, such as Mirador and Universal Viewer. In this recipe, we outline several different approaches and discuss their benefits, drawbacks, and requirements. For a more general introduction to thumbnails, see the [Image Thumbnail for Manifest][0117] recipe.

## Implementation Notes

## Restrictions

## Example

{% include manifest_links.html viewers="Mirador, UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]
* [Image Thumbnail for Manifest][0117]
* [Implementation Note: Thumbnail Selection Algorithm][0012]

{% include acronyms.md %}
{% include links.md %}
