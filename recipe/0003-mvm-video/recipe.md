## Use Case

The simplest viable manifest for video content. This pattern presents a single video file in a IIIF Presentation resource.

## Implementation Notes

The implementation is identical to the [image example][0001], except that the content is video and the canvas has the `duration` property additional to the `height` and `width` properties. The value of the `duration` property [must be a floating point number](https://iiif.io/api/presentation/3.0/#duration). If the duration value you have is an integer, it therefore needs to be written with at least a decimal point and a trailing zero: `1985.0` rather than `1985`.

## Example

This example shows a Manifest with a single Canvas that lasts for 572 seconds, or just under 10 minutes. It has a single video file (lunchroom_manners_1024kb.mp4) which is associated with it. The mp4 also has a duration of 572 seconds.

{% include manifest_links.html viewers="UV, Mirador, Clover, Ramp, Aviary, Theseus, Glycerine Viewer" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

# Related Recipes

* [Simplest Manifest - Image][0001] and [Simplest Manifest - Audio][0002] are equivalent to this example.

{% include acronyms.md %}
{% include links.md %}
