---
title: Internationalization and Multi-language Values
id: 6
layout: recipe
tags: [i18n, text, presentation]
summary: "An example of a IIIF Resource with labels/descriptions in multiple languages."
---

## Use case
In some cases, a IIIF resource may have a title or summary/abstract (`label` or `summary`) in more than one language; or, the publisher of the content may want to provide descriptive `metadata` labels in multiple languages, for example supplying the label for the "Creator" key/value pair in both English and French ("Creator"/"Auteur").

## Implementation notes
IIIF allows a language to be specified for strings that are intended to be displayed to the user. Languages are specified by forming a JSON key/value pair where the specified language is the key using the [BCP 47][bcp-47] code for the language and the value is an array, for example `"en": ["Whistler's Mother"]`.

A language key can be associated with Manifest `label` and `summary` properties, as well as the `label` and `value` properties of the `metadata` and `requiredStatement` objects.

If the language is either not known or the string does not have a language, then the key must be the string `none`.

A client will choose the appropriate value(s) by following the processing rules provided in the [Language of Property Values][language-of-property-values] section of the IIIF Presentation API 3.0 specification.

## Restrictions
Note that the implementation described here does not apply to embedded textual bodies in Annotations, which use the Web Annotation pattern of value and language as separate properties.

## Example
In this example, the content is an image of the painting *Whistler's Mother* by James Abbott McNeill Whistler. The painting is know by more than one title and is presented in both English and French. There are multiple examples within this manifest:

- The Manifest label (lines 6-17) is provided in both English and French, and uses two arrays to list the variant titles

- In the `metadata` and `required statement` properties (lines 22-27, 43-48), the label in the key/value pair is supplied in both English and French

- The values in the `metadata` and `required statement` properties (lines 30-32, 51-53) have no specified language, so uses the value "none"

- The `summary` property (lines 37-39) specifies a single language for the property value, English

The image was sourced via Wikimedia Commons and is public domain.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="6-17, 22-27, 30-32, 37-39, 43-48, 51-53"' %}

# Related recipes

* [Simple Image Manifest][0001]
