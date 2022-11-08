---
title: Addressing a Spatial Region
id: 299
layout: recipe
tags: [fragment]
summary: "Presenting a spatial region of a IIIF image resource independently"
viewers:
topic:
 - basic
---

## Use Case

You have a digitized issue of a newspaper. From that digitized object, there is a single article that you would like to display on its own in a viewer, rather than highlighting it with an Annotation in the context of the whole issue or even just in the context of its complete page.

## Implementation Notes

You can focus on a region of a IIIF image or limit the display to a region in a few ways. This recipe focuses on one, but will describe the others briefly at the end. The way this recipe will address is that of pointing to the region of interest in a separate and independent manifest from the resource's primary IIIF manifest. Approaching the use case this way leverages the abilities of IIIF to leave the original image intact, sharpens users' focus on specific content, and by extension facilitates concentrated attention on annotations to the specified content.

To retrieve only a region of a IIIF resource, create an Annotation whose `body` contains the resource as a [`SpecificResource`](https://www.w3.org/TR/annotation-model/#specific-resources) type. The  `source` contains the resource's details and a `selector` of type [ImageApiSelector](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector) describes the region in a `region` property. The `region` value is the starting point and dimensions of the desired region, either as `x,y,w,h` (originating coordinates, width, and height) or as `pct:x,y,w,h` (originating coordinates, region width, and region height *as percentages of the original resource*).

Set the Canvas dimensions to equal the region you want to display, not the whole resource, to be sure the resource region displays in its original proportions. The region will be transformed as needed to fit the Canvas — enlarged or shrunk proportionally, or stretched or sqeezed disproportionally. (For more on the relationship of Canvas values and resource values, see [Image and Canvas with Differing Dimensions][0004].)

This recipe brings into relief the polyvocality of the term "Annotation". On the one hand, the term and the IIIF construct can refer to presenting a IIIF resource or part of one in a viewer. This sort of Annotation, as in this recipe, takes the `motivation` value of `painting` and are conventionally called "painting Annotations". The term can also be used to refer to associating additional data with all or part of a IIIF resource painted onto a Canvas. Because these latter kind of Annotations can have multiple values for their `motivation` property, they are frequently labeled "non-painting Annotations" as a group.

As mentioned above, there are other methods of drawing attention to a region of a IIIF resource:
+ **Copy and Crop**: Duplicate the image file you are working from, crop it in an image editor directly to the desired dimensions, and use this derived image's URI in the Manifest. This method sidesteps the benefits of IIIF and walks right into one of the problems that IIIF aims to address, namely the proliferation of copies of high-quality images as image re-use grows.
+ **Annotation**: Create an Annotation on the full resource to tag the region. This method leaves the region in its resource context and allows you to draw attention to multiple regions without creating a new manifest for each.
+ **Content State**: Use the Content State API with a viewer to show the region. With a valid Content State URI and a IIIF viewer that works with Content State
+ **Static Image**: Skip using an Image service and refer to an image directly, appending a `#xywh` fragment identifier to the image URI. As with any IIIF use of a static image, the image will only be enlarged in the viewer, where an Image service offers among other benefits the download speed benefit of a tiled image, where the tiles are sized appropriate to zoom level and only delivered to the viewer when requested by the browser.

## Restrictions

This recipe can not be applied to pulling a temporal segment from a time-based IIIF resource or to specifying a non-rectangular spatial region of an image. Incorporating a temporal region would use `FragmentSelector` and a non-rectangular region would use `SvgSelector`, but further description is beyond this recipe. However, see ["Table of Contents for Multiple A/V Files on a Single Canvas"](https://preview.iiif.io/cookbook/0299-region/recipe/0064-opera-one-canvas/) for an implementation example.

## Examples

In this example we use an ImageApiSelector on the `body` of the Manifest's sole Annotation to retrieve a single article selection from the 16 February 1925 issue of _Berliner Tageblatt_. The article discusses a meeting including Neville Chamberlain of Great Britain.

{% include manifest_links.html manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config="data-line='14-15,25-48'" %}

## Related Recipes

* [Simple Image Manifest][0001]
* [Image and Canvas with Differing Dimensions][0004] for thinking through relative dimensioning of a resource and a Canvas
* [Introduction to IIIF Image Service][0005] for a basic example of image service use
* [Simple Annotation — Tagging][0021] for an example of a non-`painting` Annotation
* [Image Rotation Two Ways][0040] for another example of using a selector with a IIIF Image service
* [Table of Contents for Multiple A/V Files on a Single Canvas][0064] for using a timecode fragment selector

{% include acronyms.md %}
{% include links.md %}
