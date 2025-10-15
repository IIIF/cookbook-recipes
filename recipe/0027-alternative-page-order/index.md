---
title: Alternative Page Sequences
id: 27
layout: recipe
tags: [book, presentation]
summary: "Using Ranges to offer alternative orderings of book pages."
viewers:
topic:
 - structure
---

## Use Case

A book may contain pages in the incorrect order; for example, a codex that was rebound at some point in history may have certain folios or quires accidentally misplaced. You want to digitally represent the book object in its current order while offering users the option to browse its contents in the intended order.

## Implementation Notes

In [Presentation API 3.0](https://iiif.io/api/presentation/3.0/#54-range), setting a Range’s `behavior` value to `sequence` allows you to define a specific viewing order for Canvases that differs from the default order in the Manifest’s `items` property. When `behavior` is set to `sequence`, user interfaces that interact with this order should use the order within the selected Range, rather than the default order of items.

There may be more than one Range, each representing an alternative sequence of items (such as different orderings of book pages). The first Range should act as the default ordering, and any additional Ranges should be available for the user to select. For a IIIF viewer to display the selectable Ranges, each Range should have a `label`.

If reordering the Canvases affects the reading layout or direction, properties can be set on the Range (such as `viewingDirection` or other [valid behaviors](https://iiif.io/api/presentation/3.0/#behavior) besides `sequence`) to override those inherited from the Manifest.

## Restrictions

Ranges with the `behavior` value set to `sequence` must be directly within the `structures` property of the Manifest and must not be referenced or embedded within other Ranges ([see specification](https://iiif.io/api/presentation/3.0/#54-range)). Such Ranges have limited hierarchical nesting and cannot be used to describe more complex structures, such as a [Table of Contents for Book Chapters][0024].

## Example

These manuscript folios are an excerpt from the original draft of the 1895 novel _Piccolo mondo antico_ by novelist and Nobel Prize nominee for Literature, Antonio Fogazzaro. The original autograph numbering in pen (384, 385, [386], 387) is incorrect, so archivists noted the correct reading order in pencil: 171r (387), 171v (384), 172r (385), 172v ([386]).

Two Ranges are provided within the `structures` to represent this case study. From the two Ranges with the `behavior` value `sequence`, the first Range should be used as the navigation default, and the other should be selectable.

Images provided by permission of Biblioteca Civica Bertoliana.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="200-261"' %}

## Related Recipes

* [Simple Manifest - Book][0009] shows an example where the order of the pages follows the order in the `items` property.
* [Table of Contents for Book Chapters][0024] shows how to use Ranges to create a table of contents rather than to represent alternative orders.

{% include acronyms.md %}
{% include links.md %}
