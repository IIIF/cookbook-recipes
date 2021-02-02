---
title: Multi-volume work
id: 30
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

Why is this pattern important?

## Implementation notes

How does one implement the pattern?

## Restrictions

Collections may be embedded inline within other Collections, such as when the Collection is used primarily to subdivide a larger one into more manageable pieces, however Manifests must not be embedded within Collections. An embedded Collection should also have its own URI from which the JSON description is available.

## Example

In this example, we have a Japanese book in two volumes. The first Manifest is the Collection Manifest with the `behavior` property value `multi-part` (line 8). The two Manifests for each volume are included in the `items` property (beginning with line 11).

Following the Collection Manifest are the two book Manifests for vol. 1 and vol. 2 that are included in the `items` property of the Collection Manifest.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="4, 10-12"' %}

{% include jsonviewer.html src="manifest_v1.json" %}

{% include jsonviewer.html src="manifest_v2.json" %}

# Related recipes

* [][]

{% include acronyms.md %}
{% include links.md %}
