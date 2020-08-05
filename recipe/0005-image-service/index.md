---
title: Basic Use of an Image Service
id: 5
layout: recipe
tags: [annex, service, services, specifications]
summary: "[TBD]"
---

## Use Case

Paint a Canvas using an image with an associated IIIF Image API service.

## Implementation Notes

The annotation structure follows that of the [Simplest Manifest - Image] recipe. Within the `body` of the image annotation, specify the IIIF Image API service using the `service` property. The `id` of the service is the base URI of the associated IIIF Image API service.  

The `type` property is mandatory. Image API version 1 and 2 services may be referenced using the `type` values defined in the Presentation API[#service].  

## Restrictions

None known.

## Example

{% include manifest_links.html viewers="UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

# Related recipes

* [Simplest Manifest - Image][0001] demonstrates use of an image without a IIIF Image API service.

{% include acronyms.md %}
{% include links.md %}
