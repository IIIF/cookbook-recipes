---
title: Recipe - Simplest Manifest - Audio
layout: recipe
tags: [annex, service, services, specifications]
cssversion: 2
---



# Simplest Manifest - Audio

## Use Case

The simplest viable manifest for audio content. This pattern presents a single audio file in a IIIF Presentation resource.

## Implementation notes

The implementation is identical to the [image example][mvm-image], except that the content is audio and the canvas has a duration instead of a height and width.

## Restrictions

None known.

## Example

This example shows a Manifest with a single Canvas that lasts for 3600 seconds, or exactly one hour. It has a single audio file (audio-sample.mp4) which is associated with it. The mp4 also has a duration of exactly one hour.

```jsonld
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.org/iiif/podcast1/manifest",
  "type": "Manifest",
  "label": { "en": [ "Audio Example 1" ] },
  "items": [
    {
      "id": "https://example.org/iiif/podcast1/canvas/segment1",
      "type": "Canvas",
      "duration": 3600,
      "items": [
        {
          "id": "https://example.org/iiif/podcast1/annotation/segment1/page",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://example.org/iiif/podcast1/annotation/segment1-audio",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "http://iiif.io/api/presentation/3/example/fixtures/resources/audio-sample.mp4",
                "type": "Sound",
                "format": "audio/mp4",
                "duration": 3600
              },
              "target": "https://example.org/iiif/podcast1/canvas/segment1"
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

{% include acronyms.md %}
{% include links.md %}
