## Use Case

You want to represent captions for your video content as timed annotations.

## Implementation notes

This recipe follows the pattern for [Using Caption Files with Video Content][0219], but shows an alternative form of representing a caption file using annotations.

In this recipe, annotations are used to mark up video content shown on a canvas of the manifest. The time alignment of the captions with the video content is achieved by annotations that target the canvas by using Media Fragments URIs with a [temporal dimenstion](https://www.w3.org/TR/media-frags/#naming-time).  

## Restrictions



## Example

In this example we show the same captions and video from [Using Caption Files with Video Content][0219]. but the `annotations` section of the manifest links to a `AnnotationPage` instead of the WebVTT file. For readability, the example contains only the annotations that concern the captions of the first minute of the video. 

The `AnnotationPage` contains one annotation per individual caption entry, and these are provided as `supplementing` annotations on the Canvas that contains the video file. The references to the canvas uses Media Fragment URIs with a begin time and an end time. The language of the captions is expressed with a `language` property containing a [BCP 47](https://tools.ietf.org/html/bcp47) language code as specified by the Presentation API 3.0.

{% include manifest_links.html viewers="Clover, Ramp, Aviary, Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="39-44"'%}

{% include jsonviewer.html src="lunchroom_manners-captions-en.json" config='data-line="6-18"'%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Using Caption Files with Video Content][0219]
- [Using Caption and Subtitle Files in Multiple Languages with Video Content][0074]
- [Using Transcript Files with Audio or Video Content][0253]
- [Providing Access to Transcripts of A/V Content][0017]

{% include acronyms.md %}
{% include links.md %}
