---
title: Multimedia Canvas
id: 499
layout: recipe
tags: Complex Object
summary: "tbc"
viewers:
topic: 
 - annotation
---

## Use Case

You want to create a digital assignment by providing students with a IIIF image resource to analyze in a fixed amount of time, a timer to show students how long they have, and text instructions for how to complete the assignment. You want to keep everything in one IIIF viewer.

## Implementation Notes

This recipe pulls together techniques and structures described in other recipes, and adds new elements. In other recipes, this cookbook shows [how to place multiple resources on a single Canvas][0036] and how to work with [a resource with different dimensions than its Canvas][0004]. In the Use Case for this recipe, the aim is to mix AV and image IIIF resources, set an image to be visible for an amount of time, and resize and position an AV resource on a Canvas.

## Restrictions

No restrictions known.

## Example

[Theseus Viewer temporary link](https://theseus-viewer.netlify.app/?iiif-content={{ id.path }}/manifest.json)

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Simple Image Manifest][0001]
* [Image and Canvas with Differing Dimensions][0004] for thinking through relative dimensioning of a resource and a Canvas

{% include acronyms.md %}
{% include links.md %}

