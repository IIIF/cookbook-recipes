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

You have a codex that has been scanned and prepared for online display. The work was digitized by scanning single pages, and one page's image is mistakenly rotated 90 degrees. Rather than altering the original scanned files or re-scanning the work, you'd like to make an adjustment at the presentation level so viewers will display the page in the same layout as the other pages.

## Implementation Notes

In the image service section of your manifest, you must use an `@context` field in order to point to the [`ImageApiSelector`](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector) definition for canonical rotation options. The selector as defined must contain a `type` property whose value must be `ImageApiSelector`. The `rotation` property takes as its value just the numeric amount of rotation in degrees. **negative value?** For more  information about the selector and its use outside of rotation, read the full [selector document](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector).

Rotation of an image may be supported by your IIIF Image API server, and if so, using that service for rotation is a great way to handle changing the view of an image. To be able to support this recipe your Image API server must support the rotation requested in the selector. Rotation by 90º increments is mandatory for [level 2 IIIF Image API servers](https://iiif.io/api/image/3.0/compliance/#33-rotation) but can be implemented at all levels. Rotation by an arbitrary amount other than 90º, 180º, or 270º (360º being equal to 0º) is always optional, so you would need to familiarize yourself with what your image servers supports and look into the profile portion of the server's `info.json`.

This is true for [mirroring before rotation](https://iiif.io/api/image/3.0/#43-rotation), as this functionality is not mandatory at any level of image service IIIF compliance.

If your resource is not being served from an image server that supports the desired rotation (or rotation at all) through the IIIF Image API, then you can use the [CSS rotation][0039] recipe. Using CSS for rotation depends on the viewer to rotate the image rather than the server. (Note that at the time of writing this recipe no known viewers support CSS rotation.)

As well, though it is not described in this recipe, the Presentation API indicates the ability to target a region for rotation by using a fragment on the `target` value's URI.


## Restrictions

This approach is not usable if you do not have a IIIF Image API service for the image, or if your image server does not allow rotation through service calls. Rotation amounts may only be available in 90º increments even if your image server supports rotation. Mirroring an image before rotation similarly may or may not be available from your image server.

## Example

For this recipe, we conveniently had a work on hand that had a page whose text direction was oriented perpendicularly to the facing page. For simplicity's sake, we are using the page in isolation. Because no viewers currently support rotation. we have included here a picture of the page in its original orientation followed by its appearance according to the manifest's declaration for rotation.

Image of a codex page in its original orientation when reading conventionally:

![Image of a codex page in its original orientation when reading conventionally](https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-page1/full/300,/0/default.jpg "Before rotation")

Image showing the same codex page after rotating 90 degrees clockwise:

![Image showing the same codex page after rotating 90 degrees clockwise](https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-page1/full/300,/90/default.jpg "After rotation")

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Image Rotation with CSS][0039]

{% include acronyms.md %}
{% include links.md %}

