---
title: Reuse parts of a manifest
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

A [IIIF Presentation Manifest][prezi3] is a fixed document at a given URI with a given set of Canvases, Ranges, metadata or Annotations. If you want to modify the Manifest to change anything inside like the metadata description, remove or reorder images, add images from other Manifests or add Annotations to the images, you have to create a new Manifest and make it available at a new URI. 

To create this new document you can copy most elements of the source Manifest and add your modifications. There are some guidelines you should follow in the process:

You have to change the `id` property of the Manifest to match the URI that your published new Manifest will have.

You should copy the Canvases preserving the URI in their `id` property unless you modify the Canvas itself. This indicates that additions like Annotations made by you would also apply to the original Canvas in the source Manifest.

You can copy the `label` property of the Manifest but you should modify it to indicate what you have changed so that users of your new Manifest can easily differentiate it from the source Manifest.

You have to reproduce the `requiredStatement`, `rights` and `provider` properties that apply to the images or other resources that you copy from the source Manifest. If you combine resources from multiple Manifests you may have to combine these properties.

You should copy the `metadata` property, particularly identifiers like library-ids to make it easier for users of your Manifest to identify the original object. 

There is no formal way to reference the source Manifest but you are encouraged to add a metadata element that contains a link to the source Manifest and describes your changes.

You should be considerate of possible ethical implications of copying parts of an existing Manifest and try not to confuse users of your Manifest about intellectual or legal ownership.


## Example

In this example we reuse the Manifest of the recipe [rights statement][0008] and we add an Annotation to the Canvas.

The new Manifest reproduces the `rights` and `requiredStatement` properties from the source Manifest and the original Canvas ids.

The original Manifest label "Picture of Göttingen taken during the 2019 IIIF Conference" has been modified to indicate that an Annotation has been added and a metadata element with a link to the original Manifest and a note about the changes was added.

{% include manifest_links.html viewers="UV, Mirador, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Rights statement][0008] for the source Manifest and information on rights statements
* [Simplest Annotation][0266] for information on the Annotation used here

{% include acronyms.md %}
{% include links.md %}

