## Use Case

The simplest viable manifest for 3D model. This pattern presents a single glb file in a IIIF Presentation Manifest.

## Implementation Notes

The implementation at this basic level is quite similar to other types of resources, with some changes to accommodate the nature of 3D models. See [Simplest Manifest - Image][0001-4] for enumeration and brief description of required properties.

3D models are contained inside a [Scene](https://iiif.io/api/presentation/4.0/#scene). Unlike a Canvas (for image and video resources) or a Timeline (for audio-only resources), a Scene does not use dimensions or duration. Scenes are imagined to be infinite in the x, y, and z planes. This principle carries through to an Annotation `body`, which likewise has no dimensions or duration.

## Example

This example shows an astronaut Model painted into the origin of the Scene, with no additional information. The viewer is expected to add default lighting and camera.

This asset (astronaut.glb) was originally uploaded by the user 'Poly by Google' to the defunct Google Poly repository under a Creative Commons Attribution (CC-BY) license. The version of the model used here was downloaded from [poly.pizza](https://poly.pizza/m/dLHpzNdygsg), a 3D model repository rehosting a subset of Creative Commons&#8211;licensed material from Google Poly.

{% include manifest_links.html manifest="v4/manifest.json" version="4" %}

{% include jsonviewer.html src="v4/manifest.json" %}

# Related Recipes

* [Simplest Manifest - Image][0001-4] a basic image example 

{% include acronyms.md %}
{% include links.md %}
