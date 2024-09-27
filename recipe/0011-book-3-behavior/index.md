---
title: Book 'behavior' Variations (continuous, individuals)
id: 11
layout: recipe
tags: [image, text, layout]
summary: "The 'behavior' property specifies how Canvases should be displayed in the viewer in relation to one another, such as paged for book-view, continuous for a scroll or accordion book, or as individuals for a book imaged as full page spreads."
viewers:
 - id: UV
   support: partial
 - Mirador
 - Theseus
topic: property
property:
 - behavior
 - image
code:
 - iiif-prezi3
---

## Use cases

Book objects (and their digital surrogates) come in a variety of forms and layouts that affect how we might display a resource to users, such as codices with the concept of recto and verso, scrolls or accordion books that have a continuous layout, or a digitized codex that has been imaged as 2-page spreads.

To tell a presentation client how to display a sequence of resources in relation to one another, IIIF uses the `behavior` property. For example, a collection of unordered photographs might use the property `"behavior": "unordered"`; or, a standard codex might be best presented in book-view, with two facing pages displaying next to one another. In this case, the `behavior` property value used is `paged`. For an example Manifest using the `"behavior": "paged"` property, see the [Book (simplest)][0009] recipe.

This recipe provides example Manifests demonstrating the use of the `behavior` property for two additional book-related use cases:

**Use case 1:** An accordion book that has been imaged by capturing each segment through multiple shots, allowing the book to be "stitched together" in the viewer for a single continuous view. In this example, the Manifest will use the `behavior` property `continuous`.

**Use case 2:** A book (codex) object where the page images were captured with one image per 2-page spread. In this example, the Manifest will use the `behavior` property `individuals`.

## Implementation notes

The default `behavior` value, if not specified, is `individuals` for Layout Behaviors (as opposed to Temporal, Collection, Range, and Miscellaneous Behaviors).

In addition to `behavior`, you may want to use the `viewingDirection` property (see [Viewing direction and its effect on navigation][0010] recipe), for example `right-to-left` or `top-to-bottom`, depending on the expected user experience for viewing the resource. Interactions between `viewingDirection` and `behavior`, especially when they are set on multiple and/or hierarchical resources, need special attention. For more information, consult [the Presentation 3.0 spec on `behavior`](https://iiif.io/api/presentation/3.0/#behavior) to keep current with future releases.

## Restrictions

The property is permissible for all resource types, but some values (`unordered`, `individuals`, `continuous`, `paged`) are permissible only for Collection, Manifest, and Range, while others (`facing-pages`, `non-paged`) are permissible only on Canvas.

## Examples

### Use case 1: Accordion book (`continuous`)

This Manifest represents an Ethiopic accordion book with a continuous layout running left-to-right. It has four images that, when using the `"behavior": "continuous"` property, will display as a single continuous image in the viewer.

{% include manifest_links.html viewers="Mirador, Theseus" manifest="manifest-continuous.json" %}

{% include jsonviewer.html src="manifest-continuous.json" config='data-line="10-12"' %}

### Use case 2: Book imaged as 2-page spreads (`individuals`)

This Manifest represents a book imaged as 2-page spreads (two facing pages in a single image). When using the `"behavior": "individuals"` property, the presentation client will force a one-at-a-time view and remove the "book view" option.

{% include manifest_links.html viewers="UV, Mirador, Theseus" manifest="manifest-individuals.json" %}

{% include jsonviewer.html src="manifest-individuals.json" config='data-line="10-12"' %}

# Related recipes

* [Book (simplest)][0009]
* [Viewing direction and its effect on navigation][0010]

{% include acronyms.md %}
{% include links.md %}
