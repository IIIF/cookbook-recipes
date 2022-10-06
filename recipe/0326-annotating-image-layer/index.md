---
title: Annotate specific images or layers
id: 326
layout: recipe
tags: [annotation, multiple-images, layers]
summary: "Annotate a single image or layer when more than one image is present on the Canvas."
viewers:
topic: annotation
---

## Use Case
An Annotation might be specific to a single image or a part of an image rather than
the whole Canvas. For instance, you might want to annotate a painting detail that is only visible on a specific image of a multi-spectral set of images.

![Illustration of the concept of annotating a specific layer of a multi-spectral stack.](layerannotation.png)

Furthermore, if you are analyzing a complex multi-layer image you might want to group the Annotations linked to a layer together and keep them embedded. 

## Implementation Notes
The [Web Annotation Model ](https://www.w3.org/TR/annotation-model/#introduction)
specifies that:

> Typically, an Annotation has a single Body, which is a comment or other descriptive resource, and a single Target that the Body is somehow "about".

Other recipes like [Simple Annotation — Tagging](https://iiif.io/api/cookbook/recipe/0021-tagging/) or [Simplest Annotation](https://iiif.io/api/cookbook/recipe/0266-full-canvas-annotation/) add the Annotation to the `annotations` list of the Canvas targetting the `id` of the Canvas itself. 
In this example, we will write the Annotation as part of the [content resources](https://iiif.io/api/presentation/3.0/#57-content-resources) associated with the Canvas adding an Annotation Page with an Annotation inside the `annotations` list of the `service` attribute of
content resources. 

This is the preferred solution rather than adding the Annotation in the `annotations` field of the Canvas. Doing so if the Annotation is dereferenced all the relevant information will be embedded in the Annotation.

For annotating a part of the image the Annotation will target a SpecificResource resource with an [Image API selector](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector) specifying the region of interest.

Some visualizers might choose to render only the Annotation of the active content resource or to allow to group the Annotations based on the content resource they are targeting. 

## Restrictions
This recipe is valid only for images served using a IIIF service.
When the max image size might vary depending on the image server configurations, to ensure that the Annotation targets the intended region of the image, the ImageAPI selector should provide the `size` attribute with the width and height of the image in the form `w,h`.

## Example
The example is based on the recipe [Multiple Choice of Images in a Single View (Canvas)][0033]. In this case, we want to annotate the skulls on the floor that are visible only on the X-ray image. Within the Service `annotations` attribute we create an Annotation Page with an Annotation. We want to tag only a portion of the image and thus the `motivation` of the Annotation must be tagging. The `body` of the Annotation must be a `TextualBody` — with a format of text/plain — that contains the text of our Annotation. The `target` of the Annotation is a SpecificResource with `source` assigned to the `id` of the Service used for serving the image to be annotated. The region of interest is specified in the `selector` arttribute that is an `ImageApiSelector` with `region` attribute assigned to the region of interest (810,900,260,30 in this case).

Credit: John Dee performing an experiment before Queen Elizabeth I. Oil painting by Henry Gillard Glindoni. Credit: Wellcome Collection. Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="63-90"' %}

## Related Recipes

* [Multiple Choice of Images in a Single View (Canvas)][0033] for the original example without annotations.
* [Simple Annotation — Tagging][0021] for an Annotation using a fragment selector
* [Full Canvas annotation][0266] for a simple annotation of the whole Canvas.
* [Annotation with a Non-Rectangular Polygon][0261] for an Annotation using an SVG selector
* [Simplest Manifest - Image][0001]
* [Composition from multiple images][0036] another approach for building multi-layer Canvases 
* [Embedded or Referenced Annotations][0269]

{% include acronyms.md %}
{% include links.md %}

