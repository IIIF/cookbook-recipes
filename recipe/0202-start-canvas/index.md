---
title: Load Manifest Beginning with a Specific Canvas
id: 202
layout: recipe
tags: [image]
summary: "This manifest uses the 'start' property to specify which Canvas the client should display on initialization of the resource."
viewers:
 - Mirador  
 - Annona
topic: 
 - image
 - property
property: start
---

## Use Case

In some cases, a book object will have front matter that most users would like to skip, such as blank pages (or perhaps shots of the binding and other non-textual views or color calibration images). In this recipe, we demonstrate using the `start` property to tell the presentation client to skip the initial Canvas (a blank page) and instead display the second Canvas (where the content begins) when loading the resource.

## Implementation Notes

This recipe extends [Multiple Related Images (Book, etc.)][0009] by adding the information required by a client to load the Manifest at a specific Canvas. This is done by adding the `start` property to the Manifest and specifying the Canvas the client should display on initialization.

The target of `start` must be a JSON object with `id` and `type` properties, where `type` can be either a Canvas or a Specific Resource with a Selector. In this use case, the target type property is a Canvas (`"type": "Canvas"`).

For an example of the `start` property using a Specific Resource with a Selector, see [Begin playback at a specific point - Time-based media][0015]. For more on the start property, see: [Start Property][prezi3-start].

## Example

This example shows a Manifest with multiple Canvases for a book object. The `start` property specifies loading the Manifest at the second Canvas. Note that all Canvases are still displayed in the viewer and the user is able to navigate back to the first Canvas using the viewer navigation controls.

{% include manifest_links.html viewers="Mirador,Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="10-13"'%}

## Related Recipes

* [Begin playback at a specific point - Time-based media][0015]
* [Multiple Related Images (Book, etc.)][0009]

{% include acronyms.md %}
{% include links.md %}
