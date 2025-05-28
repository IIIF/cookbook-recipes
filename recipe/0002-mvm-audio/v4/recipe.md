## Use Case

You have some digital or digitized audio that you would like to present on the web using  IIIF.

## Implementation Notes

The implementation is identical to the [image example][0001], except that the content is audio, which requires the use of a [Timeline](https://preview.iiif.io/api/prezi-4/presentation/4.0/model/#timeline) instead of a Canvas. The Timeline has the `duration` property instead of the Canvas' `height` and `width` properties. The value of the `duration` property [must be a floating point number](https://iiif.io/api/presentation/3.0/#duration). If the duration value you have is an integer, it therefore needs to be written with at least a decimal point and a trailing zero: `1985.0` rather than `1985`.

## Example

This example shows a Manifest with a single Timeline that lasts for 1985.024 seconds. It has a single audio file which is associated with it. The mp4 also has a duration of 1985.024 seconds.

{% include manifest_links.html manifest="v4/manifest.json" version="4" config='data-line="13"' %}

{% include jsonviewer.html src="v4/manifest.json" %}

## Related Recipes

* [Simplest Manifest - Image][0001] for the most minimal image Manifest
* [Simplest Manifest - Video][0003] for the most minimal video Manifest

{% include acronyms.md %}
{% include links.md %}
