---
title: An opera on multiple Canvases
id: 65
layout: recipe
tags: [video, presentation, opera]
summary: "A real world example of an audio recording of an opera spread across multiple canvases."
---


## Use Case

An opera performance can be long and split across multiple physical tapes, reels, or cassettes.  These may be digitized as one file per physical medium then mapped to one canvas per file.  This real world example shows how this can be modeled using multiple canvases.

## Implementation notes

Implementation is identical to the [opera on one canvas recipe](../0064-opera-one-canvas/index.md) except that there are two files, one for each act.  These files each have their own canvas and are referenced as such in the structures.

## Restrictions

None known.

## Example

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }

# Related recipes

* [Table of Contents - Opera](../0026-toc-opera/index.md) - Another example of using nested ranges to represent an opera's table of contents.
* [Opera One Canvas](../0064-opera-one-canvas/index.md) - The same opera from this example but in video format on one canvas.

{% include acronyms.md %}
{% include links.md %}