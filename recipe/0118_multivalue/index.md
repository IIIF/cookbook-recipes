---
title: Displaying Multiple Values with Language Maps
id: 118
layout: recipe
tags: [tbc]
summary: "The language map pattern requires that all values are supplied as an array, whether a single value string or a string of multiple values."
---

## Use Case

In some cases, a work is known by more than one title (or has multiple authors, subject heading, etc.) that we would like to display to end users. In this case, our work has title variants that we will include in the `metadata` property using the required arrays. This pattern can be applied to any property values that are intended to be displayed to end users.

## Implementation Notes

Language maps are required of all strings that are intended to be displayed to the user (this includes the `label` and `summary` properties, as well as `label` and `value` properties within the `metadata` and `requiredStatement` properties). Furthermore, the language map pattern requires that all values are supplied as an array, whether a single value or multiple value strings. For example, a work with multiple authors would include separate strings for each author within a single array: `["Picart, Bernard", "Bernard, Jean-Frédéric"]`; a work with only one author would have a single string also within an array: `["Whistler, James McNeill"]`.

In the case of multiple languages, each language is represented by its own "language code/array" pair. For more information on language maps and multi-language values, see the recipe [Internationalization and Multi-language Values][0006]. For more information on what clients are expected to do with language map properties and values in general, see the Presentation API [Language of Property Values](https://iiif.io/api/presentation/3.0/#44-language-of-property-values) section.

## Restrictions

None

## Example

In this example, the work has multiple titles in both English and French. The manifest `label` provides a single title in French within a single-value array (lines 6-8). The alternative titles are provided in the `metadata` property in both English and French, each with variants contained within two separate arrays -- one array for English (lines 18-21) and one for French (lines 22-25). In the `summary` property (lines 30-32) the value is included as a single-string array.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="6-8, 18-21, 22-25, 30-32"'%}

## Related Recipes

* [Internationalization and Multi-language Values][0006]
* [Metadata][0029]

{% include acronyms.md %}
{% include links.md %}
