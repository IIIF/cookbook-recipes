---
title: A video with table of contents on one Canvas
id: 64
layout: recipe
tags: [video, presentation, opera]
summary: "A video recording of an opera on one canvas."
---


## Use Case

Opera performances are generally long with lots of divisions, often hierarchical, making for a complex table of contents.  This real world example shows how this can be modeled using a single canvas.

## Implementation Notes

This implementation builds upon the [opera table of contents recipe][0026] but uses two video files, one for each act, annotated onto the same canvas.  With only one canvas the playback will be continuous across the two files and the viewer will report the sum duration of the two files providing the user with a cohesive viewing experience.  Metadata and thumbnail properties have been added for more context.

## Example

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Table of Contents - Opera][0026] - Another example of using nested ranges to represent an opera's table of contents.
* [Opera Multiple Canvases][0065] - The same opera from this example but in audio format split across multiple canvases.

{% include acronyms.md %}
{% include links.md %}

