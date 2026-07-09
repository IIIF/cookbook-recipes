## Use Case

You have some digital or digitized video that you would like to present on the web using IIIF.

## Implementation Notes

This illustrates the mandatory structure and properties of a manifest, with the simplest possible video content. 

The implementation is substantively identical to the [image example][0001-4], except that the content is video and the Canvas has the `duration` property additional to the `height` and `width` properties. See [Simplest Manifest - Image][0001-4] for enumeration and brief description of required properties.

The value of the `duration` property [must be a floating point number](https://iiif.io/api/presentation/4.0/model/#duration). If the duration value you have is an integer, it therefore needs to be written with at least a decimal point and a trailing zero: `1985.0` rather than `1985`.

The duration of the video file, in seconds, is given and here matches the Canvas's `duration` property exactly. Matching is not required, but mismatches will change how much of the video is presented and may change what happens after the video finishes playing. Likewise, the pixel dimensions of the video file match the dimensionless coordinate space units. Matching is also not required here, but mismatches may change the visual display.

## Example

This example shows a Manifest with a single Canvas that lasts for 572 seconds, or just under 10 minutes. It has a single video file associated with it. The mp4 also has a duration of 572 seconds.

{% include manifest_links.html manifest="v4/manifest.json" version="4" viewers="UV, Mirador, Clover, Ramp, Aviary, Theseus" %}

{% include jsonviewer.html src="v4/manifest.json" %}

# Related Recipes

* [Simplest Manifest - Image][0001-4] for a minimal image Manifest
* [Simplest Manifest - Audio][0002-4] for a minimal audio Manifest
* [Simplest Manifest - 3D][0608] for a minimal 3D object Manifest

{% include acronyms.md %}
{% include links.md %}
