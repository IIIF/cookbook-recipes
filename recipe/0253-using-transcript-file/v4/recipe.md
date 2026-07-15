## Use Case

Transcripts may be available for your audio and/or video content and should be enabled for display with your IIIF media resources.

## Implementation notes

External transcript files may exist in a wide variety of formats. To improve accessibility, it is ideal for a IIIF media viewer to display as many potential formats as possible. Common file formats for transcripts include WebVTT, SubRip Text, and plain text.

Offering the transcript file(s) as an Annotation on the Canvas that contains the media file itself enables us to express the relationship between the two. The `provides` property of the Annotation can be used by the client to identify transcript files that should be usably rendered along with the resource. The `format` property of the Annotation can be used to determine if the transcript file format can be rendered directly to the user by the media viewer.

In addition to this implementation, one could also offer transcripts as a series of timed textual annotations, making the text available in multiple ways. See [Using Annotations for Timed Text][0079-4].

While captions, subtitles, and transcripts each present some text interpretation of the A/V content, the ways in which they are consumed by users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231-4].

## Restrictions

No known restrictions.

## Example

In this example we demonstrate a transcript file in the docx format, but other formats are possible (see above).

Note: This recipe only exists for IIIF Presentation API v4.

{% include manifest_links.html viewers="" manifest="v4/manifest.json" version="4"%}

{% include jsonviewer.html src="v4/manifest.json" config='data-line="43-61"'%}

# Related recipes

- [Using Caption Files with Video Content][0219-4]
- [Using Caption and Subtitle Files in Multiple Languages with Video Content][0074-4]
- [Using Annotations for Timed Text][0079-4]
- [Providing Access to Transcripts of A/V Content][0017]
- [Annotating a Poetry Reading][0103]

{% include acronyms.md %}
{% include links.md %}