---
title: Full Canvas Annotation
id: 266
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

I want to annotate the full canvas as a whole and add a comment or a tag.

## Implementation Notes

Annotations for a canvas are stored in the `annotations` property of the canvas in the form of an AnnotationPage containing a list of Annotation objects conforming to the [W3C Web Annotation](https://www.w3.org/TR/annotation-model/) format.

The AnnotationPage and the Annotations can either be embedded in the manifest (as in the example below) or referenced by providing just the URI of the external document containing the AnnotationPage.

The Annotations must have a `body` property that contains the text of the comment or tag. The body itself can be an object with a `type` of `TextualBody` that contains the text in a `value` property and specifies format and language in `format` and `language` properties.

The Annotations must have a `target` property that contains only the URI of the Canvas and no additional fragments or selectors.

The Annotations have a `motivation` property that can contain different values specifiying the purpose of the annotation. Common values are `commenting` and `tagging`. Be careful when using other motivations, IIIF viewers may only display annotations with certain motivations.

## Restrictions

The semantic of annotating the full canvas as a whole can be specified by either using the canvas URI without fragment or selector as in this example or by using a selector that selects the whole canvas (see recipe 260 ???). Using a selector that selects the whole canvas is a more universal pattern and may be better supported by IIIF clients.

## Example

This example manifest contains an embedded annotation containing the text "Göttinger Marktplatz mit Gänseliesel Brunnen" with the motivation "commenting" targeting the whole canvas. The Annotation is the single content of an AnnotationPage contained in the `annotations` property of the Canvas.

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* 260 Simple Commenting Annotation (with fragment)

{% include acronyms.md %}
{% include links.md %}
