---
title: Embedded or referenced Annotations
id: -1
layout: recipe
tags: [tbc]
summary: "Annotations can be embedded in the manifest or referenced from separate URIs."
---

## Use Case

I would like to link to a large annotation list and not have it embedded in the manifest because it will be too big.

## Implementation Notes

Annotations for a Canvas are stored in the `annotations` property of the Canvas in the form of an Annotation Page object containing a list of Annotation objects conforming to the [W3C Web Annotation](https://www.w3.org/TR/annotation-model/) format.

The Annotation Page and the Annotations can either be embedded in the manifest (as in the [Simplest Annotation][0266] example) or referenced (as in this recipe) by putting the URI of the external document in the manifest.

External Annotation Pages are referenced in the `annotations` property of the Canvas by an object with an `id` property containing the URI of the external document and a `type` property containing `AnnotationPage`.

The external Annotation Page document must have a `@context` property containing `http://iiif.io/api/presentation/3/context.json` (TODO: what about `http://www.w3.org/ns/anno.jsonld`?), an `id` property with its URI, a `type` `AnnotationPage`, and an `items` property containing the list of Annotations.

Each Annotation in the Annotation Page must have an `id` property with a unique identifier, the `type` `Annotation` and a `target` and a `body`. The `target` of all Annotations should be the id of the Canvas that contains the reference to the Annotation Page. This means that there should be one Annotation Page document for each Canvas that you want to annotate. 

The `target` of the Annotation can be just the URI of the Canvas if you want to annotate the full canvas as in [Simplest Annotation][0266] or use a fragment selector at the end of the URI as in [Simple Annotation — Tagging][0021] or a more complex selector as in [Annotation with a Non-Rectangular Polygon][0261]. 

The `body` itself can be an object with a type of TextualBody that contains the text in a value property and specifies the format of the text string (e.g. text/plain) in a format property and the language (e.g. de for German) in a language property as in the example below.



## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.? 

Delete this section if it is not needed.
If you don't know what the restrictions might be initially, just leave the following line:
**Unknown - Help Needed**

## Example

TODO: Describe the solution in prose and provide an example.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}

### Manifest file

{% include jsonviewer.html src="manifest.json" %}

### Annotation Page file

{% include jsonviewer.html src="annotationpage.json" %}

## Related Recipes

* [Simplest Annotation][0266] for a simple embedded Annotation

{% include acronyms.md %}
{% include links.md %}

