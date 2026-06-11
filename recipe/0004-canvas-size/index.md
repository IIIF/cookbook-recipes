---
title: Image and Canvas with Differing Dimensions
id: 4
layout: recipe
tags: [image, presentation, canvas]
summary: "Demonstrates that image dimensions (pixels) need not be the same as the Canvas dimensions (unit-less)"
viewers:
 - UV
 - Mirador
 - Annona
 - Theseus
 - Curation
 - TIFY
topic: image
code:
 - iiif-prezi3
---

## Use Case

You have an image ready for annotating that is expected to be replaced later by a higher resolution image. You would like to provide a sufficiently high-resolution coordinate space to position the annotations precisely. IIIF Presentation v3.0 allows you to describe a Canvas with the dimensions of the larger image to come, fill it with the smaller image you have ready now, and capture annotations on the smaller image in confidence that they will be positioned appropriately on the larger image when it is swapped in.

## Implementation notes

This recipe demonstrates the importance of thinking about a Canvas as a coordinate space, not as absolute pixel or display dimensions. The Canvas dimensions (unit-less values of width and height) need not be related to the (pixel) dimensions of the content painted onto the Canvas. This recipe shows the Canvas dimensions differing from the image dimensions, yet the image fills the Canvas completely. A more complex but not uncommon case (with a recipe linked below in Related Recipes) is to have multiple images on the same Canvas, where each image might have a different pixel-based resolution but must be reconciled into the same Canvas coordinate space.

By making the Canvas coordinate space larger than the pixel space of an image:
+ You have the leeway to not know what your replacement image dimensions will be,
+ Annotations made on the current version will have consistent locations on the larger image, and
+ Drawing annotation regions on the smaller version will be facilitated by having more screen space.

For a future replacement image of unknown dimensions, a good starting point is to make each Canvas dimension at least twice the corresponding pixel dimension of the current image as long as each Canvas dimension is over 1000.

Finally, if the image dimensions are larger than the Canvas, the image will be scaled to fit the Canvas.

## Restrictions

The aspect ratio should be consistent between your source image and Canvas. Otherwise, you'll see unpredictable stretching and/or distorting.

## Example

This example shows a Manifest with a single Canvas that has height and width dimensions three times the pixel dimensions of the image in order to construct a Canvas with both dimensions greater than 1000px.

{% include manifest_links.html viewers="UV, Mirador, Annona, Theseus, Curation, TIFY" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config="data-line='14-15,29-30'"%}

# Related recipes

* [Simple Image Manifest][0001]
* [A/V Content and the Behavior Property][0000]

{% include acronyms.md %}
{% include links.md %}
