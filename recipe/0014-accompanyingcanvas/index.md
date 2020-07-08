---
title: "Posters: accompanyingCanvas"
id: 14
layout: recipe
tags: [tbc]
summary: "Provide the user with something to look at before they choose to start interacting with the main content, and/or while they wait for it to load/buffer, and/or while interacting with the main content."
---

## Use Case

You have content you'd like to provide to the user to enrich the presentation or experience of the main content. It could be something to experience before the user chooses to start interacting with the main content and/or something additional to consider while interacting with the main content. You might want to have an image available while an audio-only Canvas is playing or period- or theme-appropriate audio to play while a user is navigating an image-only Manifest.

## Implementation notes

Across a Manifest and its properties, you may use more than one `accompanyingCanvas`, allowing you to have an authentic `accompanyingCanvas` for each appropriate resource (Collection, Manifest, Canvas, and Range). Any resource, though, may only have one `accompanyingCanvas`.

The `target` of the `Annotation` of an `accompanyingCanvas` should have as its value the `id` of the `accompanyingCanvas`, not the `id` of the resource that has the `accompanyingCanvas.`<span style="background-color:#ffff00; color:#333333;">Note for cookbook author group: Am I remembering correctly the outcome of our discussion?</span>

Always keep in mind the wide latitude given conforming clients: It is up to the client whether and in what sort of UI to display content you place in a `accompanyingCanvas` property. Don't use this property for content that must be displayed. On the other hand, placing content in a `accompanyingCanvas` does tell a client that the content, if displayed, should be displayed at the same time as the resource to which it is attached.

## Restrictions

Each instance of `accompanyingCanvas` may only contain one Canvas, and as such may specifically not contain an additional `accompanyingCanvas` or a `placeholderCanvas`.

## Example

Describe in prose and provide examples, e.g.: 

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='15-46'"%}

# Related recipes

* [Posters: placeholderCanvas][0013], for presenting content ahead of with another resource.

{% include acronyms.md %}
{% include links.md %}
