---
title: An opera on one Canvas
id: 64
layout: recipe
tags: [video, presentation, opera]
summary: "A real world example of a video recording of an opera on one canvas."
---


## Use Case

Opera performances are generally long with lots of divisions, often hierarchical, making for a complex table of contents.  This real world example shows how this can be modeled using a single canvas.

## Implementation notes

This implementation builds upon the [opera table of contents recipe](../0026-toc-opera/index.md) but adds metadata, homepage, and thumbnail properties for more more context.

## Restrictions

None Known.

## Example

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }

# Related recipes

* [Table of Contents - Opera](../0026-toc-opera/index.md) - Another example of using nested ranges to represent an opera's table of contents.
* [Opera Multiple Canvases](../0065-opera-multiple-canvases/index.md) - The same opera from this example but in audio format split across multiple canvases.

{% include acronyms.md %}
{% include links.md %}

