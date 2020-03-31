---
title: Book (viewingDirection variations)
id: 10
layout: recipe
tags: image, text, layout
summary: "A sample manifest for informing a client how the canvases should be displayed to the viewer in order to read the contents authentically in accordance with the script used or other reading practice."
---

## Use Case

A sample manifest for informing a client how the canvases should be displayed to the viewer in order to read the contents authentically in accordance with the script used or other reading practice.

The `viewingDirection` property tells a presentation client one part of how to display a sequence of resources to a viewer. It is permissible for IIIF `Collection`, `Manifest`, and `Range` resources, but is an invalid property on other types of resources. Clients should process the property when it is part of a `Collection` or `Manifest`, may process it when part of a `Range`, and should ignore it if used other resource types.

Possible values for `viewingDirection` are `left-to-right` (the default if the property is not specified), `right-to-left`, `top-to-bottom`, and `bottom-to-top`. Note particularly that this is the visual layout of the views, not the orientation of the views or the layout or orientation of any visual material of the represented objects' views.

The `viewingDirection` property can inform a client of the appropriate presentation order and navigational cues for a variety of resource arrangements. Some examples include a sequence of pages within a manuscript, all views of a scroll, or a set of multiple books.

Though the example manifest below uses the `items` property for a list of IIIF Canvases, representing the ordered sequence of views that make up a book, in principle the `viewingDirection` property, when appropriately placed in a manifest, should be given greater weight than the manifest order of views. 

## Implementation notes

In addition to `viewingDirection`, you may want to use the `behavior` property (see also [Book (paging variations)][0011] recipe) depending on the expected user experience for viewing your resource(s) or the specificities of the physical object and its digital surrogate. The most common `behavior` value for a book is `paged`. Interactions between `viewingDirection` and `behavior`, especially when they are set on multiple and/or hierarchized resources, need special attention. You are recommended to read [the Presentation 3.0 spec on `behavior`](https://iiif.io/api/presentation/3.0/#behavior) carefully and to keep current with future releases.


## Restrictions

None known

## Example

[JSON-LD](manifest.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-line="6" data-src="manifest.json" }
```json
```

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.

* [Book (simplest)][0009]
* [Book (paging variations)][0011]
* [Thumbnails][0012]
* [Table of contents (ranges) - book chapters][0024]

{% include acronyms.md %}
{% include links.md %}