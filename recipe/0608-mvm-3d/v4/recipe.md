
## Use Case

You have 3D model video that you would like to present on the web using IIIF.

## Implementation Notes

3D models are contained inside a Scene. Unlike canvases and timelines a Scene does not require dimensions as it is imagined to be infintie in the x,y and z planes. In this simple example a model is painted on to the Scene at the origin and the viewer is expected to add default lighting and cameras.

## Example
This manifest shows the astronaut Model painted into the origin of the Scene. 

This asset (astronaut.glb) was originally uploaded by the user 'Poly by Google' to the Google Poly 3D model repository, which now no longer exists. It was released under the terms of a Creative Commons Attribution (CC-BY) license. The version of the model used here was downloaded from [poly.pizza](https://poly.pizza/m/dLHpzNdygsg), a 3D model repository rehosting a subset of Creative Commons-licensed material from Google Poly.

{% include manifest_links.html manifest="v4/manifest.json" version="4" %}

{% include jsonviewer.html src="v4/manifest.json" %}

# Related Recipes

* [Simplest Manifest - Image][0001-4] a basic image example 
* [Simplest Manifest - Audio][0002-4] a basic audio example 
* [Simplest Manifest - Video][0003-4] a basic video example 

{% include acronyms.md %}
{% include links.md %}
