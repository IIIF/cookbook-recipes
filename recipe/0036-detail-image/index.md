---
title: Page with Detail Image
id: 36
layout: recipe
tags: [segmentation, complex-canvas]
summary: "Place one image on top of another - recombination"
---


## Use Case

Place one image on top of another.

Example: A page of a manuscript from which an illumination has been cut out. You have one image for the page of the manuscript, and other image for just the illumination. This manifest recombines the two.

(diagram?)

## Implementation notes

The presentation of images is upwards in a z-index from the first painting annotation encountered for all subsequent painting annotations. Thus the small 300 pixel square image is painted on top of the larger 1800x1200 image in the first annotation, rather than the other way around.

## Restrictions

None known.

## Example

A manifest with a single canvas that has two images painted on it. One is of the entire object, and one fills in a missing detail from the first image.

```jsonld
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.org/iiif/detail-image/manifest",
  "type": "Manifest",
  "label": { "en": [ "Detail Image" ] },
  "items": [
    {
      "id": "https://example.org/iiif/detail-image/canvas1",
      "type": "Canvas",
      "height": 1800,
      "width": 1200,
      "items": [
        {
          "id": "https://example.org/iiif/detail-image/canvas1/page1",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://example.org/iiif/detail-image/canvas1/page1/annotation1",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "https://iiif.io/api/presentation/3/example/fixtures/resources/image1.jpg",
                "type": "Image",
                "format": "image/jpeg",
                "height": 1800,
                "width": 1200
              },
              "target": "https://example.org/iiif/detail-image/canvas1"
            },
            {
              "id": "https://example.org/iiif/detail-image/canvas1/page1/annotation2",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "https://iiif.io/api/presentation/3/example/fixtures/resources/image-detail.jpg",
                "type": "Image",
                "format": "image/jpeg",
                "height": 300,
                "width": 300
              },
              "target": "https://example.org/iiif/detail-image/canvas1#xywh=100,100,300,300"
            }            
          ]
        }
      ]
    }    
  ]
}
```

(link to the same fixture but with image services)

Fixture 31(b)?

# Related recipes

* [Simple Image Manifest][link]


