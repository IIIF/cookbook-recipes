---
title: Simplest Manifest - Multiple Related Images (Book, etc.)
id: 9
layout: recipe
tags: [image, presentation]
summary: "The simplest viable manifest for an object composed of a set of images (book, etc.)."
---


## Use Case

The simplest viable Manifest for an object composed of a set of images. If you have an object consisting of multiple related images, this pattern turns it into a valid IIIF Presentation resource. In practice it could be any kind of compound object that may comprise a series of pages, surfaces or views (pages of a book, the two sides of a postcard, four cardinal views of a statue etc.).

The manifest's `items` property contains the list of canvases representing the ordered sequence of views that make up the digital object. By default, the included canvases are distinct views that should only be presented individually in the order they appear in `items`.

The sample manifest below represents the digital surrogate of a part of a printed book, comprised of a frontispiece and a title page. It contains two canvases and each canvas is filled with the full size image of a page. In this case we have one view per page, but depending on the type of object and how it has been digitized, you could also have one view per double page spread or one view per side.

The `label` property on a canvas is recommended: it is the human readable label for a given view and thus allows users to distinguish between the different images. It usually gives the page or folio numbers, or any other appropriate term to identify a particular view within the object. The `label` property can be fully internationalized (see also [Text in Multiple Languages][0006]).


## Implementation notes

Depending on the expected user experience and the nature of the physical object and its digital surrogate, you may use several hints to inform a client of the appropriate presentation order and layout behavior. The Presentation 3.0 specification defines features like `viewingDirection` (see also [Book (viewingDirection variations)][0010] recipe) and `behavior` (see also [Book (paging variations)][0011] recipe) that will affect the presentation of the object in a user interface.

You should also consider providing a [thumbnail][[prezi3-thumbnail]] for each canvas, so that a client can render a grid view or a thumbnail strip efficiently, thus helping users to navigate within the object. This is a general good practice and it is especially recommended if you do not provide a IIIF Image API service for your images.


## Example

[JSON-LD](manifest.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```
```

# Related recipes

* [Simplest Manifest - Single Image File][0001]
* [Book (viewingDirection variations)][0010]
* [Book (paging variations)][0011]

{% include acronyms.md %}
{% include links.md %}

