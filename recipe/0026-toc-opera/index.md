---
title: Table of Contents for A/V Content
id: 26
layout: recipe
tags: [video, presentation, opera]
summary: "Complex nested table of contents for an opera."
---


## Use Case

Like books, A/V content can be divided into parts that constitute a unit of interest. It is important to provide users with easy access to these individual units so the structure of an A/V item is represented in a table of contents to facilitate navigation given that jumping to a specific point using only the player slider is hard.

Opera is a form of theatre in which music has a leading role. A recording of an opera is a good example of structured A/V: an opera is composed of acts; an act is composed of scenes; a scene may include multiple arias. Ranges are well suited to model the hierarchy of the components of an opera.

## Implementation Notes

Implementation is similar to [Book Chapters][0024] except that nesting may be deeper.

Ranges in the structure target different portions of the same Canvas using temporal [media fragments](https://www.w3.org/TR/media-frags/#naming-time) (e.g. "t=0,100"). This is in contrast to the Book Chapters recipe where each Range targets a different Canvas using spatial media fragments.

A media fragment specifying the Canvas temporal dimensions for a Range does not need the end time to be explicitly specified when it coincides with the end time of the Canvas itself, as exemplified here for Atto Secondo.

## Restrictions

Leaf Range nodes in a structure are played linearly so they should be contiguous, since gaps will cause silent moments resulting in poor user experience.

## Example

The opera covers the whole length of the Canvas and is divided into two Ranges for the two acts. Atto Primo has a Range for the prelude and first song and then a Range for the remainder of the act. Atto Secondo has not been subdivided into Ranges for simplicity of this example.

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

- [Simplest Manifest - Video][0003]
- [Text in Multiple Languages][0006] - Recipe explaining the use of multiple languages in text like in the label for this opera.
- [Table of Contents (Ranges) - Book Chapters][0024]
- [Table of Contents for Multiple A/V Files on a Single Canvas][0064] - The same opera from this example but expanded into a real world example.
- [Table of Contents for Multiple A/V Files on Multiple Canvases][0065] - The same opera from this example but expanded into a real world example in audio format split across multiple Canvases.

{% include acronyms.md %}
{% include links.md %}
