---
title: Transcripts, Captions, and Subtitles - General Considerations
id: 231
layout: recipe
tags: [Transcripts, Captions, Subtitles]
summary: "General Considerations for using Transcripts, Captions, and Subtitles"
---

## Use Case

This meta recipe describes options when using Transcripts, Captions, and Subtitles with your resources taking into consideration the desired user experience.

## Transcripts

Transcripts are text-based representations of material originally presented in another medium such as newspapers and audio or video recordings.
There are 3 options for handling transcript files using the IIIF Presentation API; which option to use depends on the desired user experience:

1. Providing independent access to the transcript via download

    When the transcript is considered an alternative representation of the resource, a link to the transcript can be offered so that the user can download it or view it outside the client. This is accomplished via the `rendering` link option.

    a. For an example of this option in the book space, see [Providing Alternative Representations][0046].

    b. For an example in the newspaper space see the ALTO example in [A basic newspaper][0068] recipe.
    
    c. For an example in the A/V space, see [Providing Access to Transcript Files with A/V Content][0017].

2. Providing access to the transcript alongside the resource

    When the intention is to have the client display the transcript alongside the resource, one should follow the pattern used with other supplementing materials, i.e., via an annotation with the `supplementing` motivation associated with the corresponding Canvas or at the Manifest level. Note that this option offers the transcript file as a single annotation.

    a. For an example of this option in the A/V space, see [A Side-by-side Transcript of a Video Recording][0253].

3. Providing synchronized access to transcript and resource

    When the transcript includes spatial and/or temporal information, one can use that information to enable synchronization of the display or streaming of the media and the display of the individual transcript fragments. To accomplish that, create one annotation for each transcript fragment, including its spatial and/or temporal information in the media fragment portion of the annotation target url. The motivation of the corresponding Annotation is `supplementing`.

    a. For an example in the image space see [Transcription of image-based content][016].
    
    b. For an example in the newspaper space see the example annotations in a [A basic newspaper][0068] recipe.
    
    c. For an example in the A/V space see [Using Annotations for Timed Text][0079].

## Captions and Subtitles

Captions and subtitles are used to optionally mark up the external text track resources in connection with the HTML element of a *video* file. They are available in various file formats such as [WebVTT](https://w3c.github.io/webvtt/) (Web Video Text Tracks) and [TTML](https://w3c.github.io/ttml3/index.html) (Timed Text Markup Language). These markup file formats include time tags that allow for time alignment of the captions or subtitles with the video content during playback. 

1. Serving the Caption File directly
    
    The manifest for this case is identical to option 2 above but, given the support for these standard file formats by modern viewers, the text is presented on top of the video as it is expected for captions and subtitles, thus providing for a completely different viewing experience. 

    a. See [Using Captions and Subtitles with Video Content][0219] for implementation details.

    b. See [Serving HLS Files][0257] for details on using segmented WebVTT with HLS content.

2. Transforming captions into annotations
    
    Like transcription files, caption files can be transformed into annotations. This option aligns better with image-based annotations, so providers are encouraged to offer their captions and subtitles in this way. See [Using Annotations for Timed Text][0079].


## Related Recipes

* [Providing Alternative Representations][0046]
* [Providing Access to Transcript Files of A/V Content][0017]
* [A basic newspaper][0068]
* [A Side-by-side Transcript of a Video Recording][0253]
* [Transcription of image-based content][016]
* [Using annotations for transcripts][0079]
* [Using Captions and Subtitles with Video Content][0219]
* [Serving HLS Files][0257]


{% include acronyms.md %}
{% include links.md %}

