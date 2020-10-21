---
title: Image Thumbnail for Manifest
id: 117
layout: recipe
tags: [image,presentation]
summary: "Display a thumbnail image for a resource other than a Canvas, such that it can be used by clients to represent the object."
---

## Use Case

You have images of a booklet, and you want to select one to use as the singular representation of the whole object for consuming clients. These clients range from object viewers such as Mirador or Universal Viewer to discovery services and other aggregators such as Spotlight or a homegrown solution. Absent a declared thumbnail for the Manifest, some clients will create a thumbnail from the first Canvas in the Manifest.

## Implementation Notes

Thumbnails can permit non-human interfaces consuming your manifests to present representations of your content for rapid comprehension by human readers. For instance, this could be in a cross-institutional catalog website.

Thumbnails are strongly recommended for Collections and Manifests, and permitted on Canvases, content resources, and other resource types. Conforming clients are not required to render any thumbnails, though they are strongly recommended to do so when they exist for Collections, Manifests, Canvases, and content resources. Clients are permitted to render thumbnails when they exist for all other resource types. Each resource may contain multiple thumbnails, each of which may be — but are not required to be — of the same `type` and `format` as its containing resource. 

Multiple methods exist for describing a thumbnail in your manifest. For a Manifest, it makes most sense to use a full-size image URI in conjunction with a IIIF Image Service containing the whole IIIF Image service JSON. Clients consuming a Manifest thumbnail will have unpredictable size requirements; reproducing the complete service JSON gives them the most flexibility and best shot at quickly and efficiently displaying your object's thumbnail.

## Restrictions

None known.

## Example

This example uses an image of the cover of the same kabuki performance program as in the recipe for [Viewing direction and its effect on navigation][0010]. This image, though, has a color bar and the Manifest contains an explicit `thumbnail` property for the Manifest. In this particular use case, because the image contains a color calibration bar, you can choose to declare a thumbnail image that doesn't have the calibration bar.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]
* [Implementation Note — Thumbnail Selection Algorithm][0012]

{% include acronyms.md %}
{% include links.md %}

