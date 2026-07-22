## Use Case

Transcripts may be available for your audio and/or video content. You would like to give a viewer clear information on their purposeful relationship to your IIIF media resources.

## Implementation notes

External transcript files may exist in a wide variety of formats. To improve accessibility, it is ideal for a IIIF media viewer to display as many potential formats as possible. Common file formats for transcripts include WebVTT, SubRip Text, and plain text.

Offering the transcript file(s) as an Annotation on the Canvas that contains the media file itself enables us to express the relationship between the two. The `provides` property of the Annotation can be used by the client to identify transcript files for usable rendering along with the resource. The `format` property of the Annotation can be used to determine if the transcript file format can be rendered directly to the user by the media viewer.

The `provides` property is new in IIIF Presentation API v4. It exists to allow manifest creators to declare information about the function of a linked resource in relation to the linking resource. The value of `provides` tells a viewer or other manifest consumer what the point of the linked resource is, but does not define viewer behavior as a consequence. While people encountering a resource with a transcript file may have reasonable expectations for conventional viewer behaviors with that transcript, the IIIF Presentation API v4 does not prescribe any. Within the viewer's idiom, context, and other behaviors, viewer access to information about the function of a linked file in a manifest allows it to facilitate interaction with the file content by the widest possible range of people.

In addition to this implementation, one could also or instead offer a transcript as a series of time-coded textual annotations, making the text available in multiple ways. See [Using Annotations for Timed Text][0079-4].

While captions, subtitles, and transcripts each present some text interpretation of the A/V content, the ways in which they are consumed by users differ. For a more detailed discussion about these differences see [Transcripts, Captions, and Subtitles - General Considerations][0231-4]. For a particular comparison tho this recipe, note the [Using Caption Files with Video Content][0219-4] recipe. Caption/subtitle files, linked from a manifest using an Annotation with a `provides` value of `closedCaptions` or `subtitles`, accompany time-based media such as video or audio. The content of the files are text versions of the audio information in an audio or video resource. The content is time-coded so it can be presented at appropriate points in the time-based media resource.

## Restrictions

No known restrictions.

## Example

In this example we demonstrate a transcript file in the docx format, but other formats are possible (see above).

Note: This recipe only exists for IIIF Presentation API v4. Transcript, caption, and subtitle files can be linked via annotations in IIIF Presentation API v3 manifests with an Annotation `motivation` of `supplementing`. However, the lack of the `provides` property means viewers must infer the use of the file content rather than receiving that information directly.

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