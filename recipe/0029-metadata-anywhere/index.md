---
title: Metadata on any Resource
id: 29
layout: recipe
tags: [presentation]
summary: "Provide item metadata for displaying to users"
viewers:
 - UV
 - Mirador  
 - Annona
topic: property
property: metadata
---

## Use Case

Often it is useful to provide descriptive metadata about a resource, such as information on creators, dates, subject headings, and physical or contextual descriptions, that a client will display to the end user. This metadata might describe the entire resource, but may also be applied at more granular levels to provide information on parts of the resource, such as a single image or page, a region of a page, or an annotation.

## Implementation notes

The `metadata` property is used to provide an ordered list of descriptive metadata as an array, with each entry given as a pair of human readable `label` and `value` arrays. The values of both the `label` and `value` properties must be JSON objects. These values will be displayed to the user as label/value pairs by the client. For more information, see the IIIF Presentation API [Metadata](https://iiif.io/api/presentation/3.0/#metadata) section.

## Restrictions

All descriptive properties intended for presentation to the user must use language maps as outlined in the [Language of Property Values](https://iiif.io/api/presentation/3.0/#44-language-of-property-values) section and demonstrated in the [Internationalization and Multi-language Values][0006] recipe.

The content of these entries is intended for presentation only; descriptive semantics should not be inferred. For information on how to include structured metadata that can support discovery, see the [Linking to Structured Metadata][0053] recipe.

## Example

In this example, we have two Canvases, each with a different photograph of the same painting: one using natural light and the other an x-ray image. Metadata is provided at the Manifest level to convey information about the resource and additional metadata is provided on each Canvas to provide image-specific details.

Credit: *John Dee performing an experiment before Queen Elizabeth I*. Oil painting by Henry Gillard Glindoni. Credit: Wellcome Collection. Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

{% include manifest_links.html viewers="UV, Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="10-59, 83-96, 136-149"' %}

# Related recipes

* [Internationalization and Multi-language Values][0006]
* [Displaying Multiple Values with Language Maps][0118]
* [Linking to Structured Metadata][0053]

{% include acronyms.md %}
{% include links.md %}
