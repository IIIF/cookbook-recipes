---
title: Table of contents for A/V content
id: 26
layout: recipe
tags: [video, presentation, opera]
summary: "Complex nested table of contents for an opera."
---


## Use Case

Like books, A/V content can be divided into parts that constitute a unit of interest. It is important to provide users with easy access to these individual units, so the structure of an A/V item is represented in a table of contents to facilitate navigation given that jumping to a specific point using only the player slider is hard.

Opera is a form of theatre in which music has a leading role. A recording of an opera is a good example of structured A/V: an opera is composed of Acts; an Act is composed of Scenes; a Scene may include multiple Arias. Ranges are well suited to model the hierarchy of the components of an Opera.

## Implementation Notes

Implementation is similar to [Book Chapters][0024] except that nesting may be deeper.

Ranges in the structure target different portions of the same canvas using temporal [media fragments](https://www.w3.org/TR/media-frags/#naming-time) (e.g. "t=0,100"). This is in contrast to the Book Chapters recipe where each range targets a different canvas.

## Restrictions

Leaf range nodes in a structure are played linearly so they should be contiguous, since gaps will cause silent moments resulting in poor user experience.

## Example

The opera covers the whole length of the canvas and is divided into two ranges for the two acts. Act I has a range for the prelude and first song and then a range for the remainder of the act. Act II has not been subdivided into ranges for simplicity of this example.

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

- [Table of Contents (Ranges) - Book Chapters][0024]
- [Simplest Manifest - Video][0003]
- [Table of Contents for Multiple A/V files on a Single Canvas][0064] - The same opera from this example but expanded into a real world example.
- [Table of Contents for Multiple A/V files on Multiple Canvases][0065] - The same opera from this example but expanded into a real world example in audio format split across multiple canvases.
- [Text in Multiple Languages][0006] - Recipe explaining the use of multiple languages in text like in the label for this opera.

{% include acronyms.md %}
{% include links.md %}
