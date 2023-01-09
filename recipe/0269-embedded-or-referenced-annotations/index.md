---
title: Embedded or referenced Annotations
id: 269
layout: recipe
tags: [tbc]
summary: "Annotations can be embedded in the manifest or referenced from external URIs."
topic: annotation
viewers:
 - Mirador
 - Annona
---

## Use Case

You would like to use a large number of Annotations but store them separately to make sure the Manifest does not become too big.

## Implementation Notes

Annotations for a Canvas are stored in the `annotations` property of the Canvas in the form of an Annotation Page object containing a list of Annotation objects conforming to the [W3C Web Annotation](https://www.w3.org/TR/annotation-model/) data model.

The Annotation Page and the Annotations can either be embedded in the Manifest (as in the [Simplest Annotation][0266] example) or referenced (as in the example below) by storing the Annotation Page in a separate document and putting the URI of this document in the Manifest.

An advantage of separating the Manifest and the Annotations is that the Manifest can be a smaller document that loads faster so that the viewer can start to display its contents quicker and additionally decide if and when to load the Annotations for a Canvas depending on user interactions and the current view. 

Embedded Annotations, on the other hand, have the advantage that the viewer does not have to make additional HTTPS requests so the Annotations can be displayed quicker. Viewers should treat embedded and referenced Annotations the same but the [IIIF Presentation API 3](https://iiif.io/api/presentation/3.0/#56-annotation) mentions that a viewer should process Annotations in the order given in the Manifest and a publisher may order embedded Annotation Pages before referenced pages to expedite their processing.

External Annotation Pages are referenced in the `annotations` property of the Canvas by a reference object with an `id` property containing the URI of the external document and a `type` property containing "AnnotationPage". The reference object cannot contain an `items` property.

The external Annotation Page document must have:
- a `@context` property containing "http://iiif.io/api/presentation/3/context.json"
- an `id` property with its URI
- a `type` of "AnnotationPage"
- and an `items` property containing the list of Annotations.

Each Annotation in the Annotation Page must have an `id` property with a unique identifier, a `type` of "Annotation", a `target`, and a `body`. The `target` of all Annotations should be the URI of the Canvas that contains the reference to the Annotation Page (see [IIIF Presentation API 3](https://iiif.io/api/presentation/3.0/#55-annotation-page)). This means that there should be one Annotation Page document (or multiple) for each Canvas that you want to annotate.

The `target` of the Annotation can be just the URI of the Canvas if you want to annotate the full canvas as in [Simplest Annotation][0266], or the URI with a media fragment at the end if you want to annotate a region of the Canvas as in [Simple Annotation — Tagging][0021], or a more complex selector as in [Annotation with a Non-Rectangular Polygon][0261]. 

The `body` can be a URI or a more complex object following the [W3C Web Annotation specification](https://www.w3.org/TR/annotation-model/#bodies-and-targets'). A commonly used model is the Embedded Textual Body as in the example below.


## Example

This example Manifest contains a referenced Annotation containing the text “Göttinger Marktplatz mit Gänseliesel Brunnen” with the motivation `commenting` targeting the whole Canvas. The Annotation is the single item of an Annotation Page contained in the additional Annotation Page file which is referenced in the `annotations` property of the Canvas.

The `body` of the Annotation is an object with a `type` of "TextualBody" that contains the text in a `value` property and specifies the format of the text string ("text/plain") in a `format` property and the language ("de" for German) in a `language` property.

The `target` of the Annotation is just the URI of the Canvas so the Annotation refers to the full Canvas.

The rendering of this referenced Annotation should be virtually indistiguishable from the embedded Annotation in [Simplest Annotation][0266]. Please note that Mirador does not put a highlight on the image when you mouse over the Annotation in the sidebar because the Annotation targets the Canvas as a whole.

### Manifest file

{% include manifest_links.html viewers="Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="44-49"' %}

### Annotation Page file

{% include manifest_links.html viewers="Annona" manifest="manifest.json" annotationurl="annotationpage.json" %}

{% include jsonviewer.html src="annotationpage.json" %}

## Related Recipes

* [Simplest Annotation][0266] for a simple embedded Annotation that annotates a full Canvas
* [Simple Annotation — Tagging][0021] annotating a rectangular Canvas region
* [Annotation with a Non-Rectangular Polygon][0261] annotating an irregular shape on a Canvas


{% include acronyms.md %}
{% include links.md %}

