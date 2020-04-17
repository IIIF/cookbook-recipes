---
title: Table of contents (ranges) - acts of an opera
id: 26
layout: recipe
tags: [video, presentation, opera]
summary: "Complex nested table of contents for an opera."
---


## Use Case

An opera's table of contents can be hierarchically divided into acts, scenes, and arias.

## Implementation Notes

Implementation is similar to [Book Chapters][0024] except that nesting may be deeper.

Ranges in the structure target different portions of the same canvas using temporal [media fragments](https://www.w3.org/TR/media-frags/#naming-time) (e.g. "t=0,100").  This is in contrast to the Book Chapters recipe where each range targets a different canvas.

## Restrictions

Overlapping ranges are avoided because they cause the overlapping part to be played twice.

## Example

The opera covers the whole length of the canvas and is divided into two ranges for the two acts.  Act I has a range for the prelude and first song and then a range for the remainder of the act.  Act II has not been subdivided into ranges for simplicity of this example.

[JSON-LD](manifest.json)  |  [View in Universal Viewer](https://universalviewer.io/examples/#?manifest={{ site.url }}{{ site.baseurl }}{{ page.url }}manifest.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```

## Related Recipes

* [Table of Contents (Ranges) - Book Chapters][0024]
* [Simplest Manifest - Video][0003]
* [Opera One Canvas][0064] - The same opera from this example but expanded into a real world example.
* [Opera Multiple Canvases][0065] - The same opera from this example but expanded into a real world example in audio format split across multiple canvases.


{% include acronyms.md %}
{% include links.md %}

