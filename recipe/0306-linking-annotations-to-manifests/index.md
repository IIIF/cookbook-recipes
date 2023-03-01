---
title: Linking external Annotations targeting a Canvas to a Manifest
id: 306
layout: recipe
tags: [annotation, multiple-images]
summary: "Keep a resolvable link between annotations (contained in an external Annotation Page) and the Manifest containing the Canvases they are pointing at."
viewers:
topic: annotation
---

## Use Case
You want to keep a resolvable link between annotations (contained in an external Annotation Page) and the Manifest containing the Canvases they are pointing at.

Usually, annotations in an external Annotation Page point to a Canvas or a Canvas fragment. This can cause problems for annotation consuming viewers as the Canvas identifier doesn't have to resolve. To get the information from a Canvas a viewer needs access to the containing Manifest.

## Implementation Notes

The Annotation Pages stored in an external JSON file contain a list of Annotations.
While often the `target` of the annotations is an URL containing the identifier of the Canvas the `target` can also be a Specific Resource.
The Specific Resource can have a `source` attribute containing the `id` pointing at the Canvas identifier and a `partOf` attribute pointing at the Manifest.
Hence, the `partOf` attribute will contain the Manifest identifier in the `id` attribute, while the `type` attribute will be "Manifest".

## Restrictions
There is usually no advantage in using `partOf` attribute for pointing at Manifest with Annotations contained in a Manifest. In this case, it is implicit that they are about the Manifest containing them.


## Example
The example is based on the recipe [Embedded or referenced Annotations][0269].

However, the `target` of the Annotation contained in the Annotation Page file will be a Specific Resource this allows us to use a `partOf` attribute inside the `source` element to point at the original Manifest containing the Canvas. The `partOf` `id` attribute is the resolvable link of the Manifest.

In the example, it is also shown the usage of the `selector` attribute of the Specific Resource that allows us to select a region of the image using the `value` attribute of the Fragment Selector.
The `value` attribute follows the Fragment Selector syntax [Fragment Selectors][0020].

Annotation Page file
{% include manifest_links.html viewers="Annona" manifest="annotationpage.json" %}

{% include jsonviewer.html src="annotationpage.json" config='data-line="16-33"' %}

Manifest file
{% include manifest_links.html viewers="Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="44-49"' %}

## Related Recipes

* [Embedded or Referenced Annotations][0269] an Annotation Page without links to the original Manifest.
* [Annotate specific images or layers][0326] Specific Resource used for annotating specific images or layers.
* [Simple Annotation — Tagging][0021] for an Annotation using a Fragment Selector.
* [Fragment Selectors][0020] for understanding how to use a Fragment Selector.

{% include acronyms.md %}
{% include links.md %}

