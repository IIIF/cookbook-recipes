---
title: Using Annotation Collections
id: 309
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
topic: 
 - basic
---

## Use Case

You have a large number of Annotations covering multiple Canvases in a Manifest, for example crowd-sourced transcriptions or the output from a layout analysis algorithm and you want the Annotations to be displayed in a viewer as a recognizable group over the document with a label and a common color.

## Implementation Notes

The [IIIF Presentation API 3](https://iiif.io/api/presentation/3.0/#58-annotation-collection) defines the AnnotationCollection as a mechanism to represent groupings of AnnotationPages that should be managed as a single whole, regardless of which Canvas or resource they target. The AnnotationCollection is a separate document that references a chain of one or more separate AnnotationPages containing the Annotations. The AnnotationPages contain a reference to the parent AnnotationCollection and a reference to the next page in the chain.

The AnnotationCollection should have a `label` property that can be shown to the user and it can optionally contain additional properties as specified in the [IIIF Presentation API 3](https://iiif.io/api/presentation/3.0/#a-summary-of-property-requirements). 

The AnnotationCollection has a `first` property that contains the URI of the first AnnotationPage in the sequence, a `last` property that contains the URI of the last AnnotationPage and it should have a `total` property that contains the total number of Annotations in the collection.

The IIIF Manifest requires that Annotations that should be shown on a Canvas are contained in AnnotationPages referenced in the `annotations` property of that Canvas. This means that all Annotations need to be grouped by Canvas and put into one or more AnnotationPages per Canvas. An AnnotationPage can not contain Annotations for more than one Canvas.

The AnnotationPages have an `items` property containing the list of Annotations, a `partOf` property that contains the URI of the parent AnnotationCollection, and a `next` property that contains the URI of the next AnnotationPage in the sequence. AnnotationPages are often separate documents that are [referenced][0269] in the manifest using a reference object that can additionally provide some properties for access inside the manifest.

A IIIF viewer that displays Annotations on a Canvas follows the URIs in the `annotations` property of the Canvas and loads the Annotations in the referenced AnnotationPages. If the viewer wants to indicate that these Annotations belong to one or more AnnotationCollections it has to follow the URI in the `partOf` property of the AnnotationPages to identify the AnnotationCollection and display its label and choose a common color for the Annotations. The indirect connection from the Manifest to the AnnotationCollection means that a viewer would have to load all AnnotationPages from all Canvases if it wants to present a complete list of all AnnotationCollections in the Manifest to the user. This potentially slow process can be avoided if the `partOf` and `next` properties of the AnnotationPages are provided in the reference object inside the Manifest like in the example below. 

## Example

We use a Manifest containing two pages from a newspaper (Berliner Tageblatt, February 16, 1925, from Staatsbibliothek Berlin via Europeana) and a set of Annotations concerning layout and reading order.

The Annotations select rectangular regions on the Canvases in the Manifest and add textual tags describing layout elements. They are contained in two AnnotationPages "anno_p1.json" for Annotations on the first Canvas and "anno_p2.json" for Annotations on the second Canvas. "anno_p1.json" contains a `next` reference to "anno_p2.json" and both pages contain `partOf` references to the AnnotationCollection. 

The AnnotationCollection is in the file "anno_coll.json". It has a `label` and references "anno_p1.json" as the `first` and "anno_p2.json" as the `last` page and contains the `total` number of Annotations.

The AnnotationCollection referencing the AnnotationPages:

{% include jsonviewer.html src="anno_coll.json" %}

The Manifest containing the two Canvases and referencing the AnnotationPages:

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The first AnnotationPage with Annotations on the first Canvas: [anno_p1.json](anno_p1.json)

The second AnnotationPage with Annotations on the second Canvas: [anno_p2.json](anno_p2.json)

## Related Recipes

* [Embedded or Referenced Annotations][0269] for referencing Annotations in external AnnotationPages
* [Simple Annotation — Tagging][0021] annotating a rectangular Canvas region
* [Annotation with a Non-Rectangular Polygon][0261] annotating an irregular shape on a Canvas

{% include acronyms.md %}
{% include links.md %}
