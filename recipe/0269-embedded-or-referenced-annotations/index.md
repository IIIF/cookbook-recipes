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

The Annotation Page and the Annotations can either be embedded in the manifest (as in the [Simplest Annotation][0266] example) or referenced by providing the URI of the external document containing the Annotation Page.


## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.? 

Delete this section if it is not needed.
If you don't know what the restrictions might be initially, just leave the following line:
**Unknown - Help Needed**

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Simplest Annotation][0266] for a simple embedded Annotation

{% include acronyms.md %}
{% include links.md %}

