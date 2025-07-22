---
title: Using Caption and Subtitle Files in Multiple Languages with Video Content
id: 74
layout: recipe
tags: [video, caption, subtitle, presentation]
summary: "Representing the relationship between a video file and its caption or subtitle files for multiple languages."
topic: AV
viewers:
- Ramp
- Theseus
---


## Use Case

Captions and subtitles may be available in multiple languages for video content and the IIIF Manifest representing the video can give access to representations of all the available languages. Because users will likely want to see captions/subtitles in their preferred language, the available languages should be presented as options from which one should be chosen.

## Implementation notes

This recipe builds on the pattern for [Using Caption Files with Video Content][0219], extending it to represent the availability of captions and subtitles in multiple languages.

Similarly to offering a single caption file, the multiple subtitle/caption files are provided as `supplementing` Annotations on the Canvas that contains the video file, which also contain the `provides` property with the value `subtitles` or `closedCaptions`. One Annotation is used for each of the available captions/subtitles and languages. IIIF viewers  are then able to identify which annotations contain captions/subtitles by checking the value of the `provides` property, and offer to end-users the choice for displaying subtitles/captions in one of the available languages during the video playback.

## Restrictions

Formats other than WebVTT (Web Video Text Tracks) are supported by the Presentation API 4.0, but WebVTT is the format most likely to be implemented in current IIIF viewers.

## Example

In this example we represent a video with captions in Italian and subtitles in English. 
For expressing the availability of captions and subtitles in the two languages, we use two Annotations, one for each language. The language of each caption/subtitle file is expressed with a `language` property containing a [BCP 47](https://tools.ietf.org/html/bcp47) language code as specified by the Presentation API 4.0.

In this example we use files in the WebVTT format. Other format options include SRT (SubRip Text) or TTML (Timed Text Markup Language), but these are less likely to be supported in IIIF viewers.

{% include manifest_links.html viewers="Ramp, Theseus" manifest="v4/manifest.json" %}

{% include jsonviewer.html src="v4/manifest.json" config='data-line="60-95"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Using Caption Files with Video Content][0219]
- [Transcripts, Captions, and Subtitles - General Considerations][0231]
- [Using Annotations for Timed Text][0079]
- [Providing Access to Transcript Files of A/V Content][0017]


{% include acronyms.md %}
{% include links.md %}
