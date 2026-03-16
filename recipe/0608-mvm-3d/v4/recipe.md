## Use Case

You have a 3D model that you would like to present on the web using IIIF.

## Implementation Notes

The implementation at this basic level is substantially the same as for other resources, with some changes to accommodate the nature of 3D models.

3D models are contained inside a Scene. Unlike a Canvas or a Timeline, a Scene does not use dimensions. Scenes are imagined to be infinite in the x, y, and z planes. This principle carries through to an Annotation `body`. In this example a model is painted on to the Scene with no additional information. The viewer is expected to place the model at the origin and add default lighting and camera.

## Example
This manifest shows an astronaut Model painted into the origin of the Scene. 

This asset (astronaut.glb) was originally uploaded by the user 'Poly by Google' to the defunct Google Poly repository under a Creative Commons Attribution (CC-BY) license. The version of the model used here was downloaded from [poly.pizza](https://poly.pizza/m/dLHpzNdygsg), a 3D model repository rehosting a subset of Creative Commons&#8211;licensed material from Google Poly.

{% include manifest_links.html manifest="v4/manifest.json" version="4" %}

{% include jsonviewer.html src="v4/manifest.json" %}

# Related Recipes

* [Simplest Manifest - Image][0001-4] a basic image example 
* [Simplest Manifest - Audio][0002-4] a basic audio example 
* [Simplest Manifest - Video][0003-4] a basic video example 

{% include acronyms.md %}
{% include links.md %}
