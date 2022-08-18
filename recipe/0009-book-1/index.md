---
title: Simple Manifest - Book
id: 9
layout: recipe
tags: [image, presentation]
summary: "Represent a book, or any object composed of a set of images, as a simple Manifest."
viewers:
 - UV
 - Mirador  
 - Annona
topic: 
 - image
 - basic
---

## Use Case

You have a digitized book consisting of a sequence of multiple images and want to model it as a IIIF Manifest. This recipe deals with a book (codex) object, but in practice it is applicable to any kind of compound object that may comprise a series of pages, surfaces or views (pages of a modern printed book like in the example below, the two sides of a postcard or the four cardinal views of a statue).


## Implementation notes

The sample Manifest below represents the digital surrogate of a part of a printed book, starting with a frontispiece and a title page. It contains five Canvases and each Canvas is filled with the full size image of a page. In this case we have one view per page, but depending on the type of object and how it has been digitized, you could also have one view per double page spread or one view per side.

Since this Manifest is meant to represent a printed book, it has the `behavior` value `paged`, thus indicating that it can be presented in a page-turning interface. But depending on the expected user experience and the nature of the physical object and its digital surrogate, you may use other hints to inform a client of the appropriate presentation order and layout behavior. The Presentation 3.0 specification defines other values for `behavior` (see also [Book behavior variations][0011] recipe) and a `viewingDirection` property (see also [Viewing direction and its effect on navigation][0010] recipe) that will both affect the presentation of the object in a viewing interface.

The Manifest's `items` property contains the list of Canvases representing the ordered sequence of views that make up the digital object. Each Canvas conveys the correct aspect ratio for that view, whatever it is. The most common case for a book is to have one view per page, thus resulting in one image per Canvas.

The `label` property on a Canvas is recommended: It is the human-readable label for a given view and allows users to distinguish between the different images. It usually gives the page or folio numbers, or any other appropriate term to identify a particular view within the object. The `label` property can be fully internationalized (see also [Text in Multiple Languages][0006]).

You should also consider providing a [thumbnail][prezi3-thumbnail] for each Canvas, so that a client can render a grid view or a thumbnail strip efficiently, thus helping users to navigate within the object. This is a general good practice and it is especially recommended if you do not provide a IIIF Image API service for your images.


## Example

{% include manifest_links.html viewers="UV, Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}


# Related recipes

* [Simplest Manifest - Single Image File][0001]
* [Simple Manifest - Image with IIIF Image API Service][0005]
* [Viewing direction and its effect on navigation)][0010]
* [Book behavior variations][0011]
* [Thumbnails][0012]

{% include acronyms.md %}
{% include links.md %}

