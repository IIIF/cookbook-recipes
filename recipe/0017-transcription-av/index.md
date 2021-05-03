---
title: Using Transcripts with A/V Content
id: 17
layout: recipe
tags: [audio, video, presentation, transcript]
summary: "Transcripts as alternative representation of A/V content"
---


## Use Case

A/V is a common medium for content made available to researchers, scholars, and other interested populations. Transcripts are used alongside A/V resources for a variety of reasons; for example, when understanding the content is impaired by audio quality or speaker accent; to enable text-based search on the A/V content; or as a means for making A/V content consumable in a text format.

## Implementation notes

A transcription file is a text-based representation of an audio or video file, which may or may not be in a timed-text format. As an alternative representation of the main resource, a transcription is added to a resource via the linking property `rendering`.

A transcript in a timed-text format, however, provides the ability for clients to synchronize it with its A/V resource during playback. When that syncrhonization experience is desired, it can be accomplished using annotations as discussed in [Transformation - WebVTT or OHMS XML to Annotations][0079].

For a discussion about differences between captions, subtitles, and transcripts see [Using Captions and Subtitles with Video Content][0219].

## Restrictions

None

## Example

In this example, the Manifest is using a single A/V file therefore it is indifferent to link the transcript at the Manifest level or at the Canvas level.

In Mirador, a given transcript is made available within the sidebar menu, which can be toggled open by using the 'Sidebar toggle' (hamburger) button on the top left corner of the viewer.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config='data-line="10-21"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Providing Alternative Representations][0046]
- [Transformation - WebVTT or OHMS XML to Annotations][0079]
- [Using Captions and Subtitles with Video Content][0219]

{% include acronyms.md %}
{% include links.md %}

