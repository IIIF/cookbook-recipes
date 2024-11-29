---
title: Sharing a link for opening two or more Canvases
id: 540
layout: recipe
tags: [annotation, content-state]
summary: "Allows users to use Content State API to open two canvases at the same time."
viewers:
topic:
 - content-state
---

## Use Case

I want to compare pages from two different manuscripts and share a link to open both on the same view. I want to share a link to a colleague showing two similar paintings in two different collections. I want to save my current workspace (open Canvases in the current viewer) for later use. I want to open my current workspace with another viewer.

## Implementation Notes

Some viewers already implement custom formats for exporting the current workspace for sharing or later use. Content State API could be used for the same purpose, adding the advantage of direct loading of the workspace using a crafted link with the `iiif-content` query parameter. The [multiple targets for a comparison view section](https://iiif.io/api/content-state/1.0/#53-multiple-targets-for-a-comparison-view) describes a method for targetting two Canvases at the same time; each Canvas could be from a different Manifest.

For this purpose, we create an Annotation with `motivation` set to `["contentState"]`.
The value of the the `target` attribute of the Annotation is a list containing the `id` of the Canvases and a `partOf` attribute with the `id` of the Manifests they belong to.

We can hence encode the Annotation as explained in the [Content State encoding guidelines](https://iiif.io/api/content-state/1.0/#6-content-state-encoding), and then pass the encoded string to the viewer as the value of the `iiif-content` query parameter.

## Restrictions

None known.

## Example
In this example we want to compare two painting of the Colosseum from two different Manifests.
One of the two Manifest is available at the following [link](manifest.json). We can notice that the Colosseum painting is in the second Canvas. The other Manifest is from another recipe, and can be [accessed here](https://iiif.io/api/cookbook/recipe/0318-navPlace-navDate/manifest-2.json).

The Annotation will target the `id` of the two Canvases we want to compare and contain a reference to the two Manifests as shown in the example:

{% include content-state-viewers.html iiif-content="annotation.json" viewers="" %}

{% include jsonviewer.html src="annotation.json" %}

The expected result should show the two Canvases of the two Manifest depicting the Colosseum.

## Related Recipes

* [Simplest Manifest - Image][0001] shows the basic structure of a IIIF Manifest using Presentation API 3.0.
* [A simple book][0009] shows the manifest structure.
* [Link for loading a manifest][0466] another example of Content State API.

{% include acronyms.md %}
{% include links.md %}

