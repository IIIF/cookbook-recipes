---
title: Providing Access to Transcripts of A/V Content
id: 17
layout: recipe
tags: [audio, video, presentation, transcript]
summary: "Transcripts as alternative representation of A/V content"
---


## Use Case

You have a transcription file for your A/V resource and want to allow users to download it. 

## Implementation notes

A transcription file is a text-based representation of an audio or video file, which may or may not be in a timed-text format. As an alternative representation of the main resource, a transcription is added to a resource via the linking property `rendering`.

See [Using Annotations for Transcripts][0079] when the transcript is in a timed-text format and you want to take advantage of a client's ability to synchronize it with its A/V resource during playback.

While transcripts, captions, and subtitles each present some text interpretation of the A/V content, the ways they are consumed by the users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231].

## Restrictions

None.

## Example

In this example, the Manifest is using a single A/V file; therefore, it is equivalent to link the transcript at the Manifest level or at the Canvas level and we do it at the Canvas level to complement the example in [Providing Alternative Representations][0046].

In Mirador, a given transcript is made available within the sidebar menu, which can be toggled open by using the 'Sidebar toggle' (hamburger) button on the top left corner of the viewer.

In Universal Viewer, to access the transcript use the 'Download' link on the bottom left corner of the viewer.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config='data-line="39-50"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Providing Alternative Representations][0046]
- [Using Annotations for Transcripts][0079]
- [Transcripts, Captions, and Subtitles - General Considerations][0231]
- [A side by side transcript of a video recording][0253]

{% include acronyms.md %}
{% include links.md %}

