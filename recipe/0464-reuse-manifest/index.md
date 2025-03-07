---
title: Re-use a manifest
id: -1
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
topic: 
 - basic
---

## Use Case

I want to create a new Manifest based on parts of an existing Manifest that exists online, either to mix images from different Manifests into one presentation or to add metadata or Annotations to an existing presentation.

## Implementation Notes

A IIIF Presentation Manifest is a fixed document at a given URI with a given set of Canvases, Ranges, Metadata or Annotations. If you want to modify the Manifest to change the metadata description, remove or re-order images, add images from other Manifests or add Annotations to the images, you have to create a new Manifest and make it available at a new URI. 

In this new document you can copy elements of the source Manifest and add your modifications. There are some guidelines you should follow in the process:

You can copy the `label` property of the Manifest but you should modify it slightly to indicate what you have changed.

You should reproduce the `requiredStatement`, `rights` and `provider` properties that apply to the images or other resources that you copy from the source Manifest.

You should also copy the `metadata` property, particularly identifiers like library-ids to make it easier for users of your Manifest to identify the original object.

You should copy the Canvases keeping the URI in the `id` property unless you want to modify the Canvas itself. This indicates that your additions like Annotations would also apply to the original Canvas.



## Example

In this example we use the Canvas from the Manifest of the recipe [rights statement][0008] and we add an Annotation to the Canvas.

The new Manifest reproduces the `rights` and `requiredStatement` properties from the source Manifest and the original Canvas ids.

The original Manifest label "Picture of Göttingen taken during the 2019 IIIF Conference" has been modified to indicate that an Annotation has been added.

{% include manifest_links.html viewers="UV, Mirador, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

