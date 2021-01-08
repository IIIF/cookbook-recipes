---
title: Displaying Single and Multiple Values (Arrays)
id: 118
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

The language map pattern requires that all values are supplied as an array, whether a single value string or a string of multiple values. For example, a work that is known by more than one title can include each title variation as a separate string within a single array; if the work has only a single title, the title would also be included as an array with a single value. In the use case highlighted in this recipe, the work has multiple titles in both English and French, with two separate arrays -- one array for the English and one for the French.

## Implementation Notes

Note that per Presentation API 4.4, in language maps "[t]he associated values must be arrays of strings, where each item is the content in the given language."
What do you need to know to use this pattern?
How do you implement the pattern?

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

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}
