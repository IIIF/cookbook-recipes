---
title: Visible Text Resource on a Canvas
id: 561
layout: recipe
tags: annotation
summary: "Overlaying (painting) text on top of an image resource"
viewers:
topic:
 - realWorldObject
---

## Use Case

You would like to add text visibly over some portion of a IIIF image resource without making a derivative of the original image and retaining its deep zoom possibilities.

## Implementation Notes

This recipe aims to show the simplest form of a combination that is more likely to be used in combination with other IIIF recipes. For example, it forms a part of the [Multimedia Canvas][0489] recipe.

Though the implementation is not complex, the implications get well into the nuances of IIIF. Making a textual annotation visible is the consequence of using a `motivation` value of `painting` on an Annotation in combination with placing that Annotation as an item inside an Annotation Page instead of as part of an `annotations` section. Making these two changes tells a client to display the text directly instead of separating it as an annotation to be handled in the client's manner of showing those. The Presentation API 3.0 states clearly that
+ Annotations in an `annotations` section are not permitted to have the `motivation` value `painting` ([Annotations](https://iiif.io/api/presentation/3.0/#annotations))
+ Conversely, Annotations referenced in `items` must have the `motivation` value `painting`. ([Canvas](https://iiif.io/api/presentation/3.0/#53-canvas))
+ Finally, content to be rendered must be in an Annotation with the `motivation` value `painting`. ([Motivation values](https://iiif.io/api/presentation/3.0/#values-for-motivation) and [Canvas](https://iiif.io/api/presentation/3.0/#53-canvas))

Styling text or using HTML in text painted onto a Canvas is possible, but the options are limited. In addition, styling added to a manifest may be unreliable across viewers. For one example, since IIIF Canvas dimensions are unit-less, using pixels for text size is valid but may not be interpreted identically by different viewers.

The presentation of resources is upwards in a z-index from the first "painting" Annotation encountered to all subsequent "painting" Annotations. Therefore, for the textual annotation to be visible, it must come later in the manifest order of Annotations than the image resource it marks.

## Restrictions

Markup in the textual annotation is limited for security reasons. Clents are expected to allow only `a`, `b`, `br`, `i`, `img`, `p`, `small`, `span`, `sub`, and `sup` tags, and may remove any or all of those. For more details of permitted and prohibited markup, see [the specification](https://iiif.io/api/presentation/3.0/#45-html-markup-in-property-values).

## Example

In this example, we have a base image showing people in the countryside, one of whom is carrying a wrapped koto. Hypothesizing for our use case that the wrapped koto is less identifiable to people unfamiliar with the scene, there is a textual annotation adjacent to it that indicates it.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}


## Related Recipes

* [Embedding HTML in descriptive properties][0007]
* [Multiple Choice of Images in a Single View (Canvas)][0033] contains additional text about z-index ordering

{% include acronyms.md %}
{% include links.md %}
