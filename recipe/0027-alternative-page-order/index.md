---
title: Alternative Page Order
id: 27
layout: recipe
tags: [book, presentation]
summary: "Using Ranges to offer alternative orderings of book pages."
viewers:
topic:
 - structure
---

## Use Case

A book may contain pages in the incorrect order; for example, a codex which was rebound at some point in history may have certain folios or quires accidentally misplaced. You want to digitally represent the book object in its current form while offering users the option to browse its contents in the intended order. IIIF uses Ranges to represent an alternative sequence of book pages.

## Implementation Notes

Ranges represent structure within an object beyond the default order of the Canvases defined in the `items` property of the Manifest. They must be directly within the `structures` property of the Manifest.
There may be more than one Range, each representing an alternative sequence of items (for example, alternative orderings of book pages). The `items` of each Range is an array of referenced Canvases. The first Range should act as the default ordering, and any additional Ranges should be available for the user to select.
For an IIIF viewer to display the selectable Ranges, each Range requires a `label`. Additionally, for the viewer to be able to use the provided Ranges for ordering purposes, they must have the `behavior` value `sequence`.


## Restrictions

**Unknown - Help Needed**

## Example

The mockup images in this example Manifest represent the pages of a book. At the top of each mockup page, the intended order of each sequence is shown. The two Ranges are provided within the `structures` property: `"Sequence A"` follows the numbering in blue and reflects the physical sequence of pages in the source; `"Sequence B"` in red represents an alternative reading sequence. From the two or more Ranges with the `behavior` value `sequence`, the first Range should be used as the navigation default, and the others should be selectable.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="404-509"' %}

## Related Recipes

* [Simple Manifest - Book][0009]
* [Table of Contents for Book Chapters][0024]

{% include acronyms.md %}
{% include links.md %}
