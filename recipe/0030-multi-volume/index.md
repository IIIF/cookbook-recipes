---
title: Multi-volume Work with Individually-bound Volumes
id: 30
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
 - UV
 - Mirador  
 - Annona
topic: structure
---

## Use Case

With multi-volume works, it is often desirable to group the volumes together as a single work while maintaining the user experience of separate volumes. For example, we might have separate Manifests for each volume, but prefer to maintain a single item record in our digital collection for the work as a whole, or to group the multi-volume work with other works as a single resource instead of as individual volumes.

## Implementation notes

To create a single IIIF resource for a multi-volume work, we can group the individual volume Manifests using a IIIF Collection. A Collection is a IIIF resource that references other Manifests and Collections within its `items` property. To distinguish a multi-volume Collection from other Collection types, use the `behavior` property value `multi-part`. Include the Manifests for each volume using the `items` property.

An alternative approach might be to combine the volumes into a single Manifest and use Ranges to create a table of contents for navigating the multiple volumes. The approach you choose will depend on your specific use case or context. For example, if the volumes are bound together or if the desired end result is a more unified viewing experience, the single Manifest approach might be the preferred option. For this approach, consult the [Multiple Volumes in a Single Bound Volume][0031] recipe.

*A note on metadata:* Since our Collection in this use case represents a single work with multiple volumes and the Collection is intended for display at the work level, the metadata describing the work is included in the Collection, with little metadata provided in the Manifests for the volumes. You could opt to include more metadata in the volume Manifests if the intended viewing experience necessitates it.

## Restrictions

Collections may be embedded inline within other Collections, such as when the Collection is used primarily to subdivide a larger one into more manageable pieces, however Manifests must not be embedded within Collections. An embedded Collection should also have its own URI from which the JSON description is available.

## Example

In this example, we have a Japanese book in two volumes. The first resource is a Collection representing the "work" with the `behavior` property value `multi-part` (lines 10-12). The two Manifests for each volume are included in the `items` property (beginning with line 13).

Following the Collection resource are the two Manifests for vol. 1 and vol. 2 that are included in the `items` property of the Collection. Note that these Manifests use the `behavior` property value `individuals`. The book volumes were imaged as two-page spreads, so should not be presented as `paged`. The default value of the `behavior` property is `individuals`, so the property could be omitted. Including the property makes it clear that this is intentional. For more information on the `behavior` property, see the [Book behavior (paging) variations][0011] recipe.

**Example Collection for the multi-volume work *青楼絵本年中行事 [Seirō ehon nenjū gyōji]*:**

{% include manifest_links.html viewers="UV, Mirador, Annona" manifest="collection.json" %}

{% include jsonviewer.html src="collection.json" config='data-line="4, 10-12"' %}

**Example Manifest for vol. 1 of *青楼絵本年中行事 [Seirō ehon nenjū gyōji]*:**

{% include manifest_links.html viewers="UV, Mirador, Annona" manifest="manifest_v1.json" %}

{% include jsonviewer.html src="manifest_v1.json" %}

**Example Manifest for vol. 2 of *青楼絵本年中行事 [Seirō ehon nenjū gyōji]*:**

{% include manifest_links.html viewers="UV, Mirador, Annona" manifest="manifest_v2.json" %}

{% include jsonviewer.html src="manifest_v2.json" %}

# Related recipes

* [Book with Table of Contents][0024]
* [Paged Collections][0032]
* [Multiple Volumes in a Single Bound Volume][0031]

{% include acronyms.md %}
{% include links.md %}
