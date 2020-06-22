---
title: Table of Contents for Multiple A/V files on a Single Canvas
id: 64
layout: recipe
tags: [video, presentation, opera]
summary: "A video recording of an opera on one canvas."
---


## Use Case

It is common to have A/V content split into multiple files. This recipe shows how to model such content using one single canvas. The advantage of using one single canvas is continuous playback across the files, with the viewer reporting the sum duration of the files, thus providing the user with a cohesive viewing/listening experience.

## Implementation Notes

This implementation builds upon the [Table of Contents for A/V content][0026] recipe but uses two video files, one for each act of the Opera used as example, annotated onto the same canvas: Atto Primo targets #t=0, and Atto Secondo targets #t=3971.24, right after the end of Atto Primo, thus ensuring continuous playback.

The opera covers the whole length of the canvas and is divided into two ranges for the two acts. Act I has a range for the prelude and first song and then a range for the remainder of the act. Act II has not been subdivided into ranges for simplicity of this example.

Metadata and thumbnail properties have been added for more context. Implementation is similar to [Book Chapters][0024], but nesting may be deeper.

## Example

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

- [Table of Contents for A/V Content][0026] - Another example of using nested ranges to represent an opera's table of contents.
- [Table of Contents for Multiple A/V files on Multiple Canvases][0065] - The same opera from this example but in audio format split across multiple canvases.
- [Text in Multiple Languages][0006] - Recipe explaining the use of multiple languages in text like in the label for this opera.
- [Thumbnails][0012]

{% include acronyms.md %}
{% include links.md %}
