---
title: Captions, Subtitles, and Transcripts - General Considerations
id: 231
layout: recipe
tags: [A/V, Transcripts]
summary: "General Considerations for using Captions, Subtitles, and Transcripts"
---

## Use Case

This meta recipe describes choices for using Captions, Subtitles, and Transcripts considering desired user experience.

## Captions and Subtitles

Captions and subtitles are used to optionally mark up the external text track resources in connection with the HTML element of a video file. They are available in various file formats such as [WebVTT](https://w3c.github.io/webvtt/) (Web Video Text Tracks) and [TTML](https://w3c.github.io/ttml3/index.html) (Timed Text Markup Language). These markup file formats include time tags that allow for time alignment of the captions or subtitles with the video content during playback.

See [Using Captions and Subtitles with Video Content][0219] for implementation details.

## Transcripts

Transcripts are text-based representations of material originally presented in another medium such as newspapers and audio or video recordings.
Depending on the desired user experience, there are 3 options for handling transcript files using the IIIF Presentation API:

1.	When the transcript is considered an alternate representation of the resource and the intention is to enable using the transcript independently of the resource, a link to the transcript can be offered so that the user can download it or view it outside the client. This is accomplished via the `rendering` link option and is well represented in [Providing Alternative Representations][0046].

2.	When the intention is to have the client display the transcript alongside the resource, one should follow the pattern used when making other supplementing materials available, i.e., via an annotation with the `supplementing` motivation associated with the corresponding canvas or at the manifest level. This transcript may or may not have time information.

3.	When the transcript contains spatial or temporal information, one can use this information in the media fragment portion of IIIF annotations to ensure spatial and/or temporal synchronization of the display of the annotations and the display of the resource itself. The motivation for the corresponding Annotation Page is `supplementing`.
     a.	For an example in the newspapers space see [Transcription of image-based content][0016].
     b.	For an example in the A/V space see [Using annotations for transcripts][0079].



## Related Recipes

* [Transcription of image-based content][0016]
* [Providing Alternative Representations][0046]
* [Using annotations for transcripts][0079]
* [Using Captions and Subtitles with Video Content][0219]


{% include acronyms.md %}
{% include links.md %}

