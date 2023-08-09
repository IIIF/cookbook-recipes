---
title: Missing Images in a Sequence
id: 283
layout: recipe
tags: [image, presentation]
summary: "Represent a missing image from a paged object in a sequence."
viewers:
 - UV
 - Mirador
 - Annona
 - Clover
topic:
 - image
 - basic
---

## Use Case

You have a paged object, such as a printed book or early manuscript, that has an image missing. You want to include a Canvas in the page flow to acknowledge the missing sequenced image and also to make sure the recto/verso paging functionality isn't thrown off by altogether eschewing a Canvas at the point of the missing image.

## Implementation notes

This recipe attempts to address desires to have a good user experience for people interacting with IIIF resources as well as for computational consumption of them. None of the manifest information described here is required by the IIIF Presentation API v3.0 but may bring benefits to your work. Nothing in the IIIF Presentation API v3.0 makes any provision for specifying that a Canvas replaces what is supposed to appear at that point of the page flow, as the API is agnostic both about your content and its semantics as well as any semantics of your manifest's structure.

For the purposes of this recipe, there are options worth considering for indicating a missing page:
+ Add a Canvas with a replacement image of comparable dimensions, especially with text stating explicitly that the original image is missing
+ Add a content-less Canvas with the minimum required properties (ID, type) and with dimensions for height and width
+ Add a dimensioned, resource-less Canvas with the minimum required properties and with an Annotation whose `motivation` is `supplementing` and whose content is an image stating explicitly that the original image is missing

Each of these options benefits from including a `label` on a Canvas representing a missing image, as well as the addition of robust metadata. (The IIIF Presentation API v3 strongly recommends including a `label` with every Canvas anyway.) Each of these can help both visual and non-visual users as well as computational consumers understand that the content is known to be missing.


### Benefits and Detriments

+ Inserting an image stating explicitly that an object image is missing is the clearest and most reliable visual acknowledgement by the manifest creator of the lacuna. Viewers that automatically generates thumbnails will allow visual users of the viewer to see at different scales that the image is missing. On the other hand, attention must still be paid, as with content resources, to ensuring that Canvas metadata contains sufficient information for non-visual users to understand the information communicated by the replacement image.
+ Using an empty Canvas is a very lightweight and authentic way to show missing content. That is, having a content-free Canvas parallels the lack of content from the digitization (for instance) of the real-world object. In this approach, however, there is neither visual nor metadata indications differentiating between known missing content and various software or workflow issues resulting in unknown missing content (server or network errors, automated digitization process errors, malformed file issues). 
+ Using an empty Canvas with an Annotation whose `motivation` is `supplementing` tries to combine the benefits of the first two approaches. Because an Annotation with that `motivation` should not appear visually, conforming viewers will show nothing of the Canvas, emphasizing the absence of content. At the same time, viewers can be expected to provide a means of reading the Annotation and thereby understanding the gap is not a presentation error.

### Additional Information

Though they are not being demonstrated in this recipe, selected Manifest and Canvas properties can be used in addition to give a person interacting with your content pointers to learn more about missing image(s). For instance, `homepage` can direct them to a webpage that talks about the object and its physical state, arbitrary `metadata` fields might be placed on the empty Canvases to give useful information in the viewer (keeping in mind that viewers are not required to display the metadata in any predictable way or at all), and `summary` could include a brief statement acknowledging the incomplete digital surrogate.

## Restrictions

No known restrictions.

## Example

For this example, we are using 6 views from a paged Ethiopic manuscript. The verso pages have been substituted with the three different ways of representing a missing image.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="50-81,122-131,172-202"' %}


# Related recipes

* [Simple Manifest - Book][0009]

{% include acronyms.md %}
{% include links.md %}
