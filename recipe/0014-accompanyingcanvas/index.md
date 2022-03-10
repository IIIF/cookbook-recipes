---
title: "Audio Presentation with Accompanying Image"
id: 14
layout: recipe
tags: [audio,image]
summary: "Provide the user with something to look at before they choose to start interacting with the main content, and/or while they wait for it to load/buffer, and/or while interacting with the main content."
viewers:
topic: 
 - property
 - AV
property: accompanyingCanvas
---

## Use Case

You have content you would like to provide to the user to enrich the presentation or experience of the main content. It could be something to experience before the user chooses to start interacting with the main content and/or something additional to consider while interacting with the main content. You might want to have an image available while an audio-only Canvas is playing or, conversely, audio available while a user is navigating an image-only Manifest.

## Implementation notes

Across a Manifest and its properties, you may use more than one `accompanyingCanvas`, allowing you to have an authentic `accompanyingCanvas` for each appropriate resource (Collection, Manifest, Canvas, and Range).

The `target` of the `Annotation` of an `accompanyingCanvas` should have as its value the `id` of the `accompanyingCanvas`, not the `id` of the resource that has the `accompanyingCanvas`.

Always keep in mind the wide latitude given conforming clients: It is up to the client whether and in what sort of UI to display content you place in a `accompanyingCanvas` property. Don't use this property for content that must be displayed. On the other hand, placing content in a `accompanyingCanvas` does tell a client that the content, if displayed, should be displayed at the same time as the resource to which it is attached.

## Restrictions

Each instance of `accompanyingCanvas` may only contain one Canvas, and as such may specifically not contain an additional `accompanyingCanvas` or a `placeholderCanvas`.

## Example

In the example, the main Canvas contains audio of a performance of Gustav Mahler's Symphony No. 3 and the `accompanyingCanvas` contains an image of a page from the score.

_Note: The `accompanyingCanvas` property is not yet supported in viewers._

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='20-58'"%}

# Related recipes

* [Simplest Manifest - Video][0003]
* [Load a Preview Image Before the Main Content][0013], using `placeholderCanvas` to present one resource ahead of another.

{% include acronyms.md %}
{% include links.md %}
