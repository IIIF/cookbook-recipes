---
title: Table of contents (ranges) - acts of an opera
id: 26
layout: recipe
tags: [video, presentation, opera]
summary: "Complex nested table of contents for an opera."
---


## Use Case

An opera's table of contents can be hierarchically divided into acts, scenes, and arias.

## Implementation notes

Implementation is similar to [Book Chapters](../0024-toc-book-chapters/index.md) except that nesting may be deeper.

Ranges in the structure target different portions of the same canvas using temporal Media Fragments (e.g. "t=0,100").  This is in contrast to the Book Chapters recipe where each range targets a different canvas.

## Restrictions

The ranges here don’t overlap (although that is allowed in the spec) because that can affect the user experience of playing through all the ranges in a player (the overlapping part would be played twice).

## Example

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }

# Related recipes

* [Table of Contents (Ranges) - Book Chapters](../0024-toc-book-chapters/index.md)
* [Simplest Manifest - Video](../0003-mvm-video/index.md)
* [Opera One Canvas](../0064-opera-one-canvas/index.md) - The same opera from this example but expanded into a real world example.
* [Opera Multiple Canvases](../0065-opera-multiple-canvases/index.md) - The same opera from this example but expanded into a real world example in audio format split across multiple canvases.


{% include acronyms.md %}
{% include links.md %}

