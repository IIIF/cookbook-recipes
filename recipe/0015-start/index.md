---
title: Begin playback at a specific point - Time-based media
id: 15
layout: recipe
tags: [audio, video]
summary: "This manifest uses the 'start' property to specify a point in an audio or video object where a client application should begin playback."
---

## Use Case

Often an audio or video resource will have content that is part of the object but not significant, such as a microphone check, or audience noise before the start of a performance, or a test card. The `start` property allows the publisher to specify a point where a client application should begin playback.

## Implementation notes

This recipe extends [Simplest Manifest - Video][0003] by adding the information required by a client to start playback at a particular point. This is done by adding the `start` property to the Manifest with the start time in seconds.

In this use case, the value of the `start` property is a `PointSelector` that identifies a timepoint within a particular Canvas.

### About selector classes:

Selectors in Annotations are used to describe how to retrieve a given part of a resource. There are three Selector classes defined in the IIIF specification:
* `ImageApiSelector` describes the properties/operations available to retrieve a particular image presentation, such as region, size, rotation, etc.
* `PointSelector` describes the properties available to select a specific point either spatially (`x`, `y`) or temporally (`t`).
* Content Selectors, `AudioContentSelector` and `VisualContentSelector`, allow the publisher to refer to only one aspect of the content, either audio or visual. This can be used to refer to visual content from one resource and audio content from another.

For more on the above Selectors, see: [IIIF Open/Web Annotation Extensions](https://iiif.io/api/annex/openannotation/). For additional Selectors, see the [WC3 Web Annotation Selectors](https://www.w3.org/TR/annotation-model/#selectors) (in particular, the FragmentSelector).

For more on the `start` property, see: [https://iiif.io/api/presentation/3.0/#start](https://iiif.io/api/presentation/3.0/#start)

## Example

This example shows a Manifest with a single Canvas that lasts for 1801.055 seconds. It has a single video file (30-minute-clock.mp4) which is associated with it. The `start` property specifies a start point of 120.5 seconds into the playback.

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

# Related recipes

* [Simplest Manifest - Video][0003] shows a manifest for a simple video resource.
* [The 'Start' Property - Spatial] demonstrates the `start` property with a spatial (map) resource.


{% include acronyms.md %}
{% include links.md %}
