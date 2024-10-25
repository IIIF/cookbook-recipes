---
title: Grouping Annotations into Collections
id: 309
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
topic: 
 - basic
---

## Use Case

You have a large number of Annotations covering multiple Canvases in a Manifest, for example crowd-sourced transcriptions or the output from a layout analysis algorithm, and you want the Annotations to be displayed in a viewer as a recognizable group over the document with a label and a common color.

## Implementation Notes

The [IIIF Presentation API 3](https://iiif.io/api/presentation/3.0/#58-annotation-collection) defines Annotation Collections as a mechanism to represent groupings of Annotation Pages that should be managed as a single whole, regardless of which Canvas or resource they target. The Annotation Collection is a separate document that references a chain of one or more separate Annotation Pages which contain the Annotations. The Annotation Pages contain a reference to the parent Annotation Collection and a reference to the next page in the chain.

The Annotation Collection must have a `type` of "AnnotationCollection" and should have a `label` property that can be shown to the user and it can optionally contain additional properties as specified in the [IIIF Presentation API 3](https://iiif.io/api/presentation/3.0/#a-summary-of-property-requirements). 

The Annotation Collection has a `first` property that contains the URI of the first Annotation Page in the sequence, a `last` property that contains the URI of the last Annotation Page and it should have a `total` property that contains the total number of Annotations in the collection.

The IIIF Manifest requires that Annotations that are intended to be shown on a Canvas are contained in Annotation Pages referenced in the `annotations` property of that Canvas. This means that all Annotations need to be grouped by Canvas and put into one or more Annotation Pages per Canvas. An Annotation Page can not contain Annotations for more than one Canvas.

The Annotation Pages must have a `type` of "AnnotationPage" and have an `items` property containing the list of Annotations, a `partOf` property that contains the URI of the parent Annotation Collection, and `next` and `prev` properties that contain the URIs of the next and previous Annotation Pages in the sequence. Annotation Pages are often separate documents that are [referenced][0269] in the manifest using a reference object that can additionally provide some properties for access inside the manifest.

A IIIF viewer that displays Annotations on a Canvas follows the URIs in the `annotations` property of the Canvas and loads the Annotations in the referenced Annotation Pages. If the viewer wants to indicate that these Annotations belong to one or more Annotation Collections it has to follow the URI in the `partOf` property of the Annotation Pages to identify the Annotation Collection and display its label and choose a common color for the Annotations. The indirect connection from the Manifest to the Annotation Collection means that a viewer would have to load all Annotation Pages from all Canvases if it wants to present a complete list of all Annotation Collections in the Manifest to the user. This potentially slow process can be avoided if the `partOf`, `next`, `prev` properties of the Annotation Pages are provided in the reference object inside the Manifest and also the relevant properties of the Annotation Collection and provided in the `partOf` reference object like in the example below.

## Example

We use a Manifest containing two pages from a newspaper (Berliner Tageblatt, February 16, 1925, from Staatsbibliothek Berlin via Europeana) and a set of Annotations concerning layout and reading order.

The Annotations select rectangular regions on the Canvases in the Manifest and add textual tags describing layout elements. They are contained in two AnnotationPages "anno_p1.json" for Annotations on the first Canvas and "anno_p2.json" for Annotations on the second Canvas. "anno_p1.json" contains a `next` reference to "anno_p2.json", "anno_p2.json" contains a `prev` reference to "anno_p1.json", and both pages contain a `partOf` reference to the AnnotationCollection.

The AnnotationCollection is in the file "anno_coll.json". It has a `label` and references "anno_p1.json" as the `first` and "anno_p2.json" as the `last` page and contains the `total` number of Annotations.

The AnnotationCollection referencing the AnnotationPages:

{% include jsonviewer.html src="anno_coll.json" %}

The first AnnotationPage with Annotations on the first Canvas: [anno_p1.json](anno_p1.json)

The second AnnotationPage with Annotations on the second Canvas: [anno_p2.json](anno_p2.json)

The Manifest containing the two Canvases and referencing the AnnotationPages:

{% include manifest_links.html viewers="" manifest="manifest.json" config='data-line="66-77,121-131"' %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Embedded or Referenced Annotations][0269] for referencing Annotations in external AnnotationPages
* [Simple Annotation - Tagging][0021] annotating a rectangular Canvas region
* [Annotation with a Non-Rectangular Polygon][0261] annotating an irregular shape on a Canvas

{% include acronyms.md %}
{% include links.md %}
