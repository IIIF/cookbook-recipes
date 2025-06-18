## Use Case

Captions may be available for your video content and should be enabled for display on top of your IIIF video resources.

## Implementation notes

Caption markup file formats use time tags that allow for time alignment and synchronized display of the video content with the captions. Captions are typically overlaid on top of the video. To improve accessibility, IIIF media viewers should support both [WebVTT](http://en.wikipedia.org/wiki/WebVTT) and [SRT](https://en.wikipedia.org/wiki/SubRip) formats for caption files if possible.

Offering the caption file as an Annotation on the Canvas that contains the media file itself enables us to express the relationship between the two. The `provides` property of the Annotation can be used by the client to identify caption files in a format that should be supported by the media player. The `format` property of the Annotation can also be used to verify that the file is in an appropriate format. 
In addition to this implementation, one can also offer captions as multiple timed annotations, making the text available in multiple ways. See [Using Annotations for Timed Text][0079].

While captions, subtitles, and transcripts each present some text interpretation of the A/V content, the ways in which they are consumed by users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231].

## Example

In this example we use a caption file in the WebVTT format, but other options include a caption file in the [SRT](https://en.wikipedia.org/wiki/SubRip) (SubRip Text) or [TTML](https://w3c.github.io/ttml3/index.html) (Timed Text Markup Language) formats, or other text-based format used for the same purpose.

{% include manifest_links.html viewers="" manifest="v4/manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="41-67"'%}

# Related recipes

- [Using Transcript Files with Video and Audio Content][0253]
- [Using Caption and Subtitle Files in Multiple Languages with Video Content][0074]
- [Using Annotations for Timed Text][0079]
- [Providing Access to Transcripts of A/V Content][0017]
- [Annotating a Poetry Reading][0103]

{% include acronyms.md %}
{% include links.md %}
