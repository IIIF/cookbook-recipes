---
title: Multiple choice of images in a single view
id: 33
layout: recipe
tags: [multiple-images]
summary: "How to model multiple choices of images for the same view - e.g., layers, multispectral images."
---


## Use Cases

There are multiple images available for a given View (Canvas). For example, a painting has been photographed in 10 different wavelengths of light. The images are _registered_ - that is, they all line up.

![](http://www.webexhibits.org/pigments/i/intro/examine/imaging.jpg)

_<small>[http://www.webexhibits.org/pigments/intro/](http://www.webexhibits.org/pigments/intro/)<br/>
TODO: This needs to be replaced by an image with clear reuse rights.</small>_

Another example would be a manuscript page with a flap or foldout; there are two registered images of the page available, one with the flap closed and one with it open. The page also has a transcription which is independent of either of these two images, because the annotations target the canvas.

![](choice-flap.png)

_<small>Wellcome Library</small>_

In both cases the images are all of the same thing. They all align (or could be aligned) with the same Canvas.

Users should be able to choose which of the multiple images they want to view.

Client implementations should understand that the intent is to offer the user a **choice** between 2 or more images. The user can switch between them at will, but the publisher can expect that clients will all start with the same image showing.

There are many potential user interface approaches for this model. For example, a tool used in the study of art conservation may have more sophisticated layer blending features or other manipluations of the images.

This pattern is important because it is not uncommon, especially for artworks, to have more than one image availble for the same View.

This recipe should not be used if the images make up multiple parts of the scene, where the intention is to display them together. For example, a digital reconstruction of parts of a manuscript page. In that scenario the intent is not to offer the user a choice of alternative views of the same thing, it is to build an overall view from multiple source images. This scenario is covered by the recipe [Composition of one view from multiple image sources](../0036-composition-from-multiple-images/).  

## Implementation notes

The implementation is the same as the [simplest IIIF use case](../0001-mvm-image/), except that the body of the annotation isn't an image resource directly, but a resource of type `Choice`. This is defined in the W3C Web Annotation Data Model:

> A Choice has an ordered list of resources from which an application should select only one to process or display. The order is given from the most preferable to least preferable, according to the Annotation's creator or publisher.

_from [Choice between bodies](https://www.w3.org/TR/annotation-model/#choice-between-bodies)._

The multiple images are now values of the `Choice` body.

This pattern may be used in conjunction with [Composition of one view from multiple image sources](../0036-composition-from-multiple-images/). A Canvas could have multiple sources composing the scene, one or more of which might be choices.


## Restrictions

Publishers should consider target viewing environments and clients when providing complex views of this nature.

Not all IIIF clients will recognise Choice. A very simple thumbnail strip viewer, for example, would not be able to offer a user interface for the required human choice (but should still just show the first image).

Clients need to consider generalised handling of multiple choices and multiple resources.
Clients that don't wish to offer a Choice UI should at least understand the construction and just take the first.

## Example

[JSON-LD](manifest.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```

# Related recipes

* [Choice with Image Services](../0034-choice-with-image-services/). This is the same as this example, but each of the two images is accompanied by an image service.
* [Foldouts](../0035-foldouts/). In the manuscript page example shown in the pictures on this page, `Choice` is appropriate because the two images are the same view and are aligned. For a large map that folds out to a much bigger view, the unfolded version would be a different Canvas, because it does not represent the same spatial view. This is one reason to offer two separate views rather than a choice of resources within one view.
* [Composition of one view from multiple image sources](../0036-composition-from-multiple-images/). Care should be taken not to confuse _composition_ with the current recipe. Both involve multiple images, but composition is for building a scene from multiple images (and possibly other resources), where there is no requirement to offer the user choices _between_ those images.


{% include acronyms.md %}
{% include links.md %}

