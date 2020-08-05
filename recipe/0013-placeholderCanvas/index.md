---
title: "Load a Preview Image Before the Main Content"
id: 13
layout: recipe
tags: video, audio, image, av
summary: "Provide the user with something to look at before they choose to start interacting with the main content, and/or while they wait for it to load/buffer."
---

## Use Case

You have an exceptionally large video to present to site visitors. As each visitor's connection reliability and bandwidth are unknown and unpredictable, you want to show them a still image preview of the video (which will load more quickly) until the video has finished loading or has sufficiently buffered. 

## Implementation notes

Across a Manifest and its resources, you may use more than one `placeholderCanvas`, allowing you to have an authentic `placeholderCanvas` for each appropriate resource (Collection, Manifest, Canvas, and Range). 

Always keep in mind the wide latitude given conforming clients: It is up to the client whether and in what sort of UI to display content you place in a `placeholderCanvas` property. Do not use this property for content that must be displayed. On the other hand, placing content in a `placeholderCanvas` does communicate to a conforming client that the content, if displayed, should be displayed before the resource to which it is attached.

## Restrictions

Each instance of `placeholderCanvas` may only contain one Canvas, and as such may specifically not contain an additional `placeholderCanvas` or an `accompanyingCanvas`.

## Example

In the example, the main content is a video of a performance of Donizetti's _L'elisir d'amore_ and the `placeholderCanvas` is a still frame from the video. For a site visitor with limited bandwidth, showing the still frame allows them to get an advance look at performance aspects such as costuming, staging, and set design.

_Note: The `placeholderCanvas` property is not yet supported in viewers._

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='12-38'"%}

# Related recipes

* [Simplest Manifest - Video][0003]
* [Audio Presentation with Accompanying Image][0014], using `accompanyingCanvas` to present one resource simultaneously with another.

{% include acronyms.md %}
{% include links.md %}

