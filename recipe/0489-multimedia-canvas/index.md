---
title: Teaching with a Multimedia Canvas
id: 499
layout: recipe
tags: Complex Object
summary: "Paint a still image, a video with sound, and text onto a single Canvas"
viewers:
 - Theseus
topic: 
 - annotation
---

## Use Case

You want to create a digital assignment by providing students with a IIIF image resource to analyze in a fixed amount of time, a timer to show students how long they have, and text instructions for how to complete the assignment. You want to keep everything in one IIIF viewer.

## Implementation Notes

This recipe pulls together techniques and structures described in other recipes, and adds new elements. In other recipes, this cookbook shows [how to place multiple resources on a single Canvas][0036] and how to work with [a resource with different dimensions than its Canvas][0004]. Here, the aim is to mix AV and image IIIF resources, restrict Annotations' visibility by time ranges, and resize and position an AV resource on a Canvas.

Likewise, while other recipes have discussed [simple textual annotations][0266], this recipe uses a `painting` motivation for its textual annotations (rather than `commenting` as the linked recipe does) to include the text directly and visibly on the Canvas.

Once there is an AV resource included on a Canvas, there exists a notional timeline whose duration and time range can then be used in targeting resources to the Canvas. When resources' appearance on a Manifest are governed in part by time, they can be entered in in the Manifest in any order. If a `target` value includes a `t` parameter, the associated resource can be expected to be shown only for that span of time on the timeline. (See "Restrictions" below for caveats.)

The `t` parameter of the `target` value can also serve to trim an AV resource to be displayed for something other than its whole duration. An AV resource can thus have a `target` that governs its placement on the Canvas, its dimensions relative to the Canvas, its appearance duration, and the amount of its total running time that is used. AV resources can also take [a `timeMode` property](https://iiif.io/api/presentation/3.0/#timemode) that governs its rendering in conjunction with the `t` parameter of the target.

## Restrictions

When using timing for showing and hiding resources on a Canvas, a high degree of precision is not likely to be achieved for all people viewing the Canvas. Resources may load slowly for many reasons, including image server issues, network traffic, or browser and client customizations. Except in a very predictable environment, timing should be considered approximate. As well, people interacting with a multimedia Canvas may have greater or lesser control over the Canvas timeline. Consequently, creators cannot assume rigid implementation of timeline manipulation restrictions, even implied ones as in this recipe.

## Example

In this example, a still image, a video, and plaintext annotations are combined on a single Canvas to simulate a classroom assignment designed to introduce students to image study and notetaking in a compressed period of time. Note that this example contains material pedagogical design flaws and is not to be used as is for a classroom assignment.

The simultaneously visible resources are listed in the Manifest from the foreground to the background. The timer video comes first in the Manifest, as the only currently capable viewer places resources on the Canvas so that the first resource is the most foregrounded.

A person using a viewer that supports this recipe is presented first with the instruction to "Press Play", added using a time-bound plaintext annotation. After pressing play, additional instructions appear, also created using a time-bound plaintext annotation. When the time elapses on this annotation, the person is presented with a clock video overlaid on top of a still image. In the hypothetical assignment, a student would follow the instructions and take notes on the still image while the clock counts up the time allotted. After 30 seconds passes, the still image and clock video disappear, replaced by text instructions to close the browser. These final instructions stay visible for approximately 2-1/2 minutes to avoid an immediate return to the initial instructions.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Image and Canvas with Differing Dimensions][0004] for relative dimensioning of a resource and a Canvas
* [Table of Contents for Multiple A/V Files on a Single Canvas][0064] for time ranges in `target`s
* [Simplest Annotation][0266] for a basic textual annotation
* [Composition from Multiple Images][0036] for using multiple IIIF resources on a single Canvas

{% include acronyms.md %}
{% include links.md %}

