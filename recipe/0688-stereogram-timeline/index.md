---
title: Alternating Stereogram Views on a Timeline
id: 688
layout: recipe
tags: [timeline, image]
summary: "Alternating left-eye and right-eye stereogram views on a single Canvas"
viewers:
 - Clover
topic:
 - realWorldObject
---

## Use Case

You have a stereogram image that contains left-eye and right-eye views side by side, and you want to present those views in a single-canvas animation that rapidly alternates between them.

This can help people inspect depth cues or compare small positional differences between the two views.

## Implementation Notes

This recipe uses one Canvas with a short `duration` and two `painting` Annotations. Each Annotation references a region of the same source image from Yale's IIIF Image API endpoint:

* first Annotation: left half (`x=0`)
* second Annotation: right half (`x=1409`)

Both Annotation `target` values point to the same Canvas with different temporal fragments (`#t=0,0.8` and `#t=0.8,1.6`). Because both image regions are painted to the same Canvas area, the two views overlay each other in time and produce a back-and-forth stereogram effect.

To repeat continuously, the Manifest sets `behavior` to `repeat`. As in [Rendering Resources Sequentially on a Timeline](https://iiif.io/api/cookbook/recipe/0560-resources-on-a-timeline/), playback start is viewer-dependent and may require user interaction.

## Restrictions

Timing behavior and autoplay are viewer-dependent. The interval values in this recipe are intended as a compact demonstration and may need adjustment for different audiences, devices, or network conditions.

## Example

In this example, both stereogram views come from the image behind `https://collections.library.yale.edu/iiif/2/1073279/`. The manifest crops the source image into left and right halves and alternates them on one Canvas.

{% include manifest_links.html viewers="Clover" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="10-12,18,31,53"' %}

## Related Recipes

* [Rendering Resources Sequentially on a Timeline](https://iiif.io/api/cookbook/recipe/0560-resources-on-a-timeline/) for the baseline timing pattern on a single Canvas
* [Composition from Multiple Images](https://iiif.io/api/cookbook/recipe/0036-composition-from-multiple-images/) for painting multiple image resources onto one Canvas

{% include acronyms.md %}
{% include links.md %}
