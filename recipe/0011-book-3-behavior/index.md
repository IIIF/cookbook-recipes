---
title: Book 'behavior' variations (continuous, individuals)
id: 11
layout: recipe
tags: [image, text, layout]
summary: "The 'behavior' property specifies how Canvases should be displayed in the viewer in relation to one another, such as paged for book-view, continuous for a scroll or accordion book, or as individuals for a book imaged as full page spreads."
---

## Use Cases

Book objects (and their digital surrogates) come in a variety of forms and layouts that affect how we might display a resource to users, such as codices with the concept of recto and verso, scrolls or accordion books that have a continuous layout, or a digitized codex that has been imaged as 2-page spreads. To tell a presentation client how to display a sequence of resources in relation to one another, IIIF uses the `behavior` property. For example, a standard codex might be best presented in book-view, with two facing pages displaying next to one another. In this case, the `behavior` property value used is `paged`. For an example Manifest using the `"behavior": "paged"` property, see the [Book (simplest)][0009] recipe.

This recipe provides example Manifests demonstrating the use of the `behavior` property for two additional use cases:

**Use case 1:** A accordion book (concertina) that has been imaged by capturing each segment through multiple shots, allowing the book to be "stitched together" in the viewer for a single continuous view. In this example, the Manifest will use the `behavior` property `continuous`.

**Use case 2:** A book (codex) object where the page images were captured with one image per 2-page spread. In this example, the Manifest will use the `behavior` property `individuals`.

## Implementation notes

The default `behavior` value, if not specified, is `individuals` for Layout Behaviors (as opposed to Temporal, Collection, Range, and Miscellaneous Behaviors).

In addition to `behavior`, you may want to use the `viewingDirection` property (see [Book (paging variations)][0010] recipe), for example `right-to-left` or `top-to-bottom`, depending on the expected user experience for viewing the resource. Interactions between `viewingDirection` and `behavior`, especially when they are set on multiple and/or hierarchical resources, need special attention. For more information, consult [the Presentation 3.0 spec on `behavior`](https://iiif.io/api/presentation/3.0/#behavior) to keep current with future releases.

## Restrictions

The property is permissible for all resource types, but some values (`unordered`, `individuals`, `continuous`, `paged`) are permissible only for `Collection`, `Manifest`, and `Range`, while others (`facing-pages`, `non-paged`) are permissible only on `Canvas`.

## Examples

### Use case 1: Accordion book (`continuous`)

This Manifest represents an Ethiopic accordion book with a continuous layout running left-to-right. It has four images that, when using the `"behavior": "continuous"` property, will display as a single continuous image in the viewer.

_Note: As of the writing of this recipe, the `behavior` value of `continuous` has no noticeable effect in the Universal Viewer demonstration linked below, but you can see it in practice with IIIF Presentation API 2 here: . For forward compatibility, it is a part of the recipe._

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest-continuous.json" %}

{% include jsonviewer.html src="manifest-continuous.json" config='data-line="10"' %}

### Use case 2: Book imaged as 2-page spreads (`individuals`)

This Manifest represents

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest-individuals.json" %}

{% include jsonviewer.html src="manifest-individuals.json" config='data-line="15"' %}

# Related recipes

* [Book (simplest)][0009]
* [Book (paging variations)][0011]
* [Thumbnails][0012]
* [Table of contents (ranges) - book chapters][0024]

{% include acronyms.md %}
{% include links.md %}
