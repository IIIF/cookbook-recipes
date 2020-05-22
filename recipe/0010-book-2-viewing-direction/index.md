---
title: Navigation Direction (viewingDirection variations)
id: 10
layout: recipe
tags: image, text, layout
summary: "Sample Manifests for informing a client how the Canvases should be displayed to the viewer in order to read the contents authentically in accordance with the script used, object layout, or reading practice."
---

## Use Case

Sample Manifests for informing a client how the Canvases should be displayed to the viewer in order to read the contents authentically in accordance with the script used, object layout, or reading practice.

The `viewingDirection` property tells a presentation client one part of how to display a sequence of resources to a viewer. It is permissible for IIIF `Collection`, `Manifest`, and `Range` resources, but is an invalid property on other types of resources. Clients should process the property when it is part of a `Collection` or `Manifest`, may process it when part of a `Range`, and should ignore it if used other resource types.

Possible values for `viewingDirection` are `left-to-right` (the default if the property is not specified), `right-to-left`, `top-to-bottom`, and `bottom-to-top`. Note particularly that this is the visual layout of the views, not the orientation of the views or the layout or orientation of any visual material of the represented objects' views.

The `viewingDirection` property can inform a client of the appropriate presentation order and navigational cues for a variety of resource arrangements. Some examples include a sequence of pages within a manuscript, all views of a scroll, or a set of multiple books.

Though the example Manifests below use the `items` property to contain Canvases representing the reading sequence of views that make up an object, the `viewingDirection` property should be given greater weight than the Manifest order of views.

## Implementation notes

In addition to `viewingDirection`, you may want to use the `behavior` property (see also the [Book (paging variations)][0011] recipe) depending on the expected user experience for viewing your resource(s) or the specificities of the physical object and its digital surrogate. The most common `behavior` value for a book is `paged`. Interactions between `viewingDirection` and `behavior`, especially when they are set on multiple and/or hierarchically ordered resources, need special attention. You are recommended to read [the Presentation 3.0 spec on `behavior`](https://iiif.io/api/presentation/3.0/#behavior) carefully and to keep current with future releases.

## Restrictions

None known

## Example 1: `viewingDirection` `right-to-left`

This Manifest shows the playbill for "Akiba gongen kaisen-banashi," "Futatsu chōchō kuruwa nikki", and "Godairiki koi no fūjime", kabuki performances at the Chikugo Theater in Osaka, from the fifth month of Kaei 2 (May, 1849).

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest-rtl.json" %}

{% include jsonviewer.html src="manifest-rtl.json" config='data-line="15"' %}

## Example 2: `viewingDirection` `top-to-bottom`

This Manifest represents a portion of the diary of William Lewis Sachtleben, an American long-distance cyclist who rode across Asia from Istanbul to Peking in 1891 to 1892 with Thomas Gaskell Allen Jr., his classmate from Washington University.

{% include manifest_links.html viewers="UV" manifest="manifest-ttb.json" %}

{% include jsonviewer.html src="manifest-ttb.json" config='data-line="15"' %}

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.

* [Book (simplest)][0009]
* [Book (paging variations)][0011] — The objects shown here are `paged`, but other viewing compositions are possible, including `continuous` for scrolls and rolls.
* [Multi-volume work][0030] — Not only is this page range a selection from one diary, it is also from one volume of many that make up the complete Sachtleben diaries.

{% include acronyms.md %}
{% include links.md %}