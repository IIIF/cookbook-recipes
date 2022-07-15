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

There are at least three ways to focus on a region of a IIIF image or limit the display to a region: Crop a resource or copy of the resource to the desired dimensions, use an Annotation on the full resource to indicate the region, or point to the region in an independent manifest. The first option sidesteps the benefits of IIIF and walks right into one of the problems that IIIF aims to address, namely the proliferation of copies of high-quality images as image re-use grows. The second option assumes that you and/or the user wants to see the article in context. The third option leverages the abilities of IIIF to leave the original image intact, sharpen users' focus on specific content, and by extension facilitate concentrated attention on annotations to the specified content.

To display only a region of a resource on your Canvas, set the Canvas dimensions to the region you want to display, not to the whole resource. Note, however (as discussed in [recipe 4][0004]) that the Canvas is a dimensionless set of coordinates. If desired, the dimensions of the Canvas may be different numeric values than the region you are displaying, but must be the same proportions if you want the region displayed with an  unchanged dimension ratio.

When using the [IIIF Image API](https://iiif.io/api/image/) to retrieve only a region of a IIIF resource, the manifest uses a `selector` of type [ImageApiSelector](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector) to pass the desired parameters to the IIIF Image service. When transmitting coordinates and dimensions for the region, note that the `region` property of the selector takes only those values, comma-separated, rather than the values in addition to a parameter type as the `FragmentSelector` uses. In addition, when using an Image service to retrieve your intended region of a IIIF resource, the Annotation `body` containing the resource is constructed as a [`SpecificResource`](https://www.w3.org/TR/annotation-model/#specific-resources) containing in turn a `source` with the resource's details.

The pattern implied by this recipe can be applied to pulling a temporal segment from a IIIF audio or video resource into a separate Manifest, or to grabbing a non-rectangular spatial region. The main difference is, in principle, the selector used to identify the temporal segment or non-rectangular spatial region. In the first case, you would need to use the `FragmentSelector` and in the second case, you would need to use the `SvgSelector`. Further discussion of these implementations,however, is out of scope for this recipe.

This recipe brings into relief the polyvocality of the term "Annotation". On the one hand, the term and the IIIF construct refers to pulling in to a viewer a IIIF resource and placing it in a coordinate space. This sort of Annotation takes the `motivation` value of `painting`, using a metaphor from the arts to describe placing the resource onto a Canvas, and therefore are usually called "painting Annotations". On the other hand, the term can be used to refer to IIIF content that marks all or part of a Canvas and contributes additional data. Because these latter kind of Annotations can have multiple values for their `motivation` property, they are frequently labeled "non-painting Annotations" as a group.

In the interest of completeness, it should be noted that it is possible to pull in a region of a IIIF image without using an Image service. As with any IIIF use of a static image, the image will only be enlarged in the viewer, where an Image service offers among other benefits the download speed benefit of a tiled image, where the tiles are sized appropriate to zoom level and only delivered to the viewer when requested by the browser.

## Restrictions

No known restrictions

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

{% include acronyms.md %}
{% include links.md %}

