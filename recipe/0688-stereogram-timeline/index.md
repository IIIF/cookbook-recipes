---
title: Alternating Stereograph Views on a Timeline
id: 688
layout: recipe
tags: [timeline, image]
summary: "Alternating left-eye and right-eye stereograph views on a single Canvas"
viewers:
 - Clover
topic:
 - realWorldObject
---

## Use Case

You have a stereograph image that contains left-eye and right-eye views side by side, and you want to present those views in a single-canvas animation that rapidly alternates between them. Comparing small positional differences between the two views communicates depth information.

## Implementation Notes

This recipe uses one Canvas with a short `duration` and two `painting` Annotations. Each Annotation references a region of the same source image from the University of Minnesota's IIIF Image API endpoint:

* first Annotation: left-eye selector
* second Annotation: right-eye selector

Both Annotation `target` values point to the same Canvas with different temporal fragments (`#t=0,0.2` and `#t=0.2,0.4`). Because both image regions are painted to the same Canvas area, the two views overlay each other in time and produce a back-and-forth stereogram flicker effect.

To repeat continuously, the Manifest sets `behavior` to `repeat`. As in [Rendering Resources Sequentially on a Timeline](https://iiif.io/api/cookbook/recipe/0560-resources-on-a-timeline/), playback start is viewer-dependent and may require user interaction. This may cause flashing images, which may be undesirable for some audiences.

This recipe is an exclusive way to present stereographs. While this approach is available using the IIIF Presentation API, you may want to also include a more traditional side-by-side presentation of the same views in your Manifest.

Two versions of the Manifest are included in this recipe: one with `ImageApiSelector` regions on a `SpecificResource` body, and one with direct region URLs in the Annotation `target`. Both approaches are valid and should produce the same behavior in viewers that support them. The `ImageApiSelector` approach is more consistent with the IIIF model of a single source image and multiple views of it, while the direct region URL approach is more compact and more widely supported by viewers.

## Restrictions

Timing behavior and autoplay are viewer-dependent. The interval values in this recipe are intended as a compact demonstration and may need adjustment for different audiences, devices, or network conditions.

## Examples

In this example, both stereogram views come from UMedia item 856, `Stereographic film, men with fish`. Conventionally, image resources like this are photographed with both perspectives in the same print. 

[![Thumbnail, men with fish](https://cdm16022.contentdm.oclc.org/iiif/2/p16022coll349:856/full/256,137/0/default.jpg)](https://cdm16022.contentdm.oclc.org/iiif/2/p16022coll349:856/full/full/0/default.jpg)

The Manifest crops left-eye and right-eye views from the same source image and alternates them on one Canvas.

{% include manifest_links.html viewers="Clover" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="10-12,18,31,53"' %}

### ImageApiSelector variant

This version of the Manifest uses `ImageApiSelector` regions on a `SpecificResource` body so you can test Clover behavior against the direct-region URL approach.

{% include manifest_links.html viewers="Clover" manifest="manifest-imageapiselector.json" %}

{% include jsonviewer.html src="manifest-imageapiselector.json" config='data-line="10-12,18,31,44-66,76-98"' %}

## Related Recipes

* [Rendering Resources Sequentially on a Timeline](https://iiif.io/api/cookbook/recipe/0560-resources-on-a-timeline/) for the baseline timing pattern on a single Canvas
* [Addressing a Spatial Region](https://iiif.io/api/cookbook/recipe/0299-region/) for using ImageApiSelector regions to show a fragment of an image on the Canvas
* [Composition from Multiple Images](https://iiif.io/api/cookbook/recipe/0036-composition-from-multiple-images/) for painting multiple image resources onto one Canvas

{% include acronyms.md %}
{% include links.md %}
