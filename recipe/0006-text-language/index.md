---
title: Internationalization and Multi-language Values
id: 6
layout: recipe
tags: [i18n, text, presentation]
summary: "An example of a IIIF Resource with labels/descriptions in multiple languages."
viewers:
 - UV
 - Mirador  
 - Annona
topic: basic
property: label, summary, metadata, requiredStatement
---

## Use case
In some cases, a IIIF resource may have a title or description (`label` or `summary`) in more than one language; or, the publisher of the content may want to provide descriptive `metadata` field labels in multiple languages for different language audiences, for example supplying a `label` for a creator field in both English and French ("Creator", "Auteur").

## Implementation notes
With IIIF Presentation API 3.0, language maps are mandatory for strings that are intended to be displayed to the user. Languages are specified using a JSON key/value pair where the specified language is the key following [BCP 47](https://tools.ietf.org/html/bcp47) language codes and the value is an array, for example: `"en": ["Whistler's Mother"]`. If the language is not known or the string does not have a language, then the key must be the string `none`.

A client will choose the appropriate value(s) by following the processing rules provided in the [Language of Property Values](https://iiif.io/api/presentation/3.0/#44-language-of-property-values) section of the IIIF Presentation API 3.0 specification.

Language keys should be associated with the Manifest `label` and `summary` properties, as well as the `label` and `value` properties of the `metadata` and `requiredStatement` descriptive properties.

## Restrictions
1. Note that the implementation described here does not apply to embedded textual bodies in Annotations, which use the Web Annotation pattern of value and language as separate properties.

2. It should be noted that BCP 47 allows hyphen breaks for locale and scripts (e.g. en-US); however, if you are processing these manifests with Javascript it will break the . notation features for navigating JSON objects so brackets for accessing language properties are recommended.

## Example
In this example, the content is an image of the painting commonly known as *Whistler's Mother* by James Abbott McNeill Whistler. The Manifest `label` property has both the English and French titles (lines 6-11).

In the `metadata` and `requiredStatement` properties, the `label` strings for "Creator", "Subject" and "Held by" fields (lines 16-21, 31-36, 58-63) are supplied in both English and French. The value for the "Subject" field (lines 39-44) is supplied in both English and French, while the values for the "Creator" and "Held by" fields (lines 24-26, 66-68) have no specified language, so use "none" for the language map.

Finally, the `summary` property (lines 49-54) has values in both English and French.

To see the language choice in the linked viewers, open the settings menu (gear icon) and choose either English or French.

The image in this example was sourced via Wikimedia Commons and is public domain.

{% include manifest_links.html viewers="UV, Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="6-11, 16-21, 24-26, 31-36, 39-44, 49-54, 58-63, 66-68"' %}

# Related recipes

* [Rights][0008]
* [Metadata][0029]

{% include acronyms.md %}
{% include links.md %}
