---
title: HTML in Annotations
id: 19
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
topic: 
 - basic
---

## Use Case

You want to create an annotation on a Canvas that contains a link or other HTML feature that can not be expressed in plain text. In this recipe we'll discuss the specifics of using HTML in the annotation body, see [Simplest Annotation][0266] for a general description of the annotation structure and an example of a plain text annotation body.

## Implementation Notes

The `body` of an Annotation can be a simple piece of plain text that is embedded in the Annotation as in the [Simplest Annotation][0266] example. It can also be a piece of HTML instead of plain text or it can be a URL pointing to an external HTML document. In the following example we are using an embedded HTML body.

The `body` property of the Annotation is an object with a `type` of `TextualBody` that contains the HTML text in a `value` property and specifies the format `text/html` in a `format` property and optionally the language (e.g. `de` for German) in a `language` property.

[more on html bodies and restrictions]

## Restrictions


## Example

This example Manifest contains an embedded Annotation containing the HTML text "Göttinger Marktplatz mit Gänseliesel Brunnen" with a link to the Wikipedia Article "Gänseliesel-Brunnen (Göttingen)" behind the words "Gänseliesel Brunnen". The Annotation has the motivation `commenting` targeting the whole Canvas. The Annotation is the single content of an Annotation Page contained in the `annotations` property of the Canvas.

{% include manifest_links.html viewers="Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="44-63"' %}


## Related Recipes

* [Simplest Annotation][0266] general description of Annotations and example of a plain text body

{% include acronyms.md %}
{% include links.md %}

