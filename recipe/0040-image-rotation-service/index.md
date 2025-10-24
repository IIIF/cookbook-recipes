---
title: Image Rotation Two Ways
id: 40
layout: recipe
tags: image, manipulation, service, CSS
summary: "Two approaches for rotating an image or annotation on a canvas"
viewers:
topic: 
 - image
---

## Use Case

You have a codex that has been scanned and prepared for online display. The work was digitized by scanning single pages, and one page's image is mistakenly rotated 90 degrees. Rather than altering the original scanned files or re-scanning the work, you'd like to make an adjustment at the presentation level so viewers will display the page in the same layout as the other pages.

## Implementation Notes

There are two ways to direct a client to rotate a IIIF resource: By using an image service and by using CSS.

### Image Service

Rotation of an image may be supported by your IIIF Image API server, and if so, using the image service for rotation is a great way to handle changing the view of an image. To be able to support this recipe your Image API server must support the rotation requested in the selector. Rotation by 90º increments is mandatory for [level 2 IIIF Image API servers](https://iiif.io/api/image/3.0/compliance/#33-rotation) but can be implemented at all levels. Rotation by an arbitrary amount other than 90º, 180º, or 270º (360º being equal to 0º) is always optional, so you would need to familiarize yourself with what your image server supports and look into the profile portion of the server's `info.json`.

In the image service section of your manifest, you must use a `@context` field in order to point to [the `ImageApiSelector` definition](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector) for canonical rotation options. The selector as defined must contain a `type` property whose value must be `ImageApiSelector`. The `rotation` property takes as its value just a positive numeric amount of rotation in degrees. For more  information about the selector and its use outside of rotation, read the full [selector document](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector).

This is also true for [mirroring before rotation](https://iiif.io/api/image/3.0/#43-rotation), as this functionality is not mandatory at any level of image service IIIF compliance.

Finally, you may use an image service to rotate a region — rather than a whole Canvas — by using [the `region` property of the `ImageApiSelector`](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector).

### Cascading Style Sheets (CSS)

If your resource is not being served from an image server that supports the desired rotation (or rotation at all) through the IIIF Image API, then you can use CSS for the rotation. Using CSS for rotation depends on the viewer to rotate the image rather than the server. This approach is used when your image server does not have a IIIF Image API service for the image, or if your image server does not allow rotation through service calls.

By using CSS, you may specify arbitrary rotation figures as well as incorporate additional styling values. In order for the rotated image to line up properly with the Canvas, the `transform-origin` and `transform` CSS properties must have the correct value. Without claiming to be exhaustive, we can present suggestions for 4 common cases, with slight variations:
1. Reorienting a non-square rectilinear resource from portrait orientation to landscape orientation.
	1. If the right side of the original resource should be at the top, the CSS should be `transform-origin: Xpx Xpx; transform: rotate(-90deg);` where X is a value equal to half of the resource's smaller dimension.
	1. If the left side of the original resource should be at the top, the CSS should be `transform-origin: Xpx Ypx; transform: rotate(90deg) translateY(-Zpx);` where X is a value equal to half of the resource's smaller dimension, Y is a value equal to the resource's larger dimension less half of its smaller dimension, and Z is a value equal to the mathematical difference between the dimensions.
1. Reorienting a non-square rectilinear resource from landscape orientation to portrait orientation.
	1. If the right side of the original resource should be at the top, the CSS should be `transform-origin: Xpx Ypx; transform: rotate(90deg) translateX(-Zpx);` where X is a value equal to half of the resource's smaller dimension, Y is a value equal to the resource's larger dimension less half of its smaller dimension, and Z is a value equal to the mathematical difference between the dimensions.
	1. If the left side of the original resource should be at the top, the CSS should be `transform-origin: Xpx Xpx; transform: rotate(90deg);` where X is a value equal to half of the resource's smaller dimension.
1. Rotating a square image 90º or 270º and rotating any rectilinear image 180º. In this case, set the `transform-origin` value to the coordinates of the resource's center and the `transform` to be the correct rotation value.
1. Rotating other resources by other degree amounts/directions. Using the models above, manifest creators should have a start on how to craft CSS transformations, including setting an appropriate transformation point, but further discussion of other cases is outside the scope of this recipe.

Using CSS to alter resource presentation styles is not specified in the [IIIF Presentation 3.0 API](https://iiif.io/api/presentation/3.0/). The Presentation API section is provided as a convenient but light explanation of this approach. For a more detailed look at styles in Web Annotations, see [the W3C Web Annotation Data Model's Styles section](https://www.w3.org/TR/annotation-model/#styles).

### Rotation and Annotations

Resources in IIIF should be described using their authentic metadata, including their dimensions. Canvases should be dimensioned using your desired outcome. For an unrotated resource to be painted in its entirety on a Canvas, these dimensions should be identical. With a rotated resource (absent other manipulations), the dimensions will will be flipped. The `height` of the Canvas will be the `width` of the resource and likewise for the Canvas `width` and resource `height`. Annotations, therefore, will be at the desired coordinates only if these differences are kept in mind. If your annotations target a Canvas containing a rotated resource, ensure that these annotations work in the coordinate space of that Canvas rather than the resource's original coordinate space.

## Restrictions

The image service approach is not usable if you do not have a IIIF Image API service for the image, or if your image server does not allow rotation through service calls. Depending on your image server rotation support, rotation amounts may only be available in 90º increments. Mirroring an image before rotation similarly may or may not be available from your image server.

The CSS approach depends wholly on viewer implementation of CSS as applied to a resource. Viewers have no requirement to support CSS styling.

Be aware that values, especially `transform-origin` and translation, may differ meaningfully if other styling affecting the box model is applied. Translations may differ from the above in use of `translateX` or `translateY`, whether a translation has a positive value or negative value.

## Example

For this recipe, we conveniently had a work on hand that had a page whose text direction was oriented perpendicularly to the facing page. For simplicity's sake, we are using the page in isolation. Because no viewers currently support rotation, we have included here a picture of the page in its original orientation followed by a picture of the page oriented according to the manifests' declarations for rotation.

Image of a codex page in its original orientation when reading conventionally:

![Image of a codex page in its original orientation when reading conventionally](https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-page1/full/300,/0/default.jpg "Before rotation")

Image showing the same codex page after rotating 90 degrees clockwise:

![Image showing the same codex page after rotating 90 degrees clockwise](https://iiif.io/api/image/3.0/example/reference/85a96c630f077e6ac6cb984f1b752bbf-0-21198-zz00022840-1-page1/full/300,/90/default.jpg "After rotation")

## Example 1: Using an Image Service

This Manifest shows how to rotate the image using an Image Service.

{% include manifest_links.html viewers="" manifest="manifest-service.json" %}

{% include jsonviewer.html src="manifest-service.json" config='data-line="32-51"' %}

## Example 2: CSS

This Manifest shows how to rotate the image using CSS. For clarity, we are using embedded CSS. Note the declaration of the CSS class in the `value` property of the AnnotationPage's `stylesheet` and the application of that class to the `styleClass` property on the `body`. The `stylesheet` property may instead point to an external stylesheet using a URI in a string or an id and value in a JSON object. See [the W3C Web Annotation Data Model's Styles section](https://www.w3.org/TR/annotation-model/#styles) for more.

{% include manifest_links.html viewers="" manifest="manifest-css.json" %}

{% include jsonviewer.html src="manifest-css.json" config='data-line="30-51"' %}

## Related Recipes

* Get introduced to the use of Image Services with [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]

{% include acronyms.md %}
{% include links.md %}

