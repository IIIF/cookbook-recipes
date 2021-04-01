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

Additionally, while it is not necessary to declare a thumbnail on a Canvas since clients SHOULD render thumbnails from the Resource, doing so can increase the efficiency with which thumbnails load in a viewer. This is especially noticeable in Manifests that have many Canvases, such as books and manuscripts with many high-resolution images. In these cases, and where thumbnails are loaded into the viewer, the viewer is tasked with handling tile requests for all of the source images simultaneously – a resource-intensive task for the image server.

other options for mitigating performance issues, such as caching or pre-caching so the thumbnails are "pre-warmed" - but IIIF also allows publishers of Manifests to provide clues to the viewing client, directing it on how to process thumbnails. This implementation note focuses on outlining several approaches, especially in the context of Canvases and with a focus on optimizing processing of thumbnail images, discussing their benefits and limitations, and providing recommendations to clients for processing thumbnails. For a more general introduction to thumbnails, see the [Image Thumbnail for Manifest][0117] recipe.

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
This configuration is not ideal in most cases as it offers the client no size choice and, if the sizes provided are too small to meet the client's thumbnail requirements, this will have significant impact on processing time if the client is forced to do the resizing since it is more efficient to downsize an image than to request the perfect size. Likewise, if the client is required to upscale the image, it may introduce artefacts and look pixelated.

The configuration above would be appropriate in cases where the image used for the thumbnail is not a IIIF-image, such as thumbnails for A/V materials where publishers may not have a IIIF image server just for thumbnails.

### Thumbnails with a IIIF image service

For instances where the thumbnail is derived from a IIIF image, it is recommended that a [IIIF Image API](https://iiif.io/api/image/3.0/) service be included to allow the client full flexibility in choosing a thumbnail which fits into their interface.

This approach might be a good option for Collection or Manifest thumbnails, but for Canvases this method alone would simply duplicate the image service for the Canvas resource and we gain nothing in terms of performance in cases where the client ignores the given thumbnail size in favor of the image service.

Since adding a service alone doesn't gain us anything, we can take it a step further by including all or a selection of pre-cached sizes from the [JSON image response](https://iiif.io/api/image/3.0/#51-image-information-request) and setting the profile to level 0. Advertising the appropriate pre-cached sizes ...  ... optimize thumbnail generation and delivery.

```json
"thumbnail":{
  "id":"url_to_image",
  "type": "Image",
  "format": "image/jpg",
  "width":100,
  "height":100,
  "service":{
    "id":"iiif_image_url",
    "profile": "https://iiif.io/api/image/3/level0.json",
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
In this configuration, one might expect the client to first try the given thumbnail size (100x100), then if too small, use one of the pre-cached images from the image service (200x200 or 500x500). Since we are using level 0, the client would choose the most appropriate size, probably something just larger, then downsize the image as needed...

Alternatively, we could change the image service profile to level 1. If none of the pre-cached sizes are appropriate, then the client could request a custom size if needed. Here, we are giving the client a few options to try before resorting to a custom image request, but ultimately the client may still request a custom image, in which case the thumbnail is essentially duplicating the service from the Canvas resource and not gaining anything in terms of performance.

```json
"thumbnail":{
  "id":"url_to_image",
  "width":100,
  "height":100,
  "service":{
      "id":"iiif_image_url",
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


## Restrictions

## Example

The Manifest below contains examples of the four options presented above: a Manifest thumbnail using the minimum recommended requirements, and three Canvases using the same source image, each with one of the three image service thumbnail configurations.

{% include manifest_links.html viewers="Mirador, UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]
* [Image Thumbnail for Manifest][0117]

{% include acronyms.md %}
{% include links.md %}
