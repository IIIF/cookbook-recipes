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

Other recipes like [Simple Annotation — Tagging](https://iiif.io/api/cookbook/recipe/0021-tagging/) or [Simplest Annotation](https://iiif.io/api/cookbook/recipe/0266-full-Canvas-annotation/) add the Annotation to the `annotations` list of the Canvas targetting the `id` of the Canvas itself. 
In this example, we will write the Annotation as part of the [contentresources](https://iiif.io/api/presentation/3.0/#57-content-resources) associated with the Canvas adding an Annotation Page with an Annotation inside the `annotations` list of the 
contentresources. 
This is the preferred solution rather than adding the Annotation in the `annotations` field of the Canvas.

To target a specific image (and not the whole Canvas) the `target` of the Annotation must be the `id` of the image, not the `id` of the `service`. 

For annotating a part of the image we use the [media fragment selector](https://www.w3.org/TR/annotation-model/#fragment-selector) (e.g. `#xywh=50,50,640,480`) that is concatenated after the `target` string. It is worth noting that the fragment is pointing to a part of the image not to the Canvas.

Some visualizers might choose to render only the Annotation of the active content resource or to allow to group the Annotations based on the content resource they are targeting. 

## Restrictions
None known.

## Example
The example is based on the recipe [Multiple Choice of Images in a Single View (Canvas)][0033]. In this case, we want to annotate the skulls on the floor that are visible only on the X-ray image. We create an Annotation pPage with an Annotation. We want to tag only a portion of the image and thus the `motivation` of the Annotation must be `tagging`. The `body` of the Annotation must be a `TextualBody` — with a format of `text/plain` — that contains the text of our Annotation.
The `target` of the Annotation will be the `id` of the image followed by the fragment containing the coordinates of the region of interest `#xywh=810,900,260,30`.

Credit: John Dee performing an experiment before Queen Elizabeth I. Oil painting by Henry Gillard Glindoni. Credit: Wellcome Collection. Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="65-84"' %}

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

