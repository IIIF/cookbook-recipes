---
title: Two Uses of Behavior with Ranges
id: 229
layout: recipe
tags: structure
summary: "tbc"
viewers:
 - Annona
 - Theseus
 - Aviary
 - Ramp
topic: 
 - structure
---

## Use Case

In watching a single-file IIIF video resource you will display in a client, visitors could benefit from the ability to navigation within it visually, a bit like having thumbnail scrubbing. You're not able to segment the video, and you prefer visual navigation to a textual table of contents.

## Implementation Notes

The cookbook discusses elsewhere ways to use the `behavior` property for determining paging in a book ([simple book][0009] and [book `behavior` variations][0011]), [viewing direction for a visual resource][0010], [visibility of `tagging` Annotations][0021], tables of contents ([chapters][0024], [an opera on one canvas][0064], and [an opera on multiple canvases][0065]), [collection structure of a multi-volume work][0030], and how to indicate [an alternate view of book contents][0035] such as for a foldout.

This recipe shows two ways that `behavior` can serve in a Range to tell clients how navigation should work. (For a fuller discussion of Ranges, see [the Presentation API Range section][prezi3-range].) 

One of the present ways to influence navigation behavior is to use the `no-nav` value, telling a client explicitly to not include a portion of the resource in navigation. When this value appears, whatever Canvases or portions of Canvases are used in the `items` part of the Range should not appear in the interface's navigation. The `id` of a Canvas in the `items` section indicates a Canvas from the Manifest's own `items` section or can be such an `id` with a bounding fragment for AV resources.

The other value used in this recipe is the `thumbnail-nav` value, which directs the consuming client to present an alternate, visual navigation structure using the thumbnail(s) with this `behavior` value. The API is quite clear that a traditional table of contents is not the place to put this visual navigation. Something more akin to thumbnail scrubbing is the metaphor to aim for. This can work with AV resources, where thumbnails might be put along a timeline to represent key moments a viewer might want to use in navigation. It can also be used with still images, where thumbnails might be employed usefully to navigate very large images (long, tall, or both dimensions). For those large still images, thumbnail based navigation — independent of the manifest's Canvases' thumbnails — may be arranged in any way that presents a helpful experience.

Note that `behavior` values are inherited. In order to determine the behaviors governing a particular resource, [there are four inheritance rules to observe](https://iiif.io/api/presentation/3.0/#behavior), two of which apply to Ranges:
+ Canvases inherit behaviors from their referencing Manifest, but DO NOT inherit behaviors from any referencing Ranges, as there might be several with different behaviors.
+ Ranges inherit behaviors from any referencing Range and referencing Manifest.

## Restrictions

None known.

## Example

This example uses a video (roughly 55 minutes long) of a live opera performance. The first nine seconds of the video are marked, in the first subsidiary Range, with `no-nav` because they contain no meaningful video and audio. Subsequent peer Ranges divide the video into ten segments, each assigned a `thumbnail` property and a thumbnail image. While in an authentic environment these might be created from moments that are structurally, semantically, pedagogically, or otherwise significant, here they are merely an equal amount of running time except for the final one.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="78,83"'%}

## Related Recipes

{% include links.md %}

