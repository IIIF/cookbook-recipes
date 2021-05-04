---
title: Choice: Multispectral-flavored Example, with Image Service
id: 34
layout: recipe
tags: [multiple-images]
summary: "How to model multiple choices of images for the same view - e.g., layers, multispectral images - with image services."
---


## Use Case

This recipe is identical to the previous recipe, [Multiple choice of images in a single view][0033], except that the provided example includes IIIF Image API Services for the image choices.

## Implementation notes

Please refer to [Multiple choice of images in a single view][0033] for the full discussion. For the full discussion on using a IIIF Image Service, see [Support Deep Viewing with Basic Use of a IIIF Image Service][0005].

## Example

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="25-67"' %}

## Related recipes

* [Multiple choice of images in a single view][0033]. This is the same as this example, but without the image service (only static images are used).
* [Foldouts, Flaps and Maps][0035]. In the example above, `Choice` is appropriate because the two images are the same view and are aligned. For, say, a map in a book that folds out to a much bigger view, the unfolded version would be a different `Canvas`, because it does not represent the same spatial view. This is one reason to offer two separate views rather than a choice of resources within one view.
* [Composition of one view from multiple image sources][0036]. Care should be taken not to confuse _composition_ with the current recipe. Both involve multiple images, but composition is for building a scene from multiple images (and possibly other resources), where there is no requirement to offer the user choices _between_ those images.

{% include acronyms.md %}
{% include links.md %}
