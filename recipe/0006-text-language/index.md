---
title: Internationalization and Multi-language Values
id: 6
layout: recipe
tags: [i18n, text, presentation]
summary: "An example of a IIIF Resource with labels/descriptions in multiple languages."
---

## Use case
In some cases, a IIIF resource may have a title or description (`label` or `summary`) in more than one language; or, the publisher of the content may want to provide descriptive `metadata` labels in multiple languages for different language audiences, for example supplying a label for a "Creator" field in both English and French ("Creator", "Auteur").

## Implementation notes
In these cases, IIIF allows a language to be specified for strings that are intended to be displayed to the user. Languages are specified using a JSON key/value pair where the specified language is the key using the [BCP 47](https://tools.ietf.org/html/bcp47) code for the language and the value is an array, for example: `"en": ["Whistler's Mother"]`.

A language key can be associated with Manifest `label` and `summary` properties, as well as the `label` and `value` properties of the `metadata` and `requiredStatement` descriptive properties.

If the language is either not known or the string does not have a language, then the key must be the string `none`.

A client will choose the appropriate value(s) by following the processing rules provided in the [Language of Property Values](https://iiif.io/api/presentation/3.0/#44-language-of-property-values) section of the IIIF Presentation API 3.0 specification.

## Restrictions
Note that the implementation described here does not apply to embedded textual bodies in Annotations, which use the Web Annotation pattern of value and language as separate properties.

## Example
In this example, the content is an image of the painting *Whistler's Mother* by James Abbott McNeill Whistler. The Manifest `label` property has both the English and French titles (lines 6-14).

In the `metadata` and `required statement` properties (lines 18-21, 31-34), the label for the "Creator" and "Held by" fields is supplied in both English and French. Here, the values (lines 22-24, 35-37) have no specified language, so uses the value "none".

Finally, the `summary` property (lines 27-29) has a value only for English.

The image was sourced via Wikimedia Commons and is public domain.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="6-17, 22-27, 30-32, 37-39, 43-48, 51-53"' %}

# Related recipes

* [Simple Image Manifest][0001]
