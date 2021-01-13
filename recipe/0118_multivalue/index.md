---
title: Displaying Multiple Values with Language Maps
id: 118
layout: recipe
tags: [tbc]
summary: "The language map pattern requires that all values are supplied as an array, whether a single value string or a string of multiple values."
---

## Use Case

In some cases, a work is known by more than one title (or has multiple authors, subject heading, etc.) that we would like to display to end users. In this case, our work has variant titles that we will include in the `metadata` property using the required arrays. This pattern can be applied to any property values that are intended to be displayed to end users.

## Implementation Notes

Language maps are required of all strings that are intended to be displayed to the user (this includes the `label` and `summary` properties, as well as `label` and `value` properties within the `metadata` and `requiredStatement` properties). Furthermore, the language map pattern requires that all values are supplied as an array, whether a single value string or a string of multiple values. -- any strings values should include each title variation (within the same language) as a separate string within a single array; if the work has only a single title, the title would be included as a single-value array.

all "associated values must be arrays of strings, where each item is the content in the given language." For more information, see the Presentation API
[Language of Property Values](https://iiif.io/api/presentation/3.0/#44-language-of-property-values) section.

## Example

In this example, the work has multiple titles in both English and French, with two separate arrays -- one array for the English (lines 6-9) and one for the French (lines 10-14). In the `metadata` (lines 18-27), `summary` (lines 31-33), `requiredStatement`(lines 36-45) objects, the labels and values are included as single string arrays.

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="6-9, 10-14, 18-27, 31-33, 36-45"'%}

## Related Recipes

* [Internationalization and Multi-language Values][0006]
* [Metadata][0029]

{% include acronyms.md %}
{% include links.md %}
