---
title: Rendering Resources Sequentially on a Timeline
id: 560
layout: recipe
tags: timeline
summary: "Placing image resources on a timeline to be shown in a sequence"
viewers:
topic:
 - realWorldObject
---

## Use Case

You have a set of images you would like to present sequentially in time, in the manner of an automated slide show.

## Implementation Notes

This recipe is very similar to [Composition from Multiple Images][0036], which describes using multiple IIIF resources on a single Canvas. The substantial difference between that recipe and this one is the incorporation of [the `duration` property](https://iiif.io/api/presentation/3.0/#duration) and [`behavior` values](https://iiif.io/api/presentation/3.0/#behavior) for instructing viewers on Canvas sequencing.

If a Canvas has a `duration` property, viewers have to process it, and can be helpful by providing an interactive means of displaying that Canvas for the value of the `duration`. To give a viewer instructions on showing a resource during all or part of that duration, the Canvas can use a media fragment on its `target` value, in the form `#t=`. For details on formats and semantics of this media fragment, see the [W3C Media Fragments section on Temporal Dimension](https://www.w3.org/TR/media-frags/#naming-time). Note that while the Media Fragments specification allows for values other than numbers of seconds, IIIF conventionally uses only whole and/or partial seconds. Fragment values can be individually or in the aggregate greater than the `duration` value. See [Rendering Multiple Media Types on a Time-Based Canvas][0489] for a brief explanation of the `timeMode` property and for more on the "t" parameter on a `target`.

Nothing in the Presentation API 3.0 says anything explicitly about a viewer initiating play upon loading a Canvas with a `duration` property, even with a`start` value. In addition, for browser-based viewers, people may configure their browsers to disable autoplay. Consequently, manifest creators should not assume a resource with `duration` will begin without interaction.

Once the timeline has started, the default action in IIIF is to display a Canvas for the `duration` value and stop, regardless of the individual or aggregate "t" parameter values on the `target`s of the Canvas's descendent `items`. To get the annotation sequence to repeat, the `behavior` value is set to `repeat`. This value is applicable only on Collections or Manifests containing Canvases with `duration`. Once the end of the `duration` (the end of the timeline) is reached, this behavior tells the viewer to start over at the beginning. Note that there is no mechanism for repeating a fixed number of times.

Within a Canvas's annotations, the parameterized `target` values tell viewers to show each item for the "t" parameter value, not stopping until an appropriate interaction or until and unless it reaches a Canvas with no `behavior` or a Canvas with an explicit `no-auto-advance` behavior. (The default is `no-auto-advance`, so no `behavior` is functionally equivalent to declaring `no-auto-advance`.)

## Restrictions

No known restrictions, but a caution: When using timing, a high degree of precision is not likely to be achieved for all people. Resources may load slowly for many reasons, including image server issues, network traffic, or browser and client customizations. Except in a very predictable environment, timing should be considered approximate.

## Example

In this example (a minimal implementation of the use case), there are two paintings from Winslow Homer to be displayed one after the other in a loop. For demonstration purposes, the Canvas `duration` is quite short (4.0 seconds) while the timing in a real-world situation would probably be longer. The paintings are `items` on a single Canvas and should progress automatically once the timeline is started.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Composition from Multiple Images][0036] for using multiple IIIF resources on a single Canvas
* [Image and Canvas with Differing Dimensions][0004] for details about the way this recipe uses resources with different dimensions on a Canvas with unchanging dimensions.
* [Rendering Multiple Media Types on a Time-Based Canvas][0489] is a more complex combination of still and time-based resources with various IIIF properties.

{% include acronyms.md %}
{% include links.md %}