---
title: Recipe - Simplest Manifest - Video
layout: spec
tags: [annex, service, services, specifications]
cssversion: 2
---

This is a recipe from the [IIIF Cookbook][annex-cookbook].


# Simplest Manifest - Video

## Use Case

The simplest viable manifest for video content. This pattern presents a single video file in a IIIF Presentation resource.

## Implementation notes

The implementation is identical to the [image example][mvm-image], except that the content is video and the canvas has a duration in addition to a height and width.

The height and width of the video, in pixels, are given and here match the canvas dimensions exactly. The duration of the video, in seconds, also exactly matches that of the Canvas.  The `target` property tells us that the video is associated with the entirety of the canvas.

## Restrictions

None known.

## Example

```jsonld
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.org/iiif/video1/manifest",
  "type": "Manifest",
  "label": { "en": [ "Video Example 1" ] },
  "items": [
    {
      "id": "https://example.org/iiif/video1/canvas/segment1",
      "type": "Canvas",
      "width": 1920,
      "height": 1080,
      "duration": 3600,
      "items": [
        {
          "id": "https://example.org/iiif/video1/annotation/segment1/page",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://example.org/iiif/video1/annotation/segment1-video",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "http://iiif.io/api/presentation/3/example/fixtures/resources/video-sample.mp4",
                "type": "Video",
                "format": "video/mp4",
                "width": 1920,
                "height": 1080,
                "duration": 3600
              },
              "target": "https://example.org/iiif/video1/canvas/segment1"
            }
          ]
        }
      ]
    }    
  ]
}
```

# Related recipes

* [Simple Image Manifest][]
* [Simple Audio Manifest][]


{% include acronyms.md %}
{% include links.md %}

