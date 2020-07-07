---
title: "Posters: placeholderCanvas"
id: 13
layout: recipe
tags: video, audio, image, av
summary: "Provide the user with something to look at before they choose to start interacting with the main content, and/or while they wait for it to load/buffer, and/or while interacting with the main content."
---

## Use Case

Provide the user with something to look at before they choose to start interacting with the main content, and/or while they wait for it to load/buffer, and/or while interacting with the main content.

## Implementation notes

For this property, it's particularly important to note the latitude given conforming clients. The IIIF Presentation API 3.0 only says that clients _may_ render the `placeholderCanvas` property, not _must_.

Note also the differences between this property and the `accompanyingCanvas` property. Only this property is used to load content before the main content is loaded. Either `placeholderCanvas` or `accompanyingCanvas` can be used for content while the user is interacting with the main content, with slightly different semantics. `placeholderCanvas` and `accompanyingCanvas` are each appropriate for describing an image to be shown while the main audio content is playing. `accompanyingCanvas` is more appropriate to use for audio to play while a user is interacting with a visual object.

## Restrictions

None known.

## Example

In the example, the main content is a video of Donizetti's "L'elisir d'amore" and the `placeholderCanvas` is a stillframe from the video, useful if the video itself is taking a long time to load for the site visitor.

{% include manifest_links.html viewers="UV,Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='15-46'"%}

# Related recipes

* [Additional optional accompanying content][0014] describes how to use `accompanyingCanvas`, a similar property to this one.

{% include acronyms.md %}
{% include links.md %}

