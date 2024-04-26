---
title: Providing Access to Transcript Files of A/V Content
id: 17
layout: recipe
tags: [audio, video, presentation, transcript]
summary: "Transcripts as alternative representation of A/V content"
viewers:
 - Ramp
topic: AV
property: rendering
code:
 - iiif-prezi3
---


## Use Case

You have a transcription file for your A/V resource and want to allow users to download it. 

## Implementation notes

A transcription file is a text-based representation of an audio or video file, which may or may not be in a timed-text format. As an alternative representation of the main resource, a transcription is added to a resource via the linking property `rendering`.

See [Using Annotations for Timed Text][0079] when the transcript is in a timed-text format and you want to take advantage of a client's ability to synchronize it with its A/V resource during playback.

While transcripts, captions, and subtitles each present some text interpretation of the A/V content, the ways they are consumed by the users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231].

## Restrictions

None.

## Example

In this example, the Manifest is using a single A/V file; therefore, it is equivalent to link the transcript at the Manifest level or at the Canvas level and we do it at the Canvas level to complement the example in [Providing Alternative Representations][0046].

In Ramp, the transcript file is made available to download on the right of the player controls. Click the filename listed in the menu to download the transcript file.

{% include manifest_links.html viewers="Ramp" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config='data-line="39-50"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Providing Alternative Representations][0046]
- [Using Annotations for Timed Text][0079]
- [Transcripts, Captions, and Subtitles - General Considerations][0231]
- [A side by side transcript of a video recording][0253]

{% include acronyms.md %}
{% include links.md %}

