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

 can permit non-human interfaces consuming your manifests to present representations of your content for rapid comprehension by human readers. For instance, this could be in a cross-institutional catalog website.

Thumbnails are strongly recommended for Collections and Manifests, and permitted on Canvases, content resources, and other resource types. Conforming clients are not required to render any thumbnails, though they are strongly recommended to do so when they exist for Collections, Manifests, Canvases, and content resources. Clients are permitted to render thumbnails when they exist for all other resource types. Each resource may contain multiple thumbnails, each of which may be — but are not required to be — of the same `type` and `format` as its containing resource.

Multiple methods exist for describing a thumbnail in your manifest. For a Manifest, it makes most sense to use a full-size image URI in conjunction with a IIIF Image Service containing the whole IIIF Image service JSON. Clients consuming a Manifest thumbnail will have unpredictable size requirements; reproducing the complete service JSON gives them the most flexibility and best shot at quickly and efficiently displaying your object's thumbnail.

## Restrictions

None known.

## Example

This example uses an image of the cover of the same kabuki performance program as in the recipe for [Viewing direction and its effect on navigation][0010]. This image, though, has a color bar and the Manifest contains an explicit `thumbnail` property for the Manifest. In this particular use case, to avoid having a thumbnail image with a color calibration bar, you can choose to declare a thumbnail from a completely different image. In Mirador, the sole viewer that uses it as of this writing, the Manifest thumbnail only displays when the site visitor uses "Add a resource" to change the loaded or active Manifests.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]
* [Image Thumbnail for Manifest][0117]
* [Implementation Note: Thumbnail Selection Algorithm][0012]

{% include acronyms.md %}
{% include links.md %}
