---
title: Start - Time-based media
id: 15
layout: recipe
tags: [tbc]
summary: "tbc"
---


## Use Case

Where should the viewer start playing when a user opens this resource? Often an audio or video resource will have content that is part of the object but not significant, such as a microphone check, or audience noise before the start of a performance, or a test card. The `start` property allows the publisher to specify where a client application should start playback from. 

## Implementation notes

This recipe extends _Simplest Manifest - Video_[link] by adding the information required by a client to start playback at a particular point. This is done by adding the `start` property to the Manifest with the start time in seconds. 

The value of the `start` property is either a Canvas, or if a particular point in time within a Canvas. If the latter, the `start` property value is a `PointSelector` that identifies the timepoint within a particular canvas.

TODO - link to spec:

https://preview.iiif.io/api/image-prezi-rc2/api/presentation/3.0/#start

TODO - explain additional selector classes and what they are for:

https://preview.iiif.io/api/image-prezi-rc2/api/annex/openannotation/


## Restrictions

You can't use a PointSelector on a w,h Canvas

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.? (Not present if not needed.)

## Example

[JSON-LD](manifest.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```

# Related recipes

Link to recipe 3
link to spatial `start` recipe
(explain why, if not obvious...)


{% include acronyms.md %}
{% include links.md %}

