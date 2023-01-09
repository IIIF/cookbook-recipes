---
title: Simplest Annotation
id: 266
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
 - Mirador  
 - Annona
topic: annotation
---

## Use Case

You want to annotate a canvas with some text either as a comment or a tag. In this recipe we are annotating the full Canvas but see [Simple Annotation — Tagging][0021] or [Annotation with a Non-Rectangular Polygon][0261] if you would like to target a specific part or region of the Canvas.

## Implementation Notes

Annotations for a Canvas are stored in the `annotations` property of the Canvas in the form of an Annotation Page object containing a list of Annotation objects conforming to the [W3C Web Annotation](https://www.w3.org/TR/annotation-model/) format.

The Annotation Page and the Annotations can either be embedded in the manifest (as in the example below) or referenced by providing just the URI of the external document containing the Annotation Page (see [Embedded or Referenced Annotations][0269]).

The Annotation Page object must have the `type` `AnnotationPage`, an `id` property containing a unique URI (that does not have to resolve), and an `items` property containing a list with one or more Annotations.

The Annotations must have the `type` `Annotation`, and a `body` property that contains the text of the comment or tag. The body itself can be an object with a `type` of `TextualBody` that contains the text in a `value` property and specifies the format of the text string (e.g. `text/plain`) in a `format` property and the language (e.g. `de` for German) in a `language` property.

The Annotations must have a `target` property that for a full Canvas Annotation contains only the URI of the Canvas and no additional fragments or selectors.

The Annotations should have a `motivation` property that can contain different values specifiying the purpose of the Annotation. The W3C Web Annotation specification has a [full list of motivations](https://www.w3.org/TR/annotation-model/#model-12). Commonly used values are `commenting` and `tagging`. Be careful when using other motivations, IIIF viewers may only display Annotations with certain motivations.

## Restrictions

The semantic of annotating the full Canvas as a whole can be specified by either using the Canvas URI without fragment or selector as in this example or by using a selector that selects the full area of the Canvas (see [Simple Annotation — Tagging][0021] for a simple example of how to use a fragment selector). Using a selector that selects the full Canvas area is a more universal pattern and may be better supported by IIIF clients.

## Example

This example Manifest contains an embedded Annotation containing the text "Göttinger Marktplatz mit Gänseliesel Brunnen" with the motivation `commenting` targeting the whole Canvas. The Annotation is the single content of an Annotation Page contained in the `annotations` property of the Canvas.

{% include manifest_links.html viewers="Mirador,Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="44-63"' %}

## Related Recipes

* [Simple Annotation — Tagging][0021] for an Annotation using a fragment selector
* [Annotation with a Non-Rectangular Polygon][0261] for an Annotation using a SVG selector
* [Simplest Manifest - Image][0001]
* [Simplest Manifest - Audio][0002]
* [Simplest Manifest - Video][0003]
* [Embedded or Referenced Annotations][0269]


{% include acronyms.md %}
{% include links.md %}

