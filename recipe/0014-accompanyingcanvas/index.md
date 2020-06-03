---
title: "Posters: accompanyingCanvas"
id: 14
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

Provide the user with something to look at before they choose to start interacting with the main content, and/or while they wait for it to load/buffer, and/or while interacting with the main content.

## Implementation notes

The `accompanyingCanvas` provides additional content for use while rendering the resource that has the `accompanyingCanvas` property. You might want to have an image visible while an audio-only Canvas is playing or background audio to play while a user is navigating an image-only Manifest. More than one IIIF resource may have the `accompanyingCanvas` property, though any resource may only have one instance of it. An exception is that no Canvas that is an `accompanyingCanvas` may itself have its own `accompanyingCanvas`. <span style="background-color:#ffff00; color:#333333;">Would this be better in Restrictions?</span>

The `target` of the `Annotation` of an `accompanyingCanvas` should have as its value the `id` of the `accompanyingCanvas`, not the `id` of the resource that has the `accompanyingCanvas.`<span style="background-color:#ffff00; color:#333333;">Am I remembering correctly the outcome of our discussion?</span>

For this property, it's particularly important to note the latitude given conforming clients. The IIIF Presentation API 3.0 only says that clients _may_ render the `accompanyingCanvas` property, not _must_. <span style="background-color:#ffff00; color:#333333;">Note also that the IIIF Presentation API 3.0 places makes no statements about how or even whether clients give users any controls over a Canvas used as an `accompanyingCanvas`.</span>

Note also the differences between this property and the `placeholderCanvas` property. Either `accompanyingCanvas` or `placeholderCanvas` can be used for content while the user is interacting with the main content, with slightly different semantics. `accompanyingCanvas` and `placeholderCanvas` are each appropriate for describing an image to be shown while the main audio content is playing. `accompanyingCanvas` is more appropriate to use for audio to play while a user is interacting with a visual object, while only `placeholderCanvas` is used to load content before the main content is loaded. 

## Restrictions

None known.

## Example

Describe in prose and provide examples, e.g.: 

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='15-46'"%}

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}

* [Book (simplest)][0009]
* Audio (simplest)
* Video (simplest)
* [Posters: placeholderCanvas][0013]
