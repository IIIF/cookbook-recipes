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

For the purposes of this recipe, there are three acceptable options for indicating a missing page:
+ Add a Canvas with an image that states explicitly that the image is missing
+ Add a Canvas with the minimum required properties (ID, type) and with dimensions for height and width
+ Add a Canvas with the minimum required properties and with an Annotation carrying the `motivation` of `supplementing` and with an image stating explicitly that the image is missing

### Benefits and Detriments

+ Inserting an image stating explicitly that an object image is missing is the clearest visual acknowledgement by the manifest creator of the lacuna. Viewers that automatically generates thumbnails will allow visual users of the viewer to see at different scales that the image is missing. On the other hand, attention must still be paid, as with content resources, to ensuring that Canvas metadata contains sufficient information for non-visual users to understand what the missing page content is.
+ Using an empty Canvas is a very lightweight and authentic way to show missing content. That is, having a content-free Canvas parallels the lack of content from the digitization (perhaps) of the real-world object. In this approach, however, there is neither visual nor metadata indications differentiating between known missing content and various software or workflow issues resulting in unknown missing content (server or network errors, automated digitization process errors, malformed file issues). Robust metadata such as a `label` — which every Canvas should have anyway — can help both visual and non-visual users as well as computational consumers understand that the content is known missing.
+ Using an empty Canvas with an Annotation having a `motivation` of `supplementing` tries to combine the benefits of these two approaches. Because an Annotation with that `motivation` should not appear visually, conforming viewers will show nothing of the Canvas, emphasizing the absence of content. At the same time, viewers should provide a means of reading the Annotation and thereby understanding the gap is not a presentation error.

## Restrictions

No known restrictions.

## Example

For this example, we are using a paged Ethiopic manuscript. The verso pages have been substituted with the three different ways of representing a missing page.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="50-81"' %}


# Related recipes

* [Simple Manifest - Book][0009]

{% include acronyms.md %}
{% include links.md %}
