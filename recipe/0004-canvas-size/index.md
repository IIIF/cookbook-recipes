---
title: Image with Different Size from Canvas
id: 4
layout: recipe
tags: [image, presentation, canvas]
summary: "Demonstrates that an image size (in pixels) need not be the same as the Canvas dimensions (width and height)"
---



## Use Case

You have a very small image that you hope to later replace by a higher resolution image, but want to capture some annotations on the content. You would like to provide a sufficiently high resolution coordinate space to precisely position the annotations.

The canvas dimensions (width, height) need not be related to the dimensions of the image content painted onto the canvas. This example shows the canvas dimensions differing from the image dimensions even though the image completely fills the canvas.

## Implementation notes

This recipe demonstrates that it is important to think about the canvas as a coordinate space, not as absolute pixel or display dimensions. This is a precursor to when there are multiple images on the same canvas, which have different resolutions but should be reconciled into the same coordinate space of the canvas. 

By making the canvas coordinate space larger than the image pixel space, integer based annotation coordinates will be easier to implement. Thus if the height or width is less than about 1000 pixels, the canvas height or width should probably be doubled.

## Restrictions

None known.

## Example

This example shows a Manifest with a single Canvas that has a height and width which is double the size of the image, as the image height and width are less than 1000 pixels.

{: .line-numbers data-src="manifest.json" }
```json
```

# Related recipes

* [Simple Image Manifest][0001]

{% include acronyms.md %}
{% include links.md %}
