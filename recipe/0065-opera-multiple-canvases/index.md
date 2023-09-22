---
title: Table of Contents for Multiple A/V Files on Multiple Canvases
id: 65
layout: recipe
tags: [video, presentation, opera]
summary: "A real world example of an audio recording of an opera spread across multiple Canvases."
viewers:
 - UV
 - Ramp
topic: AV
---

## Use Case

An opera performance can be long and split across multiple physical tapes, reels, or cassettes. These may be digitized as one file per physical medium then mapped to one Canvas per file. This real world example shows how this can be modeled using multiple Canvases.

## Implementation Notes

Implementation is identical to the [Table of Contents for multiple A/V Files on a Single Canvas][0064] recipe except that the two files, one for each act, each have their own Canvas and are referenced as such in the structures. With two Canvases the viewer will show the duration of only the file currently being played and the time will start at zero again when switching between files. This may be helpful when you have time references within files instead of the opera as a whole.

## Restrictions

Given the need for the player to switch context when moving from one file to the next, the result is segmented playback. To ensure continuous playback, all files should be annotated onto one single Canvas as in the [Table of Contents for multiple A/V Files on a Single Canvas][0064] recipe.

## Example

{% include manifest_links.html viewers="UV, Ramp" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

- [Simple Manifest - Video][0003]
- [Thumbnails][0012]
- [Table of Contents for A/V Content][0026] - Another example of using nested Ranges to represent an opera's table of contents.
- [Table of Contents for Multiple A/V Files on a Single Canvas][0064] - The same opera from this example but in video format on one Canvas.

{% include acronyms.md %}
{% include links.md %}
