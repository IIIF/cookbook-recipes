---
title: Using Transcripts with A/V Content
id: 17
layout: recipe
tags: [audio, video, presentation, transcript]
summary: "Transcripts as alternative representation of A/V content"
---


## Use Case

Transcripts may be available for your IIIF A/V resource and you may want to present them alongside the resource.

## Implementation notes

A transcription file is a text-based representation of an audio or video file, which may or may not be in a timed text format. As an alternative representation of the main resource, a transcription should be added to a resource via a linking property of type `rendering`.

## Restrictions

For a discussion about differences between captions, subtitles, and transcripts see [Using Captions and Subtitles with Video Content][0219].

## Example

In this example, the Manifest is using a single A/V file therefore it is indifferent to link the transcript at the Manifest level or at the Canvas level.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config='data-line="60-71"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Providing Alternative Representations][0046]
- [Using Captions and Subtitles with Video Content][0219]

{% include acronyms.md %}
{% include links.md %}

