---
title: Linking an annotation targeting a canvas to the Manifest
id: 306
layout: recipe
tags: [annotation, multiple-images]
summary: "Keep a resolvable link between annotations—contained in an external AnnotationPage—and the Manifest containing the Canvases they are pointing at."
viewers:
topic: annotation
---

## Use Case
You want to keep a resolvable link between annotations—contained in an external AnnotationPage—and the Manifest containing the Canvases they are pointing at.

Usually, annotations point to a Canvas or Canvas fragment. This can cause problems for annotation consuming viewers as the Canvas identifier doesn't have to resolve. To get the information from a Canvas a viewer needs access to the containing Manifest.

## Implementation Notes

The AnnotationPages stored in an external JSON file contain a list of Annotations.
While often the `target` of the annotations is an URL containing the identifier of the Canvas the `target` can also be a `SpecificResource`.
The `SpecificResource`  can have a `source` attribute containing the `id` pointing at the Canvas identifier and a `partOf` attribute pointing at the Manifest.
Hence, the `partOf` attribute will contain the Manifest identifier in the `id` attribute, while the `type` attribute will be `"Manifest"`.

## Restrictions
There is usually no advantage in using `partOf` attribute for pointing at Manifest with Annotations contained in a Manifest. In this case, it is implicit that they are about the Manifest containing them.


## Example
The example is based on the recipe [Embedded or referenced Annotations][0269].

However, the `target` of the Annotation contained in the AnnotationPage file will be a `SpecificResource` this allows us to use a `partOf` attribute inside the `source` element to point at the original Manifest containing the Canvas. The `partOf` `id` attribute is the resolvable link of the Manifest.

In the example, it is also shown the usage of the `selector` attribute of the `SpecificResource` this allows us to select a region of the image using the FragmentSelector `value` attribute.
The `value` attribute follows the FragmentSelector syntax [Fragment Selectors][0020].

Annotation Page file
{% include manifest_links.html viewers="Annona" manifest="manifest.json" annotationurl="annotationpage.json" %}

{% include jsonviewer.html src="annotationpage.json" %}

Manifest file
{% include manifest_links.html viewers="Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="44-49"' %}

## Related Recipes

* [Embedded or Referenced Annotations][0269] an AnnotationPage without links to the original Manifest.
* [Annotate specific images or layers][0326] SpecificResource used for annotating specific images or layers.
* [Simple Annotation — Tagging][0021] for an Annotation using a fragment selector
* [Fragment Selectors][0020] for understanding how to use a FragmentSelector.
* [Full Canvas annotation][0266] for a simple annotation of the whole Canvas.
* [Annotation with a Non-Rectangular Polygon][0261] for an Annotation using an SVG selector


{% include acronyms.md %}
{% include links.md %}

