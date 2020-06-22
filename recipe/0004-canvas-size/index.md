---
title: Image with Different Size from Canvas
id: 4
layout: recipe
tags: [image, presentation, canvas]
summary: "Demonstrates that an image size (in pixels) need not be the same as the Canvas dimensions (width and height)"
---

## Use Case

You have an image ready for annotating that is expected to be replaced later by a higher resolution image. You would like to provide a sufficiently high-resolution coordinate space to position the annotations precisely. IIIF Presentation v3.0 allows you to describe a canvas with the dimensions of the larger image to come, fill it with the smaller image you have ready now, and capture annotations on the smaller image in confidence that they will be positioned appropriately on the larger image when it is swapped in.

The canvas dimensions (unit-less values of width and height) need not be related to the (pixel) dimensions of the image content painted onto the canvas. This recipe shows the canvas dimensions differing from the image dimensions and the image filling the canvas completely.

## Implementation notes

This recipe demonstrates that it is important to think about the canvas as a coordinate space, not as absolute pixel or display dimensions. It can be thought of as a precursor to having multiple images on the same canvas, each with a different resolution but to be reconciled into the same canvas coordinate space.

By making the canvas coordinate space larger than the image pixel space, integer-based annotation coordinates will be easier to implement. Thus, if the image height or width is less than about 1000 pixels, the canvas height or width should probably be doubled.

## Restrictions

None known.

## Example

This example shows a Manifest with a single Canvas that has height and width dimensions double the pixel size of the image, as the image height and width are each less than 1000 pixels.

{% include jsonviewer.html src="manifest.json" config="data-line='14-15,29-30'"%}

# Related recipes

* [Simple Image Manifest][0001]
* [Multi Image Multi Choice][0037]
* [Image Gallery][0058]

{% include acronyms.md %}
{% include links.md %}
