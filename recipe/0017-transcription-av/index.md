---
title: Using Transcripts with A/V Content
id: 17
layout: recipe
tags: [audio, video, presentation, transcript]
summary: "Transcripts as alternative representation of A/V content"
---


## Use Case

A/V is a common medium of making content available to researchers, scholars, and others. Transcripts are used alongside A/V resources for a variety of reasons. To give some examples: as a means for making these resources more accessible; when understanding the content is impaired by audio quality or speaker accent; or to enable text-based search on the A/V content.

## Implementation notes

A transcription file is a text-based representation of an audio or video file, which may or may not be in a timed text format. As an alternative representation of the main resource, a transcription should be added to a resource via a linking property of type `rendering`.

A transcript in a timed-text format, however, provides the ability for clients to synchronize it with its A/V resource during playback. When that syncrhonization experience is desired, it can be accomplished using annotations as discussed in [Transformation - WebVTT or OHMS XML to Annotations][0079].

## Restrictions

For a discussion about differences between captions, subtitles, and transcripts see [Using Captions and Subtitles with Video Content][0219].

## Example

In this example, the Manifest is using a single A/V file therefore it is indifferent to link the transcript at the Manifest level or at the Canvas level.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config='data-line="10-21"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Providing Alternative Representations][0046]
- [Transformation - WebVTT or OHMS XML to Annotations][0079]
- [Using Captions and Subtitles with Video Content][0219]

{% include acronyms.md %}
{% include links.md %}

