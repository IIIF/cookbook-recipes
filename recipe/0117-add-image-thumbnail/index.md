---
title: Add Image Thumbnail of Resource
id: 117
layout: recipe
tags: [image,presentation]
summary: "Display a thumbnail image for a resource, be that a canvas, a range, an audio file or a video, such that it can be clicked to activate that particular resource."
---

## Use Case

You have a booklet with multiple pages, one which your site visitors may not want to navigate through in its bound order, one view at a time. Having a set of smaller images, each of which can be clicked/tapped/activated to display the represented view, provides significant utility to researchers or casual viewers. 

## Implementation Notes

+ All thumbnails are arrays of JSON objects containing at least the `id` and `type` properties.
+ Resources may contain multiple thumbnails; for each resource, its thumbnails may have the same `type` and `format` as its containing resource, but may also have different ones.
+ Thumbnails are of most use when they are of modest size. This allows the client to pull them up rapidly and thence for the viewer to negotiate their intended destination rapidly.
+ Having a Service for each thumbnail facilitates clients' presentation of these images, whether for standardizing size or shape, or for using a fragment.
+ Thumbnails are strongly recommended for Collections and Manifests, and permitted on Canvases, content resources, and other resource types.
+ Clients are strongly recommended to render thumbnails when they exist for Collections, Manifests, Canvases, and content resources. Clients are permitted to render thumbnails when they exist for other resource types.


## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.? 

Delete this section if it is not needed.
If you don't know what the restrictions might be initially, just leave the following line:
**Unknown - Help Needed**

## Example

This example uses the same kabuki performance program as in the recipe for [Viewing direction and its effect on navigation][0010], with the addition of an explicit `thumbnail` property for each view. If you look at Recipe 10's display in Mirador, you'll see thumbnails inferred from the main images' service entries, while Universal Viewer (as of this recipe's writing) does not infer them but does show broken image indicators for them. Declaring a thumbnail — with or without its own service property – moves you toward avoiding the issue manifested by Universal Viewer.

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Simplest Manifest - Image][0001]
* [Viewing direction and its effect on navigation][0010]
* [Implementation Note — Thumbnail Selection Algorithm][0012]

{% include acronyms.md %}
{% include links.md %}

