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

ISSUES
- mention `supplementary` property of Range? seems very specialized
- each AnnotationPage has to be referenced from a Canvas and it can only contain Annotations for that Canvas -> Annotations have to be sorted by Canvas
- the AnnotationPages also contain `partOf` references to the AnnotationCollection and `next` references to form a chain
- the viewer has to follow Canvas -`annotations`-> AnnotationPage -`partOf`-> AnnotationCollection to know if there are AnnotationCollections
- can a viewer find the AnnotationCollection from the Manifest? seeAlso?


## Restrictions

???

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="UV, Mirador, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

