---
title: Using Caption Files with Video Content
id: 219
layout: recipe
tags: [video, caption, subtitle, presentation]
summary: "Providing a caption file to a video resource."
viewers:
 - Clover
 - Ramp
 - Aviary
 - Theseus
topic: AV
---


## Use Case

Captions may be available for your video content and you may want to enable them for your IIIF video resources.

## Implementation notes

Caption file formats are used to mark up the external text track resources in connection with the HTML track element of a video file. The markup file formats use time tags that allow for time alignment of the video content with the captions.

Offering the caption file as an Annotation on the Canvas that contains the media file itself enables us to express the relationship between the two. The `provides` property of the Annotation can be used by the client to identify caption files in a format that should be supported by the media player. The `type` property of the Annotation can also be used to verify that the file is in an appropriate format. The `motivation` value of `supplementing` indicates the fact that processing this Annotation is optional.

In addition to this implementation, one can also offer captions as multiple timed annotations, making the text available in multiple ways. See [Using Annotations for Timed Text][0079].

While captions, subtitles, and transcripts each present some text interpretation of the A/V content, the ways in which they are consumed by users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231].

## Restrictions

Formats other than [WebVTT](https://w3c.github.io/webvtt/) (Web Video Text Tracks) are supported in IIIF, but may not be as widely supported in viewers.

When using segmented WebVTT with HLS, see [Serving HLS Files][0257].

## Example

In this example we use a caption file in the WebVTT format, but other options include a caption file in the [SRT](https://en.wikipedia.org/wiki/SubRip) (SubRip Text) or [TTML](https://w3c.github.io/ttml3/index.html) (Timed Text Markup Language) formats, or other text-based format used for the same purpose.

{% include manifest_links.html viewers="Clover, Ramp, Aviary, Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="41-67"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Using Caption and Subtitle Files in Multiple Languages with Video Content][0074]
- [A Side-by-side Transcript of a Video Recording][0253]
- [Providing Access to Transcripts of A/V Content][0017]
- [Using Annotations for Timed Text][0079]
- [Serving HLS Files][0257]

{% include acronyms.md %}
{% include links.md %}
