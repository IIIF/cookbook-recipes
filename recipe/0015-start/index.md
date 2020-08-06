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

The target of `start` must be a JSON object with `id` and `type` properties and can be either a Canvas, or a Specific Resource with a Selector and a `source` property where the value is a Canvas.

In this use case, the target `type` property is a Specific Resource (`"type": "SpecificResource"`), and the Selector `type` property is a Point Selector (`"type": "PointSelector"`) that identifies a starting timepoint (`"t": 120.5`) within the `source`.

### About selector classes:

Selectors in Annotation targets are used to describe how to retrieve a given part of a resource. There are three Selector classes defined in the IIIF specification, but only one that is appropriate for this use case - [`PointSelector`](https://iiif.io/api/annex/openannotation/#point-selector). The `PointSelector` defines a specific point either spatially (`x`, `y`) or temporally (`t`).

For more information on other Selector classes, see: [IIIF Open/Web Annotation Extensions](https://iiif.io/api/annex/openannotation/) and [WC3 Web Annotation Selectors](https://www.w3.org/TR/annotation-model/#selectors).

For more on the `start` property, see: [https://iiif.io/api/presentation/3.0/#start](https://iiif.io/api/presentation/3.0/#start)

## Example

This example shows a Manifest with a single Canvas with a duration of 1801.055 seconds. It has a single video file (30-minute-clock.mp4) which is associated with it. The `start` property specifies a start point of 120.5 seconds into the playback.

*Note: As of the writing of this recipe, playback of video content is supported by some viewers (Universal Viewer), but the `start` property for time-based objects is not yet supported in viewers.*

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="10-17"' %}

# Related recipes

* [Simplest Manifest - Video][0003] shows a manifest for a simple video resource.
<!-- * [The 'Start' Property - Spatial] demonstrates the `start` property with a spatial (map) resource. -->


{% include acronyms.md %}
{% include links.md %}
