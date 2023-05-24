---
title: Annotating a specific point of an image.
id: 15
layout: recipe
tags: image
summary: "This recipe explains how to annotate a specific point of an image."
viewers:
topic:
 - Annotations
 - property
property: PointSelector
---

## Use Case
I want to annotate a coordinate of the image rather than a region. I have a map with some locations that can be represented better by a single coordinate. I want to add some auxiliary data relative to a specific point of the image (e.g. some spectroscopic analysis made on a manuscript).

## Implementation notes

This recipe, as [Simple Annotation — Tagging][0021] implements a method for annotating an image. Recipe [Begin playback at a specific point - Time-based media][0015] uses a Point Selector for selecting a specific time of a video, this recipe selects instead a specific point of the image.

In this use case, the Annotation is inside an Annotation Page in the `annotations` list of the Manifest. The `motivation` of the Annotation is "tagging" and the target `source` points to the Canvas `id`. The `type` property is a Specific Resource while the Selector `type` property is a Point Selector that contains the coordinates `x` and `y` of the Canvas coordinates system as parameters.

Viewer might consider implementing scale-independent point markers so that they are visible at every level of zoom.

## Example

This example uses a leaflet with a map and a guide supplied by the Library of Congress Geography and Map Division, it shows how we can annotate some locations expressed in the map.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="75-83"' %}

# Related recipes

* [Begin playback at a specific point - Time-based media][0015] uses a Point Selector for selecting for starting the playback at a specific time.
* [Simple Annotation — Tagging][0021] a simple annotation pointing to a region of an image.

{% include acronyms.md %}
{% include links.md %}
