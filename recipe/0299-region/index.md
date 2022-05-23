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

You have a digitized issue of a newspaper. From that digitized object, there is a single article that you would like to display on its own in a viewer, rather than highlighting it with an Annotation as part of the whole issue or even as part of a whole page.

## Implementation Notes

There are at least three ways to focus on or display a region of a IIIF image: Copy the original image and crop the copy to the desired dimensions, incorporate the whole image and use an Annotation to indicate the region, and point to the region in an independent manifest. The first option sidesteps the benefits of IIIF and walks right into one of the problems that IIIF aims to address, namely the proliferation of copies of high-quality images as an outgrowth of demand for the images. The second option weakens the user's attention on the article of interest, giving them much more information than what achieves your goals. The third option leaves the original image intact, sharpens users' focus on specific content, and by extension allows for concentrated attention on annotations to your specified content.

This recipe requires you to keep in mind two distinctions between a Canvas and a IIIF resource.

For one, to display only a region of a resource on your Canvas, the Canvas dimensions should relate to the region you want to display, not to the whole resource. Note, however (as discussed in [recipe 4][0004]) that the Canvas is a dimensionless set of coordinates. If desired, the dimensions of the Canvas may be different numeric values than the region you are displaying, but must be the same proportions if you want the region displayed with an  unchanged dimension ratio.

The other significant pertinent distinction is that the process used to retrieve the desired region uses a `selector` of type ImageApiSelector because the process uses the [IIIF Image API](https://iiif.io/api/image/). When addressing a portion of a Canvas, however, an Annotation would use a `selector` of type [FragmentSelector](https://www.w3.org/TR/annotation-model/#fragment-selector) because the Annotation is using the [IIIF Presentation API](https://iiif.io/api/presentation/3.0/#53-canvas) in conformance with the [W3C Web Annotation data model](https://www.w3.org/TR/annotation-model/).

In the interest of completeness, it should be noted that you can pull in a region of a IIIF image without using an Image service. 

When using an image service to retrieve a region of an image to display, the Annotation `body` containing the resource is constructed as a `SpecificResource` that in turn contains a `source` with the resource's details.

## Restrictions

No known restrictions

## Example

In this example we use an ImageApiSelector on the `body` of the Manifest's sole Annotation to retrieve a single article selection from the 16 February **[year]** issue of _Berliner Tageblatt_. The article discusses a meeting including Neville Chamberlain of Great Britain.

Note: Displaying a region of a Resource is not yet supported in viewers.

Level 0 implementation (+/- effective in Mirador only but here more for discussion): {% include manifest_links.html viewers="Mirador" manifest="manifest-level0.json" %}

{% include manifest_links.html viewers="Mirador, UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='14-15,25-46'" %}

## Related Recipes

* [Simple Image Manifest][0001]
* [Image and Canvas with Differing Dimensions][0004] for thinking through relative dimensioning of a resource and a Canvas
* [Introduction to IIIF Image Service][0005] for a basic example of image service use
* [Simple Annotation — Tagging][0021] to see the image region that should be displayed
* [Image Rotation Two Ways][0040] for another example of using a selector with a IIIF Image service

{% include acronyms.md %}
{% include links.md %}

