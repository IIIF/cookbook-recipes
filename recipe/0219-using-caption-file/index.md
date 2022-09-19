---
title: Using Caption and Subtitle Files with Video Content
id: 219
layout: recipe
tags: [video, caption, subtitle, presentation]
summary: "Providing a caption or subtitle file to a video resource."
viewers:
 - Clover
topic: AV
---


## Use Case

Captions and subtitles may be available for your video content and you may want to enable them for your IIIF video resources. 

## Implementation notes

Caption and subtitle file formats are used to mark up the external text track resources in connection with the HTML track element of a video file. The markup file formats use time tags that allow for time alignment of the video content with the captions or subtitles. 

Offering the caption file as an Annotation on the Canvas that contains the media file itself enables us to express the relationship between the two. The `type` and `format` properties of the Annotation can be used by the client to identify files in a format supported by the media player for captions. The `motivation` value of `supplementing` indicates the fact that processing this Annotation is optional.

In addition to this implementation, one should consider offering the captions or subtitles as multiple timed annotations, making the text available in multiple ways. See [Using Annotations for Timed Text][0079].

While captions, subtitles, and transcripts each present some text interpretation of the A/V content, the ways in which they are consumed by users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231].

## Restrictions

Formats other than [WebVTT](https://w3c.github.io/webvtt/) (Web Video Text Tracks) are supported in IIIF, but may not be as widely supported in viewers. 

When using segmented WebVTT with HLS, see [Serving HLS Files][0257].

## Example

In this example we use a caption file in the WebVTT format, but other options include a subtitle file in the [SRT](https://en.wikipedia.org/wiki/SubRip) (SubRip Text) or [TTML](https://w3c.github.io/ttml3/index.html) (Timed Text Markup Language) formats, or other text-based format used for the same purpose.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="41-67"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Providing Access to Transcripts of A/V Content][0017]
- [Providing Alternative Representations][0046]
- [Using Annotations for Timed Text][0079]
- [Serving HLS Files][0257]

{% include acronyms.md %}
{% include links.md %}
