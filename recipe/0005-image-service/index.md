---
title: Basic Use of an Image Service
id: 5
layout: recipe
tags: [image, annex, service, services, specifications]
summary: "Paint a Canvas using an image with an associated IIIF Image API service."
---

## Use Case

You want to give a conforming client additional information about your image or allow it to exercise additional functionality with your image. With a sophisticated digital image, it makes sense to allow viewers the opportunity to study the image in many possible ways, a process facilitated by feeding the client specific data rather than relying on the client to discover the data. For instance, you might be able to note additional image sizes (for automatically generating a thumbnail, for instance) or to indicate additional image renderings such as grayscale or infrared.

## Implementation Notes

This property may attach to any IIIF resource type. The annotation structure follows that of the [Simplest Manifest - Image][0001] recipe. Within the `body` of the image annotation, specify the IIIF Image API service using the `service` property. The (required) `id` of the service is the base URI of the associated IIIF Image API service.  

The `type` property is also required, to tell the client what version of the Image API (1, 2, or 3) you are referencing. Values for `type` are defined in [the Presentation API][prezi3].  

Version 3 of the IIIF Presentation specification permits using these properties in their version 2 format: `@id` and `@type`. The latter property includes values for compatibility with other IIIF APIs. See [the specification](https://iiif.io/api/presentation/3.0/#service) for more information.

Image service properties should include a `profile` property, with a value representing the service's level of compliance with the IIIF Image specification. You may read more about service compliance level in the [Image API Compliance](https://iiif.io/api/image/3.0/compliance/) specification.

## Restrictions

None known.

## Example

{% include manifest_links.html viewers="UV,Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

# Related recipes

* [Simplest Manifest - Image][0001] demonstrates use of an image without a IIIF Image API service.

{% include acronyms.md %}
{% include links.md %}
