---
title: Multimedia Canvas
id: 499
layout: recipe
tags: Complex Object
summary: "Paint a still image, a video with sound, and text onto a single Canvas"
viewers:
topic: 
 - annotation
---

## Use Case

You want to create a digital assignment by providing students with a IIIF image resource to analyze in a fixed amount of time, a timer to show students how long they have, and text instructions for how to complete the assignment. You want to keep everything in one IIIF viewer.

## Implementation Notes

This recipe pulls together techniques and structures described in other recipes, and adds new elements. In other recipes, this cookbook shows [how to place multiple resources on a single Canvas][0036] and how to work with [a resource with different dimensions than its Canvas][0004]. In the Use Case for this recipe, the aim is to mix AV and image IIIF resources, set an image to be visible for an amount of time, and resize and position an AV resource on a Canvas.

While other recipes have discussed [simple textual annotations][0266], this recipe changes the motivation for its textual annotations to `painting` to include the text directly and visibly on the Canvas. Each of the annotations in this recipe is bound both by its placement on the Canvas and by its time of visibility.

When using timing for showing and hiding resources on a Canvas, a high degree of precision is not likely to be achieved for all people viewing the Canvas. Resources may load slowly for many reasons, including on the IIIF image server side, for network traffic reasons, or from customizations in a person's browser. Except in a very predictable environment, timing should be considered approximate

## Restrictions

No restrictions known.

## Example

In this example, a still image, a video, and plaintext annotations are combined on a single Canvas to simulate a classroom assignment designed to introduce students to image study and notetaking in a compressed period of time. Note that this example contains material pedagogical design flaws and is not to be used as is for a classroom assignment.

A person using a viewer that supports this recipe is presented first with the instruction to "Press Play", added using a time-bound plaintext annotation. After pressing play, additional instructions appear, also created using a time-bound plaintext annotation. When the time elapses on this annotation, the person is presented with a clock video overlaid on top of a still image. In the hypothetical assignment, a student would follow the instructions and take notes on the still image while the clock counts up the time allotted. After 30 seconds passes, the still image and clock video disappear, replaced by text instructions to close the browser. (These final instructions stay visible for approximately 2-1/2 minutes to avoid an immediate return to the initial instructions.)

[Theseus Viewer temporary link](https://theseus-viewer.netlify.app/?iiif-content=http://localhost:4000//recipe/0489-multimedia-canvas/manifest.json)

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Image and Canvas with Differing Dimensions][0004] for relative dimensioning of a resource and a Canvas
* [Simplest Annotation][0266] for a basic textual annotation
* [Composition from Multiple Images][0036] for using multiple IIIF resources on a single Canvas

{% include acronyms.md %}
{% include links.md %}
