---
title: Simplest Manifest - Audio
id: 2
layout: recipe
tags: [audio, presentation]
summary: "The simplest viable manifest for audio content. This pattern presents a single audio file in a IIIF Presentation resource."
---


## Use Case

The simplest viable manifest for audio content. This pattern presents a single audio file in a IIIF Presentation resource.

## Implementation Notes

The implementation is identical to the [image example][0001], except that the content is audio and the canvas has the `duration` property instead of the `height` and `width` properties.

## Example

This example shows a Manifest with a single Canvas that lasts for 3600 seconds, or exactly one hour. It has a single audio file (audio-sample.mp4) which is associated with it. The mp4 also has a duration of exactly one hour.

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```

## Related Recipes

* [Simple Image Manifest][0001]

{% include acronyms.md %}
{% include links.md %}
