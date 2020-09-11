---
title: Book behavior variations
id: 11
layout: recipe
tags: [image, text, layout]
summary: "These manifests use the 'behavior' property to specify how the Canvases should be displayed in the viewer in relation to one another, such as continuous for a scroll or as individuals for a book imaged as full page spreads."
---

## Use Cases

The `behavior` property tells a presentation client one part of how to display a sequence of resources to a viewer; specifically, how the canvases should display in relation to one another such as paged (two-up) for a book-view layout, continuous (stitched together) for a scroll, or as individual images where a book-view layout is not appropriate.

Most book objects that have a standard codex format with the concept of recto and verso (assuming one image per page) are best presented in book-view, with two facing pages displaying next to one another. In this case, the `behavior` property value used is `paged`. For an example manifest, see the [Book (simplest)][0009] recipe.

Not all books (or their digital surrogates) are created equal, so the IIIF Presentation API defines a few different behavior options. In this recipe we demonstrate example manifests for two use cases:

Use case 1: A scroll object where the scroll has been imaged by capturing each segment through multiple shots, allowing the scroll to be "stitched together" in the viewer for a single continuous view. In this example, the manifest will use the `behavior` property `continuous`.

Use case 2: A book (codex) object where the page images were captured with one image per 2-page spread. In this example, the manifest will use the `behavior` property `individuals`.

## Implementation notes

The default `behavior` value, if not specified, is `individuals` for Layout Behaviors (as opposed to Temporal, Collection, Range, and Miscellaneous Behaviors).

In addition to `behavior`, you may want to use the `viewingDirection` property (see [Book (paging variations)][0010] recipe), for example `right-to-left` or `top-to-bottom`, depending on the expected user experience for viewing your resource or the specificities of the physical object and its digital surrogate. Interactions between `viewingDirection` and `behavior`, especially when they are set on multiple and/or hierarchical resources, need special attention. You are recommended to read [the Presentation 3.0 spec on `behavior`](https://iiif.io/api/presentation/3.0/#behavior) carefully and to keep current with future releases.

## Restrictions

The property is permissible for all resource types, but some values (`unordered`, `individuals`, `continuous`, `paged`) are permissible only for `Collection`, `Manifest`, and `Range`, while others (`facing-pages`, `non-paged`) are permissible only on `Canvas`. Clients should process the property on any resource type.

## Example 1: Scroll (`continuous`)

This manifest represents an Ethiopian scroll,

Note that as of the writing of this recipe, the `behavior` value of `continuous` has no noticeable effect in the Universal Viewer demonstration linked below, but you can see it in practice with IIIF Presentation API 2 here: . For forward compatibility, it is a part of the manifest.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest-continuous.json" %}

{% include jsonviewer.html src="manifest-continuous.json" config='data-line="15"' %}

## Example 2: Book imaged as 2-page spreads (`individuals`)

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest-individuals.json" %}

{% include jsonviewer.html src="manifest-individuals.json" config='data-line="15"' %}

# Related recipes

* [Book (simplest)][0009]
* [Book (paging variations)][0011]
* [Thumbnails][0012]
* [Table of contents (ranges) - book chapters][0024]

{% include acronyms.md %}
{% include links.md %}
