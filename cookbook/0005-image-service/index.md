---
title: Recipe - Simple Manifest - Image with IIIF Image API Service
layout: spec
tags: [annex, service, services, specifications]
cssversion: 2
---

This is a recipe from the [IIIF Cookbook][annex-cookbook].


# Simple Manifest - Image with IIIF Image API Service

## Use Case

Annotate a Canvas using an image with an associated IIIF Image API service.

## Implementation notes

The annotation structure follows that of the [Simplest Manifest - Image] recipe. Within the `body` of the image annotation, specify the IIIF Image API service using the `service` property. The `id` of the service is the base URI of the associated IIIF Image API service.    

## Restrictions

None known.

## Example

``` json-doc
{
  "@context": [
    "http://www.w3.org/ns/anno.jsonld",
    "http://iiif.io/api/presentation/{{ page.major }}/context.json"
  ],
  "id": "https://example.org/iiif/book5/manifest",
  "type": "Manifest",
  "label": { "en": [ "Simple Manifest - Image with IIIF Image API Service" ] },
  "items": [
    {
      "id": "https://example.org/iiif/book5/canvas/p1",
      "type": "Canvas",
      "height": 1800,
      "width": 1200,
      "items": [
        {
          "id": "https://example.org/iiif/book5/page/p0001/1",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://example.org/iiif/book5/annotation/p0001-image",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "https://example.org/resources/book5-p0001.jpg",
                "type": "Image",
                "format": "image/jpeg",
                "service": [
                    {
                        "id": "https://example.org/image/book5-p0001",
                        "type": "ImageService3",
                        "profile": "level2"
                    }
                ],
                "height": 1800,
                "width": 1200
              },
              "target": "https://example.org/iiif/book5/canvas/p1"
            }
          ]
        }
      ]
    }    
  ]
}
```

# Related recipes

[Simplest Manifest - Image] demonstrates use of an image without a IIIF Image API service.

{% include acronyms.md %}
{% include links.md %}

