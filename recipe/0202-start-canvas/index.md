---
title: Load manifest beginning with a specific canvas
id: 202
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

In some cases, a book object will have front matter, such as blank pages (or perhaps shots of the binding and other non-textual views or color calibration images), that most users would like to skip. In this use case, we use the `start` property to tell the presentation client to skip the initial blank page and load at the first canvas with content.

## Implementation Notes

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
