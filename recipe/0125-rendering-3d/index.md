---
title: Including a 3D Rendering
id: 93
layout: recipe
tags: [tbc]
summary: "You want to include a 3D model representation"
---


## Use Case

You want to view an object from any orbital point of view or zoom level.
You want to view an object in augmented reality/XR in order to gain a better understanding of its dimensions and physical properties.

## Implementation notes

Add a [`rendering`](https://iiif.io/api/presentation/3.0/#rendering) to your manifest either at the root level, or any applicable child resource.
The rendering MUST have a dereferenceable `id` linking to the supplied 3D model, a `type` of `Model`, and a `label`.

## Restrictions


## Example

```json
{
  "@context": [
    "http://www.w3.org/ns/anno.jsonld",
    "http://iiif.io/api/presentation//context.json"
  ],
  "id": "https://example.org/iiif/book1/manifest",
  "type": "Manifest",
  "label": { "en": [ "Image 1" ] },
  "items": [
    {
      "id": "https://example.org/iiif/book1/canvas/p1",
      "type": "Canvas",
      "height": 1800,
      "width": 1200,
      "items": [
        {
          "id": "https://example.org/iiif/book1/page/p1/1",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://example.org/iiif/book1/annotation/p0001-image",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "http://iiif.io/api/presentation/2.1/example/fixtures/resources/page1-full.png",
                "type": "Image",
                "format": "image/png",
                "height": 1800,
                "width": 1200
              },
              "target": "https://example.org/iiif/book1/canvas/p1"
            }
          ]
        }
      ]
    }    
  ],
  "rendering": [
    {
      "id": "https://example.org/iiif/book1.glb",
      "type": "Model",
      "label": { "en": [ "Download as GLB" ] },
      "format": "model/gltf-binary"
    }
  ]
}
```

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}

