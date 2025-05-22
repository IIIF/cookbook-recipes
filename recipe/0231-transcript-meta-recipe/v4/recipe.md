## Use Case

This meta recipe describes options when using Transcripts, Captions, and Subtitles with your resources taking into consideration the desired user experience.

## Transcripts

Transcripts are textual representations of content originally presented in a non-textual medium such as audio or video recordings or manuscripts.
They are generally displayed alongside the original media or made available via download.
There are several options for handling transcripts using the IIIF Presentation API (v4). 

1. Providing access to the transcript via download

    When the transcript is considered an alternative representation of the resource, a link to the transcript can be offered so that the user can download it or view it outside the client. This is accomplished via the `rendering` link option.

    a. For an example of this option in the book space, see [Providing Alternative Representations][0046].

    b. For an example in the newspaper space see the ALTO example in [A basic newspaper][0068] recipe.
    
    c. For an example in the A/V space, see [Providing Access to Transcript Files of A/V Content][0017].


2. Providing access to a transcript alongside the resource via an external file 

    When the intention is to have the client display the transcript alongside the resource, one should use an annotation with the `supplementing` motivation and with the `provides` property specified to indicate a `transcript`. Note that this option offers the transcript file as a single annotation. The transcript file can take many different formats and may or may not include spatial/temporal information that allows synchronization between transcript fragments and display or streaming of media.

    a. For an example of this option in the A/V space, see [Using Transcript Files with Audio or Video Content][0253].


3. Providing access to transcript alongside the resource via textual annotations 

    When the transcript includes spatial and/or temporal information, the transcript can be expressed as a series of textual annotations. To accomplish that, create one annotation for each transcript fragment, including its spatial and/or temporal information in the media fragment portion of the annotation target url. The motivation of the corresponding annotations are `supplementing` with the `provides` property specified to indicate a `transcript`. This also allows synchronization between transcript annotations and display or streaming of media. 

    a. For an example in the image space see [Transcription of image-based content][016].
    
    b. For an example in the newspaper space see the example annotations in a [A basic newspaper][0068] recipe.
    
    c. For an example in the A/V space see [Using Annotations for Timed Text][0079].

## Captions

Captions are textual representations of spoken word and non-speech audio that are primarily used with video recordings. They are intended for users who cannot hear audio. Caption display must be synchronized with playback (generally over top of video), and caption file formats inherently include time tags that enable this synchronization. The most common formats are [WebVTT](https://w3c.github.io/webvtt/) (Web Video Text Tracks) or [SRT](https://en.wikipedia.org/wiki/SubRip) (SubRip Text). 

1. Serving a caption file directly
    
    The manifest for this case is nearly identical to option 2 above but, given the support for these standard file formats by modern viewers, the text is presented on top of the video, thus providing for a completely different viewing experience. The `provides` property is used to indicate that the annotation includes captions, rather than transcripts.

    a. See [Using Caption Files with Video Content][0219] for implementation details.

2. Transforming captions into textual annotations
    
    Like transcript files, caption files can be transformed into a series of textual annotations that include temporal information in the media fragment portion of the annotation target url. Each annotation includes the `provides` property to differentiate between captions and transcripts and enable display on top of video. 
    
    a. See [Using Annotations for Timed Text][0079].

## Subtitles

Subtitles are translations of captions into a different language than the original spoken audio. They are intended for users who can hear, but do not understand the spoken language in the recording. Just like captions, subtitles must be synchronized with playback. To provide subtitles, follow the pattern for the captions recipes above, but use a `provides` property value of `subtitles` in the appropriate annotation(s).

1. For an example of how to provide both captions and subtitles for a video recording, see [Using Caption and Subtitle Files in Multiple Languages with Video Content][0074].


## Related Recipes

* [Providing Alternative Representations][0046]
* [Providing Access to Transcript Files of A/V Content][0017]
* [A basic newspaper][0068]
* [Using Transcript Files with Audio or Video Content][0253]
* [Transcription of image-based content][016]
* [Using annotations for Timed Text][0079]
* [Using Caption Files with Video Content][0219]
* [Using Caption and Subtitle Files in Multiple Languages with Video Content][0219]


{% include acronyms.md %}
{% include links.md %}