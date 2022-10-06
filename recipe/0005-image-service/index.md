---
title: Support Deep Viewing with Basic Use of a IIIF Image Service
id: 5
layout: recipe
tags: [image, annex, service, services, specifications, transitional]
summary: "Paint a Canvas using an image with an associated IIIF Image API service."
viewers:
 - Mirador
 - Annona
topic: 
 - basic 
 - image
---

## Use Case

You have a rare or special object in your collection that you'd like to make available for research to a large audience, including those without the ability to be present at your institution to examine the object in person. Presenting a medium-resolution flat digital image of the object using IIIF is [possible][0001], but if you have implemented a [IIIF Image API](https://iiif.io/api/image/) service, you have significantly enhanced interaction possibilities for research and engagement. Specifying a IIIF Image API service in your presentation manifest allows for, among other features, proper deep zooming of large high-resolution images, client generation of derivatives, annotation of and external reference to image fragments, image rotation, choice of colors, creation of image fragments for annotation, and more. In turn, this permits researchers more sophisticated inspection of the object and more possibilities for stable, durable, and discoverable image-based scholarship.

## Implementation Notes

A service may be attached to any IIIF resource type, and requires at minumum the use of `id` and `type`. The annotation structure follows that of the [Simplest Manifest - Image][0001] recipe. Within the `body` of the image annotation, specify the IIIF Image API service using the `service` property. The service's `id` property value is the base URI of that IIIF Image API service. 

The `type` tells the client what version of the IIIF Image API (1, 2, or 3) you are referencing. Values for `type` are defined in [the IIIF Registry of Services][service-registry] and include values for compatibility with other IIIF APIs. See [the service property in the IIIF Presentation specification][prezi3-service] for more information.

Image service properties should include a `profile` property, with a value representing the service's level of compliance with the IIIF Image specification. You may read more about service compliance level in the [Image API Compliance](https://iiif.io/api/image/3.0/compliance/) specification.

As an optimisation you may want to include all of the info.json content (excluding the @context) as the content of the service sections of your manifest. Doing so allows clients to take selected actions, such as choosing an appropriate thumbnail, without making separate requests to the service.

## Restrictions

Though a version 3 Manifest may specify a service using the version 2 `@id` and `@type` property formats, these are only to be used when you are specifying an image service that itself is version 2. See [recipe 75][0075] for more on this topic.

## Example

{% include manifest_links.html viewers="Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="36-42"' %}

# Related recipes

* [Simplest Manifest - Image][0001] demonstrates use of an image without a IIIF Image API service.
* [Add Image Thumbnail][0117] discusses {how to work with thumbnail images}
* [Presentation version 3 manifest containing images on a version 2 service][00XX] forms part of the recipes connected with upgrading your offerings from v2 to v3.
* [Services][0055]

{% include acronyms.md %}
{% include links.md %}
