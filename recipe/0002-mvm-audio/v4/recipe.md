## Use Case

You have some digital or digitized audio that you would like to present on the web using  IIIF.

## Implementation Notes

This illustrates the mandatory structure and properties of a manifest, with the simplest possible audio content. 

Audio resources are contained inside a [Timeline](https://iiif.io/api/presentation/4.0/model/#timeline), which is required to have a `duration` property with the time, in seconds, of the audio resource to be included in the timeline. The value of the `duration` property [must be a floating point number](https://iiif.io/api/presentation/4.0/model/#duration). If the duration value you have is an integer, it needs to be written with at least a decimal point and a trailing zero: `1985.0` rather than `1985`.

The JSON-LD opens with the `@context` declaration, which identifies the terms used in the document as belonging to the IIIF specification. The `id` property identifies this manifest with the URL at which it is available online. The `type` property must be `Manifest`. The `label` property is mandatory, and the language of its value must be given (or the special value `none`), using a [language map][prezi4-languages]. Here the language of the label is English and its value is "Simplest Audio Example (IIIF Presentation v4)". The manifest's `items` property is a list of timelines. In this example there is only one. The timeline's `id` property is used later as part of the `target` of the annotation that links to the single image. 

The `items` property of the Canvas is a list of annotation pages. In this case there is only one. The `items` property of the annotation page is a list of annotations. Again, in this case there is only one. This annotation links the audio resource and the timeline. The `body` of the annotation is an audio file, the url of which is the `id` property of the body. The duration of the audio file, in seconds, is given and here matches the timeline's `duration` property exactly. Matching is not required, but mismatches will change how much of the audio is heard and may change what happens after the audio finishes playing. The `target` property tells us both that the audio file is associated with the entirety of the container and that the container is a timeline, and the `motivation` property of `painting` tells us that the audio file is the content of the container.

## Example

This example shows a Manifest with a single Timeline that lasts for 1985.024 seconds. It has a single audio file associated with it. The mp4 also has a duration of 1985.024 seconds.

{% include manifest_links.html manifest="v4/manifest.json" version="4" %}

{% include jsonviewer.html src="v4/manifest.json" config='data-line="13"' %}

## Related Recipes

* [Simplest Manifest - Image][0001-4] for a minimal image Manifest
* [Simplest Manifest - Video][0003-4] for a minimal video Manifest
* [Simplest Manifest - 3D][0608] for a minimal 3D object Manifest

{% include acronyms.md %}
{% include links.md %}
