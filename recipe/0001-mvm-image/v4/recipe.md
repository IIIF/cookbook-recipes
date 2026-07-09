
## Use Case

The simplest viable manifest for image content. If all you have for an object is one image on the web and a label to go along with it, this pattern turns it into a IIIF Presentation resource. If you would like to enable deep zooming, you will need to use a IIIF Image server. For this, see the [Support Deep Viewing with Basic Use of a IIIF Image Service (v3)][0005] recipe.

## Implementation Notes

This illustrates the mandatory structure and properties of a manifest, with the simplest possible image content. 

The JSON-LD opens with the `@context` declaration, which identifies the terms used in the document as belonging to the IIIF specification. The `id` property identifies this manifest with the URL at which it is available online. The `type` property must be `Manifest`. The `label` property is mandatory, and the language of its value must be given (or the special value `none`), using a [language map][prezi4-languages]. Here the language of the label is English and its value is "Simplest Image Example (IIIF Presentation v4)". The manifest's `items` property is a list of canvases. In this example there is only one canvas, with a `height` of 1800 and a `width` of 1200. These units have no dimension; they establish a coordinate space that in this case the single image will fill. The Canvas's `id` property is used later as part of the `target` of the annotation that links to the single image. 

The `items` property of the Canvas is a list of annotation pages. In this case there is only one. The `items` property of the annotation page is a list of annotations. Again, in this case there is only one. This annotation links the image resource and the Canvas. The `body` of the annotation is an image, the url of which is the `id` property of the body. The dimensions of the image, in pixels, are given and here match the Canvas dimensions exactly. Matching is not required, but mismatches may change the image's display. The `target` property tells us both that the image is associated with the entirety of the container and that the container is a canvas, and the `motivation` property of `painting` tells us that a client should render the image to fill the Canvas.

## Restrictions

This recipe is not for large images or deep zoom functionality. For this, see the [Support Deep Viewing with Basic Use of a IIIF Image Service (v3)][0005] recipe.

## Example

{% include manifest_links.html manifest="v4/manifest.json" version="4" %}

{% include jsonviewer.html src="v4/manifest.json" %}

# Related Recipes

* [Simplest Manifest - Audio][0002-4] for a minimal audio Manifest
* [Simplest Manifest - Video][0003-4] for a minimal video Manifest
* [Simplest Manifest - 3D][0608] for a minimal 3D Manifest
* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005] (v3) shows a basic manifest for use with a IIIF Image server.
* [Image and Canvas with Differing Dimensions][0004] (v3) shows a canvas with dimensions different from the pixel dimensions of its content.
* [Multiple values and languages][0006] (v3) demonstrates language map variations, for multiple values and multiple languages.

{% include acronyms.md %}
{% include links.md %}
