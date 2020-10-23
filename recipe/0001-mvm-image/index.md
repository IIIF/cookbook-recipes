---
title: Simplest Manifest - Single Image File
id: 1
layout: recipe
tags: [image, presentation]
summary: "The simplest viable manifest for image content. If all you have for an object is one image on the web and a label, this pattern turns it into a IIIF Presentation resource."
---


## Use Case

The simplest viable manifest for image content. If all you have for an object is one image on the web and a label to go along with it, this pattern turns it into a IIIF Presentation resource. If you would like to enable deep zooming, you will need to use a IIIF Image server. For this, see the [Support Deep Viewing with Basic Use of a IIIF Image Service][0005] recipe.

## Implementation Notes

This illustrates the mandatory structure and properties of a manifest, with the simplest possible content. 

The JSON-LD opens with the `@context` declaration, which identifies the terms used in the document as belonging to the IIIF specification. The `id` property identifies this manifest with the URL at which it is available online. The `type` property must be `Manifest`. The `label` property is mandatory, and the language of its value must be given (or the special value `none`), using a [language map][prezi3-languages]. Here the language of the label is English and its value is "Single Image Example". The manifest's `items` property is a list of canvases. In this example there is only one canvas, with a `height` of 1800 and a `width` of 1200. These units have no dimension: they establish a coordinate space that in this case the single image will fill. The canvas's `id` property is used later as the `target` of the annotation that links to the single image. 

The `items` property of the Canvas is a list of annotation pages, in this case there is only one page. The `items` property of the annotation page is a list of annotations, in this case there is only one annotation. This annotation is what links the image resource with the canvas. The `body` of the annotation is an image, the url of which is the `id` property of the body. The dimensions of the image, in pixels, are given and here match the canvas dimensions exactly. The `target` property tells us that the image is associated with the entirety of the canvas, and the `motivation` property of `painting` tells us that a client should render the image to fill the canvas.

## Restrictions

This recipe is not for large images or deep zoom functionality. For this, see the [Support Deep Viewing with Basic Use of a IIIF Image Service][0005] recipe.

## Example

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

# Related Recipes

* [Simplest Manifest - Audio][0002] and [Simplest Manifest - Video][0003] are equivalent to this example but for other media.
* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005] shows a basic manifest for use with a IIIF Image server.
* [Image different size to canvas][0004] shows a canvas with dimensions different from the pixel dimensions of its content.
* [Multiple values and languages] demonstrates language map variations, for multiple values and multiple languages. 


{% include acronyms.md %}
{% include links.md %}
