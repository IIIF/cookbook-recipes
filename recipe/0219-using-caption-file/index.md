---
title: Using Captions and Subtitles with Video Content
id: 219
layout: recipe
tags: [video, caption, subtitle, presentation]
summary: "Representing the tight relationship between a video file and its caption or subtitle file."
---


## Use Case

Captions and subtitles may be available for your video content and you may want to enable them for your IIIF video resources. 

## Implementation notes

Caption, subtitle, and transcription files are text-based files commonly associated with A/V content, each defined for a specific intended use. Caption and subtitle file formats are used to mark up the external text track resources in connection with the HTML <track> element of a video file. The markup file formats use time tags that allow for time alignment of the video content with the captions or subtitles. 

Offering the caption file as an Item in the same Annotation Page that contains the media file itself enables us to express the tight relationship between the two. The `type` and `format` properties of the Item clarifies the relationship and the `motivation` value of `supplementing` indicates the fact that rendering this annotation is optional.

A transcription file, on the other hand, is a text-based representation of an audio or video file. As an alternative representation of the main resource, a transcription should be added to a resource via a linking property of type `rendering` instead of using the pattern described here. See related recipe below.

## Restrictions

Formats other than [WebVTT](https://w3c.github.io/webvtt/) (Web Video Text Tracks) are supported in IIIF, but may not be as widely supported in viewers.

## Example

In this example we use a caption file in the WebVTT format, but one could just as well use a subtitle file in the [SRT](https://en.wikipedia.org/wiki/SubRip) (SubRip Text) or [TTML](https://w3c.github.io/ttml3/index.html) (Timed Text Markup Language) formats, or other text-based format used for the same purpose.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config='data-line="38-56"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Transcription of Audio and Video][0017]
- [Providing Alternative Representations][0046]
- [Transformation - WebVTT or OHMS XML to Annotations][0079]

{% include acronyms.md %}
{% include links.md %}
