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
 - Annona
topic:
 - basic
---

## Use Case

Your organization has a named collection of artworks authored by a specific person. Each of these unique items already has a digital representation and a Manifest, and you would now like to organize and present them together in a unified and coherent IIIF Presentation interface.

## Implementation notes

This recipe illustrates the mandatory structure and properties of a IIIF Collection of Manifests, with the simplest possible content. IIIF Collections have no restrictions on the organizational purpose of their referenced resources, though the resources may be related as a named digital collection, a common metadata value, or be organized as search results.

Like with a Manifest, the JSON-LD of a Collection opens with the`@context` declaration, which identifies the terms used in the document as belonging to the IIIF specification. The `id` property identifies this collection with the URL at which it is available online. The `type` property must be `Collection`.

As with a Manifest, the `label` property is mandatory, and the language of its value must be given (or the special value `none`), using a [language map](https://iiif.io/api/presentation/3.0/#language-of-property-values). Here the language of the `label` is English and its value is “Simple Collection Example”.

The Collection `items` property is an array of referenced Manifests. In this example there are two Manifests. Each `items` entry must have an `id`, `type`, and a `label`. The `id` must be the URI where the Manifest can be available online. The `type` must be `Manifest` or a `Collection`. Each `items` entry referenced should not be fully embedded into the Collection, and should contain only necessary properties for presentation of the collection such as `thumbnail`. Various other [descriptive](https://iiif.io/api/presentation/3.0/#31-descriptive-properties) and [linking](https://iiif.io/api/presentation/3.0/#33-linking-properties) properties such as `summary`, minimal `metadata`, and `homepage` may be useful as well for presentation. See the [Summary of property requirements](https://iiif.io/api/presentation/3.0/#a-summary-of-property-requirements) for a complete list.

Collections may also reference other Collections. 

Collections may have [`behavior`](https://iiif.io/api/presentation/3.0/#behavior) defined in order to influence user experience when viewing the resource. Manifests within a Collection DO NOT inherit behaviors from their referencing Collections; however referenced Collections will.

## Restrictions

Defining a IIIF Collection is to not be conflated with creating a table of contents within an individual Manifest. To define a table of contents, see [Multiple Volumes in a Single Bound Volume][0031].

## Example

{% include manifest_links.html viewers="UV, Mirador, Clover" manifest="collection.json" %}

{% include jsonviewer.html src="collection.json" %}

# Related recipes

* [Multi Volume][0030]
* [Multiple Volumes in a Single Bound Volume][0031]
* [Basic Newspaper][0068]

{% include acronyms.md %}
{% include links.md %}
