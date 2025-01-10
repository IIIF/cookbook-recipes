---
title: Rendering Resources Sequentially on a Timeline
id: 560
layout: recipe
tags: timeline
summary: "Placing resources on a timeline independent of format and individual duration"
viewers:
topic:
 - realWorldObject
---

## Use Case

You have a group of photographs taken in a temporal sequence that you would like to present as a simulation of animation, in the manner of a zoetrope.

## Implementation Notes

This recipe is very similar to [Composition from Multiple Images][0036], which describes using multiple IIIF resources on a single Canvas. The substantial difference between that recipe and this one is the incorporation of [the `duration` property](https://iiif.io/api/presentation/3.0/#duration) and [`behavior` values](https://iiif.io/api/presentation/3.0/#behavior) for instructing viewers on Canvas sequencing.

As soon as a Canvas has a `duration` property with a floating point number as the value, the viewer is expected to display that Canvas for only that many seconds.Though it is not shown in this recipe, resources can use the time fragment selector — with syntax `#t=[value in seconds]` — to display for only a portion of their containing Canvases `duration` value.

Nothing in [the spec][prezi3] says anything explicitly about a viewer initiating play upon loading a Canvas with a `duration` property, even with a`start` value. In addition, for browser-based viewers, people may configure their browsers to disable autoplay. Consequently, manifest creators should not assume a resource with a duration will engage without interaction.

With only the `duration` property on a Canvas, the default action in IIIF is to display a Canvas for that value and stop, even if there are multiple Canvases with durations. In order to display a series of resources without interaction, the Manifest needs added behaviors. For this recipe, the Manifest behavior is `repeat`, a value applicable only on Collections or Manifests containing Canvases with a duration value. Once the end of the timeline is reached, this behavior tells the viewer to start over at the beginning. In addition, each Canvas is assigned a behavior value of `auto-advance` to override the default IIIF temporal behavior. Once the timeline is started, the viewer can be expected to show each Canvas in sequence for its declared duration, not stopping absent interaction or until and unless it reaches a Canvas with no behavior or a Canvas with an explicit (but unnecessary) `no-auto-advance` behavior.

## Restrictions

No known restrictions, but pay careful attention to validity of property, value, and resource interactions. Publishers should consider target viewing environments and clients when providing complex views of this nature.

When using timing for presenting Canvases, a high degree of precision is not likely to be achieved for all people. Resources may load slowly for many reasons, including image server issues, network traffic, or browser and client customizations. Except in a very predictable environment, timing should be considered approximate.

## Example

In this example, there are two paintings from Winslow Homer to be displayed one after the other in a loop, imagining perhaps that an institution might want to display a slide show at its entrance. For demonstration purposes, the `duration` on each Canvas is quite short (4.0 seconds) while the timing in a real-world situation would undoubtedly be longer. 

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Composition from Multiple Images][0036] for using multiple IIIF resources on a single Canvas
* [Image and Canvas with Differing Dimensions][0004] for details about the way this recipe uses resources with different dimensions on a Canvas with unchanging dimensions.

{% include acronyms.md %}
{% include links.md %}