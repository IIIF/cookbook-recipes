---
title: "Implementation note: Thumbnails"
id: 232
layout: recipe
tags: [image, presentation]
summary: "Implementation discussion for specifying thumbnails on Resources, such that they can be used by clients to represent the object."
---

## Use Case

This implementation note describes several approaches to specifying thumbnail images on resources in a IIIF Manifest using the `thumbnail` property.

While it is not always necessary to declare a thumbnail, there are several scenarios where the Presentation API 3.0 recommends the use of thumbnails:
* To provide a representative image for a Collection or a Manifest
* When a Canvas has multiple resources that make up the view
* When a content resource is an option in a Choice of resources

Additionally, while it is not necessary to declare a thumbnail on a Canvas since clients SHOULD render thumbnails from the Resource, doing so can increase the efficiency with which thumbnails load in a viewer. This is especially noticeable in Manifests that have many Canvases, such as books and manuscripts with many high-resolution images. In these cases, and where thumbnails are loaded into the viewer, the viewer is tasked with handling tile requests for all of the source images simultaneously – a resource-intensive task for any viewing client.

other options for mitigating performance issues, such as caching or pre-caching so the thumbnails are "pre-warmed" - but IIIF also allows publishers of Manifests to provide clues to the viewing client, directing it on how to process thumbnails. This implementation note focuses on outlining several approaches, especially in the context of Canvases, discussing their benefits and limitations, and providing recommendations to clients for processing thumbnails. For a more general introduction to thumbnails, see the [Image Thumbnail for Manifest][0117] recipe.

## Implementation Notes

### Minimal thumbnail requirements

At a minimum, the `thumbnail` property requires the `id` and `type` properties. It is highly recommended to include `format`, `height` and `width` properties as well.

```json
"thumbnail": [
  {
    "id": "https://example.org/img/thumb.jpg",
    "type": "Image",
    "format": "image/jpeg",
    "width": 100,
    "height": 100
  }
]
```
This configuration, however, is not ideal in most cases as it offers the client no size choice and, if the sizes provided are too small to meet the client's thumbnail requirements, this will have significant impact on processing time if the client is forced to do the resizing since it is more efficient to downsize an image than to request the perfect size. Likewise, if the client is required to upscale the image, it may introduce artefacts and look pixelated.

The configuration above would be appropriate in cases where the image used for the thumbnail is not a IIIF-image, such as thumbnails for A/V materials where publishers may not have a IIIF image server just for thumbnails.

### Thumbnails with a IIIF image service

For instances where the thumbnail is derived from a IIIF image, it is recommended that a [IIIF Image API](https://iiif.io/api/image/3.0/) service be included to allow the client more flexibility in choosing a thumbnail which fits into their interface. It is also possible to include additional [JSON image response](https://iiif.io/api/image/3.0/#51-image-information-request) properties, such as `sizes`, to optimize thumbnail generation and delivery. Below are three options, beginning with the most robust configuration.

*"Deep" IIIF service with an unspecified image service level*

This configuration provides sizes that are "pre-cached"

```json
"thumbnail":{
  "@id":"url_to_image",
  "type": "Image",
  "format": "image/jpg",
  "width":100,
  "height":100,
  "service":{
    "@id":"iiif_image_url",
    "type": "ImageService3",
    "profile": "level1",
    "width":5000,
    "height":5000,
    "sizes":[
      {
         "width":200,
         "height":200
      },
      {
         "width":500,
         "height":500
      }
    ]
  }
},
```
*"Deep" IIIF service with a level 0 image service*

```json
"thumbnail":{
  "@id":"url_to_image",
  "width":100,
  "height":100,
  "service":{
      "@id":"iiif_image_url",
      "profile":"https://iiif.io/api/image/3/level0.json",
      "width":5000,
      "height":5000,
      "sizes":[
         {
            "width":200,
            "height":200
         },
         {
            "width":500,
            "height":500
         }
       ]
  }
}
```

*"Shallow" IIIF service*

```json
"thumbnail":{
  "@id":"url_to_image",
  "width":100,
  "height":100,
  "service":{
     "@id":"iiif image url",
     "width":5000,
     "height":5000
  }
}
```


## Restrictions

## Example

{% include manifest_links.html viewers="Mirador, UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]
* [Image Thumbnail for Manifest][0117]
* [Implementation Note: Thumbnail Selection Algorithm][0012]

{% include acronyms.md %}
{% include links.md %}
