---
title: Recipe - Segment of an Image
layout: spec
tags: [annex, service, services, specifications]
cssversion: 2
---

This is a recipe from the [IIIF Cookbook][annex-cookbook].

# Segment of an Image

## Use Case

You wish to select a rectangular part of the image and present it without any surrounding content. Examples are the ability to crop out the depiction of the frame from an image of a painting, or exclude the color calibration target from an image of a page.

This allows a single master image to be used for both usage scenarios of a page turner application that should not render the color bar for a page, and also for a digital conservation or research use case where the target is available.  Similarly, you could pull a small detail from a much larger image such as one item from a large contact sheet, when it is the only representation available of the object. 

diagram...

## Implementation notes

The client should not render the area of the image that is not selected by the annotation.


## Example


```jsonld
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.org/iiif/segment-image/manifest",
  "type": "Manifest",
  "label": { "en": [ "Segment Image" ] },
  "items": [
    {
      "id": "https://example.org/iiif/segment-image/canvas1",
      "type": "Canvas",
      "width": 1000,
      "height": 1600,
      "items": [
        {
          "id": "https://example.org/iiif/segment-image/canvas1/page1",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://example.org/iiif/segment-image/canvas1/page1/annotation1",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "https://iiif.io/api/presentation/3/example/fixtures/resources/image1.jpg#xywh=100,100,1000,1600",
                "type": "Image",
                "format": "image/jpg"
              },
              "target": "https://example.org/iiif/segment-image/canvas1"
            }           
          ]
        }
      ]
    }    
  ]
}
```


# Related recipes

* [Simple Image Manifest][link]

