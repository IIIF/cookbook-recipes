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

You have a large number of Annotations covering multiple Canvases in a Manifest that should be displayed in a viewer ideally as a recognizable group like a colored layer over the document.

## Implementation Notes

The [IIIF Presentation API 3](https://iiif.io/api/presentation/3.0/#58-annotation-collection) presents the AnnotationCollection to represent groupings of Annotation Pages that should be managed as a single whole, regardless of which Canvas or resource they target. The AnnotationCollection is a separate document that references one or more AnnotationPages containing the Annotations. The AnnotationPages contain a reference to the parent AnnotationCollection. 

A large collection can be divided into multiple pages. The AnnotationCollection contains references to the first and last AnnotationPage and each AnnotationPage contains a reference to the next page in the chain.

The AnnotationCollection should have a `label` property that can be shown to the user and it can optionally contain additional properties as specified in the [IIIF Presentation API 3](https://iiif.io/api/presentation/3.0/#a-summary-of-property-requirements). 

The AnnotationCollection has a `first` property that contains the URI of the first AnnotationPage in the sequence, a `last` property that contains the URI of the last AnnotationPage and it should have a `total` property that contains the total number of Annotations in the collection.

The IIIF Manifest requires that Annotations that should be shown on a Canvas are contained in AnnotationPages referenced in the `annotations` property of that Canvas. This means that all Annotations need to be grouped by Canvas and put into one or more AnnotationPages per Canvas. An AnnotationPage can not contain Annotations for more than one Canvas.

All AnnotationPages are separate documents that have an `items` property containing the list of Annotation objects and a `partOf` property that contains the URI of the parent AnnotationCollection and a `next` property that contains the URI of the next AnnotationCollection in the sequence.

A IIIF viewer that displays Annotations on a Canvas follows the URIs in the `annotations` property of the Canvas and loads the Annotations in the referenced AnnotationPages. If the viewer wants to indicate that these Annotations belong to one or more AnnotationCollections it has to follow the URI in the `partOf` property of the AnnotationPages to identify the AnnotationCollection and display its label and choose a common color for the Annotations. This means that a viewer has to load all AnnotationPages from all Canvases if it wants to present a list of all AnnotationCollections in the Manifest to the user.

issues:
- partOf in Prezi3 wants a list with id and type https://iiif.io/api/presentation/3.0/#partof

## Restrictions

???

## Example

We use a Manifest containing two pages from a newspaper (Berliner Tageblatt, February 16, 1925, from Staatsbibliothek Berlin via Europeana) and a set of Annotations concerning layout elements.

{% include manifest_links.html viewers="UV, Mirador, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

AnnotationPage with Annotations on the first Canvas.

{% include jsonviewer.html src="anno_p1.json" %}

AnnotationPage with Annotations on the second Canvas.

{% include jsonviewer.html src="anno_p2.json" %}

AnnotationCollection referencing the AnnotationPages.

{% include jsonviewer.html src="anno_coll.json" %}

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

