## Use Case

You have some digital or digitized audio that you would like to present on the web using  IIIF.

## Implementation Notes

Audio resources are contained inside a [Timeline](https://preview.iiif.io/api/prezi-4/presentation/4.0/model/#timeline), which is required to have a `duration` property. The value of the `duration` property [must be a floating point number](https://preview.iiif.io/api/prezi-4/presentation/4.0/model/#duration). If the duration value you have is an integer, it needs to be written with at least a decimal point and a trailing zero: `1985.0` rather than `1985`.

## Example

This example shows a Manifest with a single Timeline that lasts for 1985.024 seconds. It has a single audio file which is associated with it. The mp4 also has a duration of 1985.024 seconds.

{% include manifest_links.html manifest="v4/manifest.json" version="4" %}

{% include jsonviewer.html src="v4/manifest.json" config='data-line="13"' %}

## Related Recipes

* [Simplest Manifest - Image][0001] for a minimal image Manifest
* [Simplest Manifest - Video][0003] for a minimal video Manifest
* [Simplest Manifest - 3D][0608] for a minimal 3D object Manifest

{% include acronyms.md %}
{% include links.md %}
