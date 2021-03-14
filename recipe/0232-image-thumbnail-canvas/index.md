---
title: Image Thumbnails on Canvases
id: 232
layout: recipe
tags: [image, presentation]
summary: "Display a thumbnail image for a Canvas resource, such that it can be used by clients to represent the object."
---

## Use Case

As a publisher of a Manifest, you may choose to declare thumbnail images on each Canvas in order to optimize thumbnail generation and display by viewing clients, such as Mirador and Universal Viewer. While it is not necessary to declare a thumbnail on Canvases since clients SHOULD render thumbnails from the Resource, doing so can increase the efficiency with which thumbnails load in a viewer. This is especially noticeable in Manifests that have many Canvases, such as books and manuscripts.

This recipe outlines several different approaches to declaring thumbnails and discusses the benefits, drawbacks, and requirements for each. For a more general introduction to thumbnails, see the [Image Thumbnail for Manifest][0117] recipe.

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
