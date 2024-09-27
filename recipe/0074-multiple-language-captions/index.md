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

This recipe builds on the pattern for [Using Caption and Subtitle Files with Video Content][0219], extending it to represent the availability of captions and subtitles in multiple languages.

Similarly to offering a single caption/subtitle file, the multiple subtitle/caption files are provided as a `supplementing` Annotation on the Canvas that contains the video file. In the case of multiple captions/subtitles, however, the Annotation provides all the available languages as choices. IIIF viewers are then able to offer to end-users the choice for displaying subtitles/captions in one of the available languages during the video playback.

In addition to this implementation, one might consider to provide the captions/subtitles also as multiple timed annotations. Although redundant, providing both implementations will enable more IIIF viewers to display the captions/subtitles, since they may use whichever implementation they support. See [Using Annotations for Timed Text][0079].

## Restrictions

Formats other than WebVTT (Web Video Text Tracks) are supported by the [Presentation API 3.0](https://iiif.io/api/presentation/3.0/), but current IIIF viewers do not support the display of captions/subtitles. Nevertheless, WebVTT is the format most likely to be implemented.

When using segmented WebVTT with HLS (HTTP Live Streaming), see [Serving HLS Files][0257].

## Example

In this example we represent a video with subtitles in two languages: English and Italian.
For expressing the availability of the subtitles in the two languages, we use an Annotation with a Choice body that contains two items, one for each language. The language of each subtitle file is expressed with a `language` property  containing a [BCP 47](https://tools.ietf.org/html/bcp47) language code as specified by the [Presentation API 3.0](https://iiif.io/api/presentation/3.0/#language-of-property-values).

In this example we use subtitle files in the WebVTT format. Other format options include SRT (SubRip Text) or TTML (Timed Text Markup Language), but these are less likely to be supported in IIIF viewers.

{% include manifest_links.html viewers="Ramp, Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="60-92"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Using Caption and Subtitle Files with Video Content][0219]
- [Transcripts, Captions, and Subtitles - General Considerations][0231]
- [Using Annotations for Timed Text][0079]
- [Providing Access to Transcript Files of A/V Content][0017]


{% include acronyms.md %}
{% include links.md %}
