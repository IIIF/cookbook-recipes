---
title: Table of contents for A/V content
id: 26
layout: recipe
tags: [video, presentation, opera]
summary: "Complex nested table of contents for an opera."
---


## Use Case

(Why does AV content have ToC? Navigation.  Opera is a good example.  Want to get to famous aria but need to jump to specific point using only slider is hard so ToC makes this easier.)  An opera's table of contents can be hierarchically divided into acts, scenes, and arias.

## Implementation Notes

Implementation is similar to [Book Chapters][0024] except that nesting may be deeper.

Ranges in the structure target different portions of the same canvas using temporal [media fragments](https://www.w3.org/TR/media-frags/#naming-time) (e.g. "t=0,100").  This is in contrast to the Book Chapters recipe where each range targets a different canvas.

## Restrictions

(Leaf range nodes in a structure are player linearly so for good UX they should be contiguous (no-gaps) and not overlapping.  Point to recipes that explain when you might want them.)  Overlapping ranges are avoided because they cause the overlapping part to be played twice.

## Example

The opera covers the whole length of the canvas and is divided into two ranges for the two acts.  Act I has a range for the prelude and first song and then a range for the remainder of the act.  Act II has not been subdivided into ranges for simplicity of this example.

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Table of Contents (Ranges) - Book Chapters][0024]
* [Simplest Manifest - Video][0003]
* [Opera One Canvas][0064] - The same opera from this example but expanded into a real world example.
* [Opera Multiple Canvases][0065] - The same opera from this example but expanded into a real world example in audio format split across multiple canvases.
* [Text in Multiple Languages][0006] - Recipe explaining the use of multiple languages in text like in the label for this opera.


{% include acronyms.md %}
{% include links.md %}

