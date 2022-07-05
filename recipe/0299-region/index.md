---
title: Addressing a Region
id: 299
layout: recipe
tags: [fragment]
summary: "Presenting a region of an image independently"
viewers:
topic: 
 - basic
---

## Use Case

You have a digitized issue of a newspaper. From that digitized object, there is a single article that you would like to display on its own in a viewer, rather than highlighting it with an Annotation in the context of the whole issue or even just in the context of its complete page.

## Implementation Notes

There are at least three ways to focus on a region of a IIIF image or limit the display to a region: Crop a resource or copy of the resource to the desired dimensions, use an Annotation on the full resource to indicate the region, or point to the region in an independent manifest. The first option sidesteps the benefits of IIIF and walks right into one of the problems that IIIF aims to address, namely the proliferation of copies of high-quality images as uses for the image grows. The second option assumes that you and/or the user wants to see the article in context. The third option leaves the original image intact, sharpens users' focus on specific content, and by extension can facilitate concentrated attention on annotations to your specified content.

To display only a region of a resource on your Canvas, the Canvas dimensions should relate to the region you want to display, not to the whole resource. Note, however (as discussed in [recipe 4][0004]) that the Canvas is a dimensionless set of coordinates. If desired, the dimensions of the Canvas may be different numeric values than the region you are displaying, but must be the same proportions if you want the region displayed with an  unchanged dimension ratio.

When using the [IIIF Image API](https://iiif.io/api/image/) to retrieve only the desired region of a IIIF resource, the manifest uses a `selector` of type [ImageApiSelector](https://iiif.io/api/annex/openannotation/#iiif-image-api-selector) to pass the desired parameters to the IIIF Image service. In addition, when using an Image service to retrieve your intended region of a IIIF resource, the Annotation `body` containing the resource is constructed as a `SpecificResource` that in turn contains a `source` with the resource's details.

This recipe brings into relief the polyvocality of Annotations. On the one hand, the term and syntax is used to pull in to a viewer a IIIF resource and place it in a coordinate space. This sort of Annotation takes the `motivation` value of `painting`, leaning on a metaphor of painting the resource onto a Canvas. On the other hand, the term can be used to refer to IIIF content that marks in some way all or part of a Canvas and contributes additional data, usually in connection with a `painting`-type Annotation. Because these Annotations can have multiple values for their `motivation` property, we tend to refer to them not-very-cleverly as "non-painting Annotations".

*Why did we need this part, again?* To paint the region onto a specific portion of a Canvas, however, an Annotation would use a `selector` of type [FragmentSelector](https://www.w3.org/TR/annotation-model/#fragment-selector) because the Annotation is using the [IIIF Presentation API](https://iiif.io/api/presentation/3.0/#53-canvas) in conformance with the [W3C Web Annotation data model](https://www.w3.org/TR/annotation-model/).

In the interest of completeness, it should be noted that it is possible to pull in a region of a IIIF image without using an Image service. As with any IIIF use of a static image, the image will only be enlarged in the viewer, where an Image service offers among other benefits a download speed benefit of a tiled image, where the tiles are sized appropriate to zoom level.

## Restrictions

No known restrictions

## Examples

In this example we use an ImageApiSelector on the `body` of the Manifest's sole Annotation to retrieve a single article selection from the 16 February 1925 issue of _Berliner Tageblatt_. The article discusses a meeting including Neville Chamberlain of Great Britain.

Note: Displaying solely a region of a IIIF resource using an Image service is not yet supported in viewers.

### Level 0 implementation
(+/- effective in Mirador only but here more for discussion)
{% include manifest_links.html viewers="Mirador" manifest="manifest-level0.json" %}
{% include jsonviewer.html src="manifest-level0.json" config="data-line='14-15,22-32'" %}

### Full Image service implementation
{% include manifest_links.html viewers="Mirador, UV" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config="data-line='14-15,25-48'" %}

## Related Recipes

* [Simple Image Manifest][0001]
* [Image and Canvas with Differing Dimensions][0004] for thinking through relative dimensioning of a resource and a Canvas
* [Introduction to IIIF Image Service][0005] for a basic example of image service use
* [Simple Annotation — Tagging][0021] for an example of a non-`painting` Annotation
* [Image Rotation Two Ways][0040] for another example of using a selector with a IIIF Image service

{% include acronyms.md %}
{% include links.md %}

