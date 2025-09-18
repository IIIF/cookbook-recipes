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

A book may contain pages in the incorrect order; for example, a codex which was rebound at some point in history may have certain folios or quires accidentally misplaced. You want to digitally represent the book object in its current order while offering users the option to browse its contents in the intended order.

## Implementation Notes

In Presentation API 3.0, setting a Range's `behavior` value to `sequence` allows you to define a specific viewing order for Canvases that differs from the default order in the Manifest’s items property. 
There may be more than one Range, each representing an alternative sequence of items (for example, alternative orderings of book pages). The `items` of each Range is an array of referenced Canvases. The first Range should act as the default ordering, and any additional Ranges should be available for the user to select.
For an IIIF viewer to display the selectable Ranges, each Range should have a `label`. Additionally, for the viewer to be able to use the provided Ranges for ordering purposes, they must have the `behavior` value `sequence`.

When `behavior` is set to `sequence` "user interfaces that interact with this order should use the order within the selected Range, rather than the default order of items" ([Presentation API 3.0](https://iiif.io/api/presentation/3.0/#54-range)).
Furthermore, the behavior property can be assaigned to a list containing, beside `sequence`, other valid behaviors listed on the [behaviors section of the Presentation API](https://iiif.io/api/presentation/3.0/#behavior). These behaviors will work in combination with any behaviors inherited from the parent Manifest.

Other properties of the Range, such as `viewingDirection`, can be set to control the intended visualization of the Range.  

## Restrictions

Ranges with `behavior` set to `sequence` indicate that they define an alternative reading order. Therefore, they:
 - “must be directly within the structures property of the Manifest, and must not be embedded or referenced within other Ranges." see [Range section](https://iiif.io/api/presentation/3.0/#54-range). This ensures that clients can easily locate all available sequences without needing to traverse or resolve nested structures.
 - cannot have `thumbnail-nav` or `no-nav` behaviors.

## Example

The mockup images in this example Manifest represent the pages of a book. At the top of each mockup page, there is the intended order of each sequence. The two Ranges are provided within the `structures` property: `"Sequence A"` follows the numbering in blue and reflects the physical sequence of pages in the source; `"Sequence B"` in red represents an alternative reading sequence. From the two or more Ranges with the `behavior` value `sequence`, the first Range should be used as the navigation default, and the others should be selectable.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="404-509"' %}

## Related Recipes

* [Simple Manifest - Book][0009] shows an example where the order of the pages follows the order in the `items` property. 
* [Table of Contents for Book Chapters][0024] hows how to use Ranges to create a table of contents rather than to represent alternative orders.

{% include acronyms.md %}
{% include links.md %}
