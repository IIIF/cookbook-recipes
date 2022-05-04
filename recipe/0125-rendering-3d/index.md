---
title: Including a 3D Rendering
id: 93
layout: recipe
tags: [tbc]
summary: "You want to include a 3D model representation"
viewers:
 - Mirador
 - UV
topic: property
property: rendering 
---

## Use Case

You want to view an object from any orbital point of view or zoom level.
You want to view an object in augmented reality/XR in order to gain a better understanding of its dimensions and physical properties.

## Implementation notes

Add a [`rendering`](https://iiif.io/api/presentation/3.0/#rendering) to your manifest either at the root level, or any applicable child resource.
The rendering MUST have a dereferenceable `id` linking to the supplied 3D model, a `type` of `Model`, and a `label`.

## Restrictions


## Example
{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="8-15"' %}



# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}

