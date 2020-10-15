---
title: Add Image Thumbnail of Resource
id: 117
layout: recipe
tags: [image,presentation]
summary: "Display a thumbnail image for a resource, be that a canvas, a range, an audio file or a video, such that it can be clicked to activate that particular resource."
---

## Use Case

You have a booklet with multiple pages, one which your site visitors may not want to navigate through in its bound order, one view at a time. Having a set of smaller images, each of which can be clicked/tapped/activated to display the represented view, provides significant utility to researchers or casual viewers. The digital surrogate for the booklet proper is preceded by a view of the booklet cover with a color matching bar, so you don't want to use it for the thumbnail representing the entire booklet, instead using the cropped view of the front cover.

## Implementation Notes

Thumbnail images have multiple purposes, but the primary ones are to give your viewers an ability to navigate through your content without clicking/tapping through every view of the content, and to enable rapid loading of the images that facilitate this navigation. As a secondary benefit, thumbnails can permit non-human interfaces consuming your manifests to present representations of your content for rapid comprehension by human readers. For instance, this could be in a cross-institutional catalog website.

Thumbnails are strongly recommended for Collections and Manifests, and permitted on Canvases, content resources, and other resource types. Conforming clients are not required to render any thumbnails, though they are strongly recommended to do so when they exist for Collections, Manifests, Canvases, and content resources. Clients are permitted to render thumbnails when they exist for all other resource types. Each resource may contain multiple thumbnails, each of which may be — but are not required to be — of the same `type` and `format` as its containing resource. 

Three primary scenarios exist for describing a thumbnail in your manifest:
+ Using a IIIF Image Service with a full-size image URI; this makes most sense for a Collection or Manifest thumbnail, where the client's preferred images size is more unpredictable.
+ Using a IIIF URI only, but to a specified and modest size; this makes most sense for Canvases or other resource types, where the client can be predicted to prefer small images but still may rescale them. At the same time, you should aim for declaring thumbnail sizes larger than the final expected size, as the client will be able to downscale more efficiently than upscale.
+ As a flat image file of a specific size. Because III Image Servers facilitate significant additional client functionality, such as agile resizing of image resources, we only recommend this approach when you are engaged in rapid ad hoc use of a similarly flat file for the primary content.

It is also possible to adjust your IIIF Image server to privilege serving particular size images if you know what will be most frequently requested. (e.g. by your internal discovery software) Discussion of this is out of scope for this cookbook, however.

## Restrictions

None known.

## Example

This example uses the same kabuki performance program as in the recipe for [Viewing direction and its effect on navigation][0010], with the addition of an explicit `thumbnail` property for each view and a supplementary view at the beginning. If you look at that recipe's display in Mirador, you'll see thumbnails inferred from the main images' service entries, while Universal Viewer (as of this recipe's writing) does not infer them but does show broken image indicators for them. Declaring a thumbnail — with or without its own service property – moves you toward avoiding the behavior exhibited by Universal Viewer.

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Simplest Manifest - Image][0001]
* [Viewing direction and its effect on navigation][0010]
* [Implementation Note — Thumbnail Selection Algorithm][0012]

{% include acronyms.md %}
{% include links.md %}

