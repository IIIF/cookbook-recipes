---
title: Table of Contents for Book Chapters
id: 24
layout: recipe
tags: [text, image, book]
summary: "Using Ranges to create a table of contents for a book"
---

## Use Case

Many books have a logical structure, such as chapters and other sections or multiple works contained within an anthology or bound manuscript, that can be made navigable through a table of contents (ToC) or other wayfinding methods. IIIF uses Ranges to represent a book's structure and IIIF viewers can display this ToC in a side panel to aid users in navigating the book by chapter, section, work, etc.

## Implementation Notes

Ranges are used to represent a structure within a book object by grouping Canvases together and/or by providing an alternate order of the Canvases from the order presented in the `items` property of the Manifest. Ranges can include Canvases, parts of Canvases, or other Ranges, creating a tree structure like a table of contents.

Ranges are contained within the `structures` property and require a `label` property to display in the ToC (viewers do not use the Canvas `label` property to display values in the ToC). The `behavior` property can also be applied to Ranges. For more information on how `behavior` affects navigation in Ranges, see the [the Presentation 3.0 spec on Ranges](https://iiif.io/api/presentation/3.0/#54-range).

## Restrictions

None

## Example

In this example, an Ethiopic manuscript contains multiple works, one of which contains multiple sections. The manifest contains a Range to represent the top-level structure (begins with lines 247-254), and another embedded Range to represent the content sections of the second work, *Arede'et* (begins with lines 275-282).

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="246-326, 247-254, 275-282"' %}

## Related Recipes

* [Book (simplest)][0009]
* [Book (paging variations)][0011]
* [Table of Contents for A/V Content][0026]

{% include acronyms.md %}
{% include links.md %}
