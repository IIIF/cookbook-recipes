---
title: Internationalization and Multi-lingual Labels
id: 6
layout: recipe
tags: [i18n, text, presentation]
summary: "You have more than one label for a IIIF resource, and/or more than one language version of the label."
---


## Use Case

You have more than one label for a IIIF resource, and/or more than one language version of the label. This can be used for the statement that is required to be shown to the user, the summary of the content, and the metadata labels and values.


## Implementation notes

The value `none` indicates that the language value of the string is either unknown, or not applicable.

A client will choose the appropriate value(s) by following the processing rules provided in https://iiif.io/api/presentation/3.0/#43-language-of-property-values


## Example
Multiple values for the manifest label in different languages (lines 6-17)

In descriptive metadata, multiple languages for the key in the key/value pair (lines 22-27, 43-48)

Values with no specified language use "none" (lines 30-32, 51-53)

Summary only in English (lines 37-39)

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="6-17, 22-27, 30-32, 37-39, 43-48, 51-53"' %}

# Related recipes

* [Simple Image Manifest][0001]
