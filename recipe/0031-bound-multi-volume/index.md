---
title: Multi-volume Work in a Single Bound Volume
id: 30
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

We have a multi-volume work which is bound together in a single volume. In this case, in contrast to a [multi-volume work with individually bound volumes][0030], we want to maintain the user experience of a single physical volume by grouping all of the volumes into a single Manifest and using Ranges.

## Implementation notes

To create a single IIIF resource for a multi-volume work, we can group the individual volume Manifests using a IIIF Collection. ... single Manifest and use Ranges to create a table of contents for navigating the multiple volumes. 

The approach you choose will depend on your specific use case or context. For example, if the volumes are bound together or if the desired end result is a more unified viewing experience, it is often desirable to group the volumes together as a single work while maintaining the user experience of separate volumes. For example, we might have separate Manifests for each volume, but prefer to maintain a single item record in our digital collection for the work as a whole, or to group the multi-volume work with other works as a single resource instead of as individual volumes. For this approach, consult the [Multi-volume Work with Individually-bound Volumes][0030] recipe.

*A note on metadata:* Since our Manifest in this use case represents a single multi-volume work with multiple volumes, the metadata describing the work is included in the Manifest, with volume-level metadata provided in the Ranges.

## Restrictions

None.

## Example

In this example, we have a Japanese book in two volumes. The first resource is a Collection representing the "work" with the `behavior` property value `multi-part` (lines 10-12). The two Manifests for each volume are included in the `items` property (beginning with line 13).

Following the Collection resource are the two Manifests for vol. 1 and vol. 2 that are included in the `items` property of the Collection. Note that these Manifests use the `behavior` property value `individuals`. The book volumes were imaged as two-page spreads, so should not be presented as `paged`. The default value of the `behavior` property is `individuals`, so the property could be omitted. Including the property makes it clear that this is intentional. For more information on the `behavior` property, see the [Book behavior (paging) variations][0011] recipe.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="collection.json" config='data-line="4, 10-12"' %}

# Related recipes

* [Book with Table of Contents][0024]
* [Multi-volume Work with Individually-bound Volumes][0030]
* [Paged Collections][0032]

{% include acronyms.md %}
{% include links.md %}