---
title: Multi-volume work
id: 30
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

With multi-volume works, it is often desirable to group the volumes together as a single work while maintaining the user experience of separate volumes. For example, we might have separate Manifests for each volume, but prefer to maintain a single item record in our digital collection for the work as whole, or to group the multi-volume work with other works as a single resource instead of as individual volumes.

## Implementation notes

To create a single IIIF resource for a multi-volume work, we can group the individual volume Manifests using a IIIF Collection. A Collection is a IIIF resource that references other Manifests and Collections within its `items` property. To distinguish a multi-volume Collection from other Collection types, use the `behavior` property value `multi-part`. Using the `items` property, include the Manifests for each volume.

An alternative approach might be to combine the volumes into a single Manifest and use Ranges to create a table of contents for navigating the multiple volumes. For this approach, consult the [Book with Table of Contents][0024] recipe.

## Restrictions

Collections may be embedded inline within other Collections, such as when the Collection is used primarily to subdivide a larger one into more manageable pieces, however Manifests must not be embedded within Collections. An embedded Collection should also have its own URI from which the JSON description is available.

## Example

In this example, we have a Japanese book in two volumes. The first resource is a Collection representing the "work" with the `behavior` property value `multi-part` (lines 10-12). The two Manifests for each volume are included in the `items` property (beginning with line 13).

Following the Collection resource are the two Manifests for vol. 1 and vol. 2 that are included in the `items` property of the Collection.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="4, 10-12"' %}

{% include jsonviewer.html src="manifest_v1.json" %}

{% include jsonviewer.html src="manifest_v2.json" %}

# Related recipes

* [][]

{% include acronyms.md %}
{% include links.md %}
