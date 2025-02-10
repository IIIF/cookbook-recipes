---
title: Using Transcript Files with Audio or Video Content
id: 253
layout: recipe
tags: [video, audio, transcript, presentation]
summary: "Providing a transcript file to to be rendered alongside an audio or video resource."
viewers:
 - Clover
 - Ramp
 - Aviary
 - Theseus
topic: AV
---


## Use Case

Transcripts may be available for your audio and/or video content and should be enabled for side-by-side display for your IIIF media resources.

## Implementation notes

External transcript files may exist in a wide variety of formats, including .docx, .txt, .vtt, and .pdf. To improve accessibility, it is ideal for a IIIF media viewer to display as many potential formats as possible.
Some markup file formats use time tags that allow for time alignment of the audio or video content with the transcript, primarily [WebVTT](http://en.wikipedia.org/wiki/WebVTT) or [SRT](https://en.wikipedia.org/wiki/SubRip) (SubRip Text).

Offering the transcript file(s) as an Annotation on the Canvas that contains the media file itself enables us to express the relationship between the two. The `provides` property of the Annotation can be used by the client to identify transcript files that should be rendered side-by-side or adjacent to the media item itself. 
The `format` property of the Annotation can be used to determine if the transcript file format can be rendered directly to the user by the media player.

In addition to this implementation, one can also offer transcripts as multiple timed annotations, making the text available in multiple ways. See [Using Annotations for Timed Text][0079].

While captions, subtitles, and transcripts each present some text interpretation of the A/V content, the ways in which they are consumed by users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231].

## Example

In this example we demonstrate transcript files in the WebVTT and Word formats, but other formats are possible (see above).

{% include manifest_links.html viewers="Clover, Ramp, Aviary, Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="41-67"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Providing Access to Transcripts of A/V Content][0017]
- [Providing Alternative Representations][0046]
- [Using Annotations for Timed Text][0079]
- [Serving HLS Files][0257]

{% include acronyms.md %}
{% include links.md %}
