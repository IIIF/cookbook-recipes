---
title: Simplest Manifest - Audio
id: 2
layout: recipe
tags: [audio, presentation]
summary: "The simplest viable manifest for audio content. This pattern presents a single audio file in a IIIF Presentation resource."
viewers:
 - Mirador
 - UV
 - Clover
topic: 
 - basic
 - AV
code:
 - iiif-prezi3
---


## Use Case

The simplest viable manifest for audio content. This pattern presents a single audio file in a IIIF Presentation resource.

## Implementation Notes

The implementation is identical to the [image example][0001], except that the content is audio and the canvas has the `duration` property instead of the `height` and `width` properties.

## Example

This example shows a Manifest with a single Canvas that lasts for 1985.024 seconds. It has a single audio file (audio-sample.mp4) which is associated with it. The mp4 also has a duration of 1985.024 seconds.

{% include manifest_links.html viewers="UV, Mirador, Clover" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Simplest Manifest - Image][0001] and [Simplest Manifest - Video][0003] are equivalent to this example.

{% include acronyms.md %}
{% include links.md %}
