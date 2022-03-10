---
title: Image Rotation Two Ways
id: 40
layout: recipe
tags: image, manipulation, service, CSS
summary: "Two approaches for rotating an image or annotation on a canvas"
viewers:
topic: 
 - basic
 - image
 - service
---

## Use Case

You have a codex that has been scanned and prepared for online display. The work was digitized by scanning single pages, and one page's image is mistakenly rotated 90 degrees. Rather than altering the original scanned files or re-scanning the work, you'd like to make an adjustment at the presentation level so viewers will display the page in the same layout as the other pages.

## Implementation Notes

There are two ways to direct a client to rotate a IIIF resource: By using an image service and by using CSS. Using an image service is the preferred way, 

### Image Service

In the image service section of your manifest, you must use an `@context` field in order to point to [the `ImageApiSelector` definition](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector) for canonical rotation options. The selector as defined must contain a `type` property whose value must be `ImageApiSelector`. The `rotation` property takes as its value just a positive numeric amount of rotation in degrees. For more  information about the selector and its use outside of rotation, read the full [selector document](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector).

Rotation of an image may be supported by your IIIF Image API server, and if so, using that service for rotation is a great way to handle changing the view of an image. To be able to support this recipe your Image API server must support the rotation requested in the selector. Rotation by 90º increments is mandatory for [level 2 IIIF Image API servers](https://iiif.io/api/image/3.0/compliance/#33-rotation) but can be implemented at all levels. Rotation by an arbitrary amount other than 90º, 180º, or 270º (360º being equal to 0º) is always optional, so you would need to familiarize yourself with what your image servers supports and look into the profile portion of the server's `info.json`.

This is true for [mirroring before rotation](https://iiif.io/api/image/3.0/#43-rotation), as this functionality is not mandatory at any level of image service IIIF compliance.

As well, though it is not described in this recipe, an image service may describe a region — rather than a whole Canvas — for rotation by using [the `region` property of the `ImageApiSelector`](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector).

### Cascading Style Sheets (CSS)

If your resource is not being served from an image server that supports the desired rotation (or rotation at all) through the IIIF Image API, then you can use CSS for the rotation. Using CSS for rotation depends on the viewer to rotate the image rather than the server. This approach is used when your image server does not have a IIIF Image API service for the image, or if your image server does not allow rotation through service calls.

By using CSS, you may specify arbitrary rotation figures as well as incorporate additional styling values.

Using CSS to alter resource presentation styles is not specified in the [IIIF Presentation 3.0 API](https://iiif.io/api/presentation/3.0/). This section is provided as a convenient but light explanation of this approach, but for a more detailed look at styles in Web Annotations, see [the W3C Web Annotation Data Model's Styles section](https://www.w3.org/TR/annotation-model/#styles).

## Restrictions

The service approach is not usable if you do not have a IIIF Image API service for the image, or if your image server does not allow rotation through service calls. Rotation amounts may only be available in 90º increments even if your image server supports rotation. Mirroring an image before rotation similarly may or may not be available from your image server.

The CSS approach depends wholly on viewer implementation of CSS as applied to a resource. Viewers have no requirement to support CSS styling.

## Example

For this recipe, we conveniently had a work on hand that had a page whose text direction was oriented perpendicularly to the facing page. For simplicity's sake, we are using the page in isolation. Because no viewers currently support rotation. we have included here a picture of the page in its original orientation followed by a picture of the page oriented according to the manifests' declarations for rotation.

Image of a codex page in its original orientation when reading conventionally:

![Image of a codex page in its original orientation when reading conventionally](https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-page1/full/300,/0/default.jpg "Before rotation")

Image showing the same codex page after rotating 90 degrees clockwise:

![Image showing the same codex page after rotating 90 degrees clockwise](https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-page1/full/300,/90/default.jpg "After rotation")

## Example 1: Using an Image Service

This Manifest shows how to rotate the image using an Image Service.

{% include manifest_links.html viewers="" manifest="manifest-service.json" %}

{% include jsonviewer.html src="manifest-service.json" config='data-line="32-51"' %}

## Example 2: CSS

This Manifest shows how to rotate the image using CSS. For clarity, we are using embedded CSS, but the `stylesheet` property may, rather than a JSON object with `type` and `value` properties, be a string URL pointing to an external stylesheet.

{% include manifest_links.html viewers="" manifest="manifest-css.json" %}

{% include jsonviewer.html src="manifest-css.json" config='data-line="30-51"' %}

## Related Recipes

* Get introduced to the use of Image Services with [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]

{% include acronyms.md %}
{% include links.md %}

