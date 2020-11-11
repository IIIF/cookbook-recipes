---
title: Internationalization and Multi-lingual Labels
id: 6
layout: recipe
tags: [i18n, text, presentation]
summary: "You have more than one label for a IIIF resource, and/or more than one language version of the label."
---

## Use Case

In some cases, a IIIF resource may have more than one label value, or there may be more than one language version of the label. This can be used for the statement that is required to be shown to the user, the summary of the content, and the metadata labels and values.

## Implementation notes

The value `none` indicates that the language value of the string is either unknown, or not applicable.

A client will choose the appropriate value(s) by following the processing rules provided in https://iiif.io/api/presentation/3.0/#43-language-of-property-values

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
