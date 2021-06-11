---
title: Transcripts, Captions and Subtitles  - General Considerations
id: 231
layout: recipe
tags: [Transcripts, Captions, Subtitles]
summary: "General Considerations for using Transcripts, Captions and Subtitles"
---

## Use Case

This meta recipe describes options when using Transcripts, Captions and Subtitles with your resources considering desired user experience.

## Transcripts

Transcripts are text-based representations of material originally presented in another medium such as newspapers and audio or video recordings.
There are 3 options for handling transcript files using the IIIF Presentation API; which option to use depends on the desired user experience:

1. Providing independent access to the transcript

    When the transcript is considered an alternative representation of the resource and the intention is to enable using the transcript independently of the resource, a link to the transcript can be offered so that the user can download it or view it outside the client. This is accomplished via the `rendering` link option.

    a. For an example of this option in the book space, see [Providing Alternative Representations][0046].

    b. For an example of using `rendering` in the A/V space, see [Using Transcripts with A/V content][0017].

2. Providing access to the transcript alongside the resource

    When the intention is to have the client display the transcript alongside the resource, one should follow the pattern used with other supplementing materials, i.e., via an annotation with the `supplementing` motivation associated with the corresponding canvas or at the manifest level. This transcript may or may not have time information; in the case it does, the information is not used by the client. Note that this option offers the transcript file as a single annotation.

    a. For an example in the newspaper space see [A basic newspaper][0068].

    b. For an example in the A/V space, see [].

3. Providing syncrhonized access to transcript and resource

    When the transcript includes spatial and/or temporal information, one can use that information to enable synchronization of the display or streaming of the media and the display of the individual transcript fragments. To accomplish that, create one annotation for each transcript fragment, including its spatial and/or temporal information in the media fragment portion of the annotation target url. The motivation of the corresponding Annotation Page is `supplementing`.

    a. For an example in the image space see [Transcription of image-based content][016].
    
    b. For an example in the A/V space see [Using annotations for transcripts][0079].

## Captions and Subtitles

Captions and subtitles are used to optionally mark up the external text track resources in connection with the HTML element of a *video* file. They are available in various file formats such as [WebVTT](https://w3c.github.io/webvtt/) (Web Video Text Tracks) and [TTML](https://w3c.github.io/ttml3/index.html) (Timed Text Markup Language). These markup file formats include time tags that allow for time alignment of the captions or subtitles with the video content during playback.

See [Using Captions and Subtitles with Video Content][0219] for implementation details.

## Related Recipes

* [Providing Alternative Representations][0046]
* [Using Transcripts with A/V content][0017]
* [A basic newspaper][0068]
* [Transcription of image-based content][016]
* [Using annotations for transcripts][0079]
* [Using Captions and Subtitles with Video Content][0219]


{% include acronyms.md %}
{% include links.md %}

