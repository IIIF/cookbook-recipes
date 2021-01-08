---
title: Internationalization and Multi-language Values
id: 6
layout: recipe
tags: [i18n, text, presentation]
summary: "An example of a IIIF Resource with labels/descriptions in multiple languages."
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

In the `metadata` and `requiredStatement` properties, the 'label' values for both "Subject" and "Held by" fields (lines 16-21, 43-48) are supplied in English and French. The value of the "Subject" field (lines 24-29) is supplied in both English and French, while the value of the "Held by" field (51-53) has no specified language, so uses "none".

Finally, the `summary` property (lines 34-39) has values in both English and French.

To see the language choice in the linked viewers, open the settings menu (gear icon) and choose either English or French.

The image in this example was sourced via Wikimedia Commons and is public domain.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="6-11, 16-21, 24-29, 34-39, 43-48, 51-53"' %}

# Related recipes

* [Rights][0008]
* [Metadata][0029]

{% include acronyms.md %}
{% include links.md %}
