---
title: Simple Collection
id: 32
layout: recipe
tags: [presentation]
summary: ""
viewers:
 - UV
 - Mirador
 - Clover
topic:
 - basic
---

## Use Case

Your organization has a named digital collection of artworks authored by a specific person. Each of these unique items are already digital objects represented by Manifests and you would now like to organize and present them as an ordered IIIF Presentation resource.

## Implementation notes

This recipe illustrates the mandatory structure and properties of a IIIF Collection of Manifests, with the simplest possible content. 

Like with a Manifest, The JSON-LD of a Collection opens with the`@context` declaration, which identifies the terms used in the document as belonging to the IIIF specification. The `id` property identifies this collection with the URL at which it is available online. The `type` property must be `Collection`.

As with a Manifest, the `label` property is mandatory, and the language of its value must be given (or the special value `none`), using a [language map](https://iiif.io/api/presentation/3.0/#language-of-property-values). Here the language of the `label` is English and its value is “Simple Collection Example”.

The Collection `items` property is an array of referenced Manifests. In this example there are two Manifests. Each `items` entry must have an `id`, `type`, and a `label`. The `id` must be the URI where the Manifest can be available online. The `type` must be `Manifest` or a `Collection`. Each `items` entry referenced should not be full embedded into the Collection, and should contain only necessary properties for presentation of the collection such as thumbnail. Various other [descriptive](https://iiif.io/api/presentation/3.0/#31-descriptive-properties) and [linking](https://iiif.io/api/presentation/3.0/#33-linking-properties) properties such as `summary`, minimal `metadata`, and `homepage` may be useful as well for presentation. See the [Summary of property requirements](https://iiif.io/api/presentation/3.0/#a-summary-of-property-requirements) for a complete list.

Though this simple recipe is an ordered list of Manifests, Collections may also reference other Collections as sub-collections. IIIF Collections have no restrictions on the organizational purpose of their referenced resources, though the resources may be related as a named digital collection, a common metadata value, or be organized as search results.

## Restrictions


## Example

{% include manifest_links.html viewers="UV, Mirador, Clover" manifest="collection.json" %}

{% include jsonviewer.html src="collection.json" %}

# Related recipes

* [Multi Volume][0030]
* [Multiple Volumes in a Single Bound Volume][0031]
* [Basic Newspaper][0068]

{% include acronyms.md %}
{% include links.md %}
