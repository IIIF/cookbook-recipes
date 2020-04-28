---
title: Multiple Related Images (Book, etc.)
id: 9
layout: recipe
tags: [image, presentation]
summary: "A sample Manifest for an object composed of a set of images (book, etc.)."
---


## Use Case

A sample Manifest for an object composed of a set of images (book, etc.). If you have an object consisting of a sequence of multiple related images, this pattern turns it into a valid IIIF Presentation resource. In practice it could be any kind of compound object that may comprise a series of pages, surfaces or views (pages of a book, the two sides of a postcard, four cardinal views of a statue etc.).

The sample Manifest below represents the digital surrogate of a part of a printed book, starting with a frontispiece and a title page. It contains four Canvases and each Canvas is filled with the full size image of a page. In this case we have one view per page, but depending on the type of object and how it has been digitized, you could also have one view per double page spread or one view per side.


## Implementation notes

Since this Manifest is meant to represent a printed book, it has the `behavior` value `paged`, thus indicating that it can be presented in a page-turning interface. But depending on the expected user experience and the nature of the physical object and its digital surrogate, you may use other hints to inform a client of the appropriate presentation order and layout behavior. The Presentation 3.0 specification defines other values for `behavior` (see also [Book (paging variations)][0011] recipe) and a `viewingDirection` property (see also [Book (viewingDirection variations)][0010] recipe) that will both affect the presentation of the object in a user interface.

The Manifest's `items` property contains the list of Canvases representing the ordered sequence of views that make up the digital object. Each Canvas conveys the correct aspect ratio for that view, whatever it is. The most common case for a book is to have one view per page, thus resulting in one image per Canvas.

The `label` property on a Canvas is recommended: it is the human readable label for a given view and thus allows users to distinguish between the different images. It usually gives the page or folio numbers, or any other appropriate term to identify a particular view within the object. The `label` property can be fully internationalized (see also [Text in Multiple Languages][0006]).

As in the sample Manifest below, you should also consider providing a [thumbnail][[prezi3-thumbnail]] for each Canvas, so that a client can render a grid view or a thumbnail strip efficiently, thus helping users to navigate within the object. This is a general good practice and it is especially recommended if you do not provide a IIIF Image API service for your images.


## Example

[JSON-LD](manifest.json)
 | [View in Universal Viewer](https://universalviewer.io/uv.html?manifest={{ site.url }}{{ site.baseurl }}{{ page.url }}manifest.json) 

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

