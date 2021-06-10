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

1.	When the transcript is considered an alternative representation of the resource and the intention is to enable using the transcript independently of the resource, a link to the transcript can be offered so that the user can download it or view it outside the client. This is accomplished via the `rendering` link option.

    a. For an example of this option in the book space, see [Providing Alternative Representations][0046].

    b. For an example of using `rendering` in the A/V space, see [Using Transcripts with A/V content][0017].

2.	When the intention is to have the client display the transcript alongside the resource, one should follow the pattern used when making other supplementing materials available, i.e., via an annotation with the `supplementing` motivation associated with the corresponding canvas or at the manifest level. This transcript may or may not have time information. Note that this option offers the transcript file as a single annotation.

3.	When the transcript contains spatial and/or temporal information and the intention is to use that information to enable spatial and/or temporal synchronization between the display or streaming of the media and the display of the individual transcript fragments, one can provide to the client the spatial and/or temporal information in the media fragment portion of IIIF annotations, creating one annotation for each transcript fragment. The motivation for the corresponding Annotation Page is `supplementing`.

    a. For an example in the newspapers space see [A basic newspaper][0068].
    
    b. For an example in the A/V space see [Using annotations for transcripts][0079].



## Related Recipes

* [Using Transcripts with A/V content][0017]
* [Providing Alternative Representations][0046]
* [A basic newspaper][0068]
* [Using annotations for transcripts][0079]
* [Using Captions and Subtitles with Video Content][0219]


{% include acronyms.md %}
{% include links.md %}

