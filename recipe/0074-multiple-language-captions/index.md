---
title: Video with captions in multiple languages
id: 74
layout: recipe
tags: [video, caption, subtitle, presentation]
summary: "Representing the  relationship between a video file and its caption or subtitle files for multiple languages."
---


## Use Case

Captions and subtitles in multiple languages may be available for video content and all the available languages should be represented in the IIIF manifest of the video. Because users will likely want to see captions/subtitles in one language of choice, the available languages should be presented as options from which one should be chosen.

## Implementation notes

This recipe builds on the pattern for [Using Captions and Subtitles with Video Content][0219], extending it to represent the availability of captions and subtitles in multiple languages.

Similarly to offering a single caption/subtitle file, the multiple subtitles/captions files are offered as a supplementing Annotation on the Canvas that contains the video file. In the case of multiple captions/subtitles, however, the Annotation expresses all the available languages as choices. IIIF viewers are then able to offer to end-users the choice for displaying subtitles/captions in one of the available languages during the video playback.  

In addition to this implementation, one should consider offering the captions or subtitles as multiple timed annotations, making the text available in multiple ways. See [Using Annotations for Timed Text][0079].

## Restrictions

Formats other than WebVTT (Web Video Text Tracks) are supported in IIIF, but may not be as widely supported in viewers.

When using segmented WebVTT with HLS (HTTP Live Streaming), see [Serving HLS Files][0257].

## Example

In this example we represent a video with subtitles in two languages: English and Italian. 
For expressing the availability of the subtitles in the two languages, we use an Annotation with a Choice body that contains two items, one for each language.

In this example we use subtitles files in the WebVTT format. Other options include a subtitle file in the SRT (SubRip Text) or TTML (Timed Text Markup Language) formats, but these may not be as widely supported in viewers.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config='data-line="35-45"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Using Captions and Subtitles with Video Content][0219]
- [Transcripts, Captions, and Subtitles - General Considerations][0231]
- [Using Annotations for Timed Text][0079]
- [Providing Access to Transcript Files of A/V Content][0017]


{% include acronyms.md %}
{% include links.md %}
