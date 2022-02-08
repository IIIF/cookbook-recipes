---
title: Image Rotation with Image Service
id: 40
layout: recipe
tags: image, manipulation
summary: Rotating an image using a IIIF Image API service
viewers:
topic: 
 - basic
 - image
---

## Use Case

You have a codex that has been scanned and prepared for online display. The work was digitized by scanning single pages, and one page's image is mistakenly rotated 90 degrees. Rather than altering the original scan files or re-scanning the work, you'd like to make an adjustment at the presentation level so viewers will display the page in the same layout as the other pages.

## Implementation Notes

Rotation of an image may be supported by your IIIF Image API server, and if so, it's a great way to handle changing the view of an image. The only thing like a baseline expectation for server support is that [Level 2 conformant IIIF Image API servers][https://iiif.io/api/image/3.0/compliance/#33-rotation] must support rotation by 90º increments. Other levels may or may not. You therefore first need to know your image server's capabilities in order to create your manifest. This is especially true if you want to rotate by an amount other than 90º, 180º, or 270º (360º being equal to 0º). No IIIF Image server is required to implement this kind of rotation. The same goes for [mirroring before rotation][https://iiif.io/api/image/3.0/#43-rotation]. IIIF Image API servers may permit mirroring the image before rotating, but this functionality is not required at any level of image service IIIF compliance.

In the image service section of your manifest, you must use an `@context` field in order to point to the [`ImageApiSelector`][https://iiif.io/api/annex/openannotation/#iiif-image-api-selector] definition for canonical rotation options.

If your resource is not being served from an image server that supports rotation through the IIIF Image API, it is syntactically valid to use [CSS rotation][0039], though at the time of writing this recipe no known viewers support it.

As well, though it is not described in this recipe, the Presentation API describes the ability to rotate a region by using a fragment on the `target` value's URI.


## Restrictions

This approach is not usable if you do not have a IIIF Image API service for the image, or if your image server does not allow rotation through service calls. Rotation amounts may only be available in 90º increments even if your image server supports rotation. Mirroring an image before rotation similarly may or may not be available from your image server.

## Example

For this recipe, we conveniently had a work on hand that had a page whose text direction was oriented perpendicularly to the facing page. For simplicity's sake, we are using the page in isolation. Because no viewers currently support rotation. we have included here a picture of the page in its original orientation followed by its appearance according to the manifest's declaration for rotation.

![Image of a codex page in its original orientation when reading conventionally](https://fixtures.iiif.io/info.html?file=/images/UCLA/conoximent_individuals/0-21198-zz00022840-1-page1.jpg "Before rotation")

![Image showing the same codex page after rotating 90 degrees clockwise](https://fixtures.iiif.io/info.html?file=/images/UCLA/conoximent_individuals/0-21198-zz00022840-1-page2.jpg "After rotation")

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Image Rotation with CSS][0039]

{% include acronyms.md %}
{% include links.md %}

