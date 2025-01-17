---
title: Visible Text Annotation
id: 561
layout: recipe
tags: annotation
summary: "Overlaying (painting) visible text on top of an image resource"
viewers:
topic:
 - realWorldObject
---

## Use Case

You have an 

## Implementation Notes

This recipe aims to show the simplest form of a combination that is more likely to be used in combination with other IIIF recipes. For example, it forms a part of the [Multimedia Canvas] recipe.

Fundamentally, what it is showing is the importance of the `motivation` property on an annotation, in combination itself with making that annotation directly inside a Canvas resource instead of as part of an `annotations` section. Making these two changes tells a viewer to display the text directly instead of separating it as an annotation to be handled in the viewer's manner of showing those.

Styling text or using HTML in text painted onto a Canvas is possible, but the options are limited. 

## Restrictions

For security reasons, clients are expected to allow only `a`, `b`, `br`, `i`, `img`, `p`, `small`, `span`, `sub`, and `sup` tags in the textual annotation, and may remove any or all of those. For more details of permitted and prohibited markup, see [the specification](https://iiif.io/api/presentation/3.0/#45-html-markup-in-property-values).

## Example

In this example, we have a base image showing people in the countryside, one of whom is carrying a wrapped koto. Hypothesizing for our use case that the wrapped koto is less recognizable to people unfamiliar with the scene, there is a textual annotation adjacent to it that identifies it.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Embedding HTML in descriptive properties][0007]
* [Image Rotation Two Ways][0040] to see an example of using a CSS class for style manipulation

{% include acronyms.md %}
{% include links.md %}
