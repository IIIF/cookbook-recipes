---
title: Foldouts, Flaps, and Maps
id: 35
layout: recipe
tags: [images, behavior, non-paged]
summary: "Demonstrates how to model a foldout diagram or map."
viewers:
 - Theseus
 - TIFY
topic: structure
property: behavior
---


## Use Case

Books (and other objects) sometimes include foldout flaps or sheets, such as a map in a historical work. During digitization, the foldout might be captured in both its folded and unfolded state.

In the previous recipe, [Multiple choice of images in a single view][0033], a flap is offered to users as a Choice of images for the same view. But consider this example:

![two images of a map foldout, folded and unfolded](foldout.png)

Here, the page has been captured folded and unfolded. Unlike the example in the previous recipe, these are not the same **view**. There is no one single IIIF Canvas that would serve to represent both of these spatial extents - we can't logically place these two images on the same spatial view.

While the present example and that given in [Multiple choice of images in a single view][0033] are clearly different, the modeling decision may not always be as obvious. There will be cases that could be modeled in either way, depending on what the publisher is trying to present.

## Implementation notes

The unfolded view is simply an additional Canvas in the sequence given by `manifest.items`.

These pages are from a printed, paged book, which might have the `behavior` value of `paged`, so as to generate the correct recto-verso-recto-verso representation in a viewer that supports this behavior. If we insert an additional Canvas into the Manifest's `items`, we will break this sequence unless we introduce an additional `behavior` property on the Canvas with the foldout using the value `non-paged` to indicate that it is not part of the paged sequence.

## Example

This example has been adapted from [https://wellcomelibrary.org/iiif/b29346423/manifest](https://wellcomelibrary.org/iiif/b29346423/manifest) but in a much reduced form to convey the essential points.

The Manifest is given the behavior `paged`. With no other qualifiers, this indicates a left-to-right sequence with the first item _recto_.

The sequence is:

* Front cover
* Inside front cover
* Foldout, folded
* Foldout, unfolded (given the behavior `non-paged`, to indicate that it does not constitute part of the paged sequence of the Manifest)
* Foldout, folded (verso)
* Title page
* Back of title page
* _the normal run of pages would continue here; removed in this Manifest for brevity_
* Inside back cover
* Back Cover

The "non-paged" behavior on Canvases is not yet supported by viewers making this difficult to visualize. The resulting layout in a thumbnail view would look something like this:

![thumbnail layout example with non-paged](layout_example1.jpg)

{% include manifest_links.html viewers="Theseus, TIFY" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="10-12, 134-136"' %}

## Related recipes

* [Multiple choice of images in a single view][0033]
* [Composition of one view from multiple image sources][0036]

{% include acronyms.md %}
{% include links.md %}
