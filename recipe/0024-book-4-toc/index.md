---
title: Table of Contents for Book Chapters
id: 24
layout: recipe
tags: [text, image, book]
summary: "Using Ranges to create a table of contents for a book"
viewers:
 - UV
 - Mirador
 - Theseus
 - Glycerine Viewer
 - TIFY
topic: structure
property: structures
---

## Use Case

Many books have a logical structure that can be made navigable through a table of contents (ToC) or other wayfinding methods. These might include chapters and other internal sections, or might reflect multiple works contained within an anthology or bound manuscript. IIIF uses Ranges to represent a book's structure and IIIF viewers can display this structure as a ToC in an index panel to aid users in navigating the book by chapter, section, work, etc.

## Implementation Notes

Ranges are used to represent a structure within a book object by grouping Canvases together and/or by providing an alternate order of the Canvases from the order presented in the `items` property of the Manifest. Ranges can include Canvases, parts of Canvases, or other Ranges, creating a tree structure like a table of contents.

Ranges are contained within the `structures` property and require a `label` property to display in the ToC (`labels` are not inherited from a referenced Canvas, so you will need to explicitly include the `label` property in the Range). Within a Range, resources are included as an array of resources using the `items` property. These structures can be made hierarchical simply by nesting an `items` array within another `items` array. This is useful when chapters might be sub-divided or in the case of multiple works where individual works may have chapters. This is a departure from the method defined by previous versions of the IIIF Presentation API.

The `behavior` property can also be applied to Ranges. For more information on how `behavior` affects navigation in Ranges, see the [IIIF Presentation API on Ranges](https://iiif.io/api/presentation/3.0/#54-range) and the [Ranges and the `behavior` Property][229] recipe.

## Restrictions

None

## Example

In this example, an Ethiopic manuscript contains multiple works, one of which contains multiple sections. The Manifest contains a Range to represent the top-level structure (begins with lines 247–254), and another embedded Range to represent the content sections of the second work, *Arede'et* (begins with lines 275–282). This will result in a hierarchical ToC like so:

* Tabiba Tabiban [ጠቢበ ጠቢባን]
* Arede'et [አርድዕት]
    * Monday
    * Tuesday

{% include manifest_links.html viewers="UV, Mirador, Glycerine Viewer, Theseus, TIFY" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="246-326, 247-254, 275-282"' %}

## Related Recipes

* [Book (simplest)][0009]
* [Book (paging variations)][0011]
* [Table of Contents for A/V Content][0026]

{% include acronyms.md %}
{% include links.md %}
