## Use Case

Captions are available for your video content and you want to enable them for display with your IIIF video resources.

## Implementation notes

Caption markup file formats use time tags that allow for time alignment and synchronized display of the video content with the captions. Captions are typically overlaid on top of the video. IIIF media viewers can best support all people experiencing multimedia content by supporting multiple common formats for caption files, such as [WebVTT](http://en.wikipedia.org/wiki/WebVTT) and [SRT](https://en.wikipedia.org/wiki/SubRip), wherever possible.

Offering the caption file as an Annotation on the Canvas that contains the media file itself enables us to express the relationship between the two. The `provides` property of the Annotation can be used by the client to identify caption files to be rendered on top of video content. The `format` property of the Annotation can also be used to verify that the file is in a usable format. The `motivation` value of "supplementing" indicates the fact that this Annotation is in addition to the media resource.

In addition to this implementation, you can also offer captions as multiple timed annotations, making the text available in multiple ways. See [Using Annotations for Timed Text][0079-4].

While transcripts, captions, and subtitles each present some text interpretation of the A/V content, the ways in which they are consumed by users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231-4].

## Restrictions

When using segmented WebVTT with HLS, see [Serving HLS Files][0257].

## Example

In this example we use a caption file in the WebVTT format. Other options include the [SubRip Text (SRT)](https://en.wikipedia.org/wiki/SubRip) or [Timed Text Markup Language (TTML)](https://w3c.github.io/ttml3/index.html) formats, or other text-based formats used for the same purpose.

{% include manifest_links.html viewers="" manifest="v4/manifest.json" %}

{% include jsonviewer.html src="v4/manifest.json" config='data-line="41-67"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Providing Access to Transcripts of A/V Content][0017]
- [Providing Alternative Representations][0046]
- [Using Caption and Subtitle Files in Multiple Languages with Video Content][0074-4]
- [Using Annotations for Timed Text][0079-4]
- [Annotating a Poetry Reading][0103]
- [Using Transcript Files with Video and Audio Content][0253-4]
- [Serving HLS Files][0257]

{% include acronyms.md %}
{% include links.md %}
