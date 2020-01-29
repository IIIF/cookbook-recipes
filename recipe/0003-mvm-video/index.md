---
title: Simplest Manifest - Video
id: 3
layout: recipe
tags: [video, presentation]
summary: "The simplest viable manifest for video content. This pattern presents a single video file in a IIIF Presentation resource."
---


## Use Case

The simplest viable manifest for video content. This pattern presents a single video file in a IIIF Presentation resource.

## Implementation notes

The implementation is identical to the [image example][0001], except that the content is video and the canvas has a duration instead of a height and width.

## Restrictions

None known.

## Example


This example shows a Manifest with a single Canvas that lasts for 3600 seconds, or exactly one hour. It has a single video file (video-sample.mp4) which is associated with it. The mp4 also has a duration of exactly one hour.

{: .line-numbers data-src="manifest.json" }
```json
```

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}

