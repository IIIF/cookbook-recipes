
## Use Case

Captions and subtitles may be available in multiple languages for video content and the IIIF Manifest representing the video can give access to representations of all the available languages. Because users will likely want to see captions/subtitles in their preferred language, you want to present the available languages as options from which one should be chosen.

## Implementation notes

This recipe builds on the pattern for [Using Caption Files with Video Content][0219], extending it to represent the availability of captions and subtitles in multiple languages. As in that recipe, it is worth noting that IIIF media viewers can best support all people experiencing multimedia content by supporting multiple common formats for caption files, such as WebVTT and SRT, wherever possible.

Similarly to offering a single caption/subtitle file, the multiple subtitle/caption files are provided as a `supplementing` Annotation on the Canvas that contains the video file. In the case of multiple captions/subtitles, however, the Annotation provides all the available languages as choices. IIIF viewers are then able to offer to end-users the choice for displaying subtitles/captions in one of the available languages during the video playback.

Likewise, there is no prohibition against also providing the captions/subtitles [as timed annotations][0079]. With variability and unpredictability in IIIF viewer support for captioning, providing multiple caption implementations may enable more people to see the captions or subtitles accompanying the video resource.

## Restrictions

Formats other than WebVTT (Web Video Text Tracks) are supported by the [Presentation API 3.0](https://iiif.io/api/presentation/3.0/), but WebVTT is the format most likely to be implemented in current IIIF viewers.

When using segmented WebVTT with HLS (HTTP Live Streaming), see [Serving HLS Files][0257].

## Example

In this example we represent a video with captions in Italian and subtitles in English.
For expressing their availability, we use an Annotation with a Choice body that contains two items, one for each language. The language of each file is expressed with a `language` property containing a [BCP 47](https://tools.ietf.org/html/bcp47) language code as specified by the [Presentation API 3.0](https://iiif.io/api/presentation/3.0/#language-of-property-values).

We are using subtitle files in the WebVTT format. Other format options include SRT (SubRip Text) or TTML (Timed Text Markup Language). Support for any particular format is not predictable across IIIF viewers.

{% include manifest_links.html viewers="Ramp, Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="60-92"'%}

# Related recipes

- [Using Caption Files with Video Content][0219]
- [Transcripts, Captions, and Subtitles - General Considerations][0231]
- [Using Annotations for Timed Text][0079]
- [Providing Access to Transcript Files of A/V Content][0017]


{% include acronyms.md %}
{% include links.md %}
