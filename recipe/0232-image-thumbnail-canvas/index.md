---
title: "Implementation discussion: Thumbnails"
id: 232
layout: recipe
tags: [image, presentation]
summary: "Implementation discussion for specifying thumbnails on Resources, especially Canvases, such that they can be used by clients to represent the object."
---

## Use Case

This implementation note describes several approaches to specifying thumbnail images on resources in a IIIF Manifest using the `thumbnail` property.

While it is not always necessary to declare a thumbnail, there are several scenarios where the Presentation API 3.0 recommends the use of thumbnails:
* To provide a representative image for a Collection or a Manifest
* When a Canvas has multiple resources that make up the view
* When a content resource is an option in a Choice of resources

Presentation API 3.0 does not explicitly recommend the use of thumbnails for Canvases in general since most viewing clients render thumbnails from the resource; however, it can be advantageous to declare thumbnails on Canvases in order to increase the efficiency with which thumbnails load in a viewer. This is especially noticeable in Manifests that have many Canvases, such as books and manuscripts with many high-resolution images. In these cases, and where thumbnails are loaded into the viewer, the viewer is tasked with handling tile requests for all of the source images simultaneously – a resource-intensive task for the image server.

There are options for mitigating such performance issues, such as pre-caching select image sizes to make available "pre-warmed" thumbnail images, and the `thumbnail` property allows publishers of Manifests to provide more explicit directions to the viewing client on how to process thumbnails. This implementation discussion focuses on outlining the most efficient methods for declaring thumbnails on Canvases in order to optimize processing and rendering. The recommendations here are intended to guide both publishers of Manifests and developers of viewing clients. While the examples here are intended to optimize processing of thumbnails on Canvases, they work equally well for other IIIF Resource types (Manifests, Collections, etc.). For a more general introduction to thumbnails, see the [Image Thumbnail for Manifest][0117] recipe.

## Implementation Notes

### Minimal thumbnail requirements

At a minimum, the `thumbnail` property requires the `id` and `type` properties. It is highly recommended to include `format`, `height` and `width` properties as well.

```json
"thumbnail": [
  {
    "id": "https://fixtures.iiif.io/video/indiana/donizetti-elixir/act1-thumbnail.png",
    "type": "Image",
    "format": "image/png",
    "height": 360,
    "width": 640
  }
]
```
This configuration is not ideal in most cases as it offers the client no size choice and, if the sizes provided are too small to meet the client's thumbnail requirements, this will have significant impact on processing time if the client is forced to do the resizing since it is more efficient to downsize an image than to request the perfect size. Likewise, if the client is required to upscale the image, it may introduce artefacts and look pixelated.

The configuration above would be most appropriate in cases where the image used for the thumbnail is not a IIIF-image, such as thumbnails for A/V materials where publishers may not have a IIIF image server just for thumbnails.

### Thumbnails with a IIIF image service

For instances where the thumbnail is derived from a IIIF image, it is recommended that a [IIIF Image API](https://iiif.io/api/image/3.0/) service be included to allow the client full flexibility in choosing a thumbnail which fits into their interface. For an example of this method, see the [Image Thumbnail for Manifest][0117] recipe.

This approach might be a good option for Collection or Manifest thumbnails, but for Canvases this method alone would simply duplicate the image service for the Canvas resource and we gain nothing in terms of performance in cases where the client ignores the given thumbnail size in favor of the image service.

### Thumbnails with a IIIF image service + JSON image response sizes

Since adding a service alone doesn't gain us anything, we can take it a step further by including all or a selection of pre-cached sizes from the [JSON image response](https://iiif.io/api/image/3.0/#51-image-information-request) and setting the profile to level 0. Advertising the appropriate pre-cached sizes provides the viewing client with a list of available size options that it can retrieve instead of using the image service, thereby optimizing thumbnail generation and delivery.

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
}
```
In this configuration, we might expect the client to first try the given thumbnail size (100x100), then if too small, use one of the pre-cached images from the image service (200x200 or 500x500). Since we are using level 0, the client ideally would choose the most appropriate size, probably something just larger, then downsize the image as needed to best fit the view.

Alternatively, we could change the image service profile to level 1. In this case, if none of the pre-cached sizes are appropriate, then the client could still request a custom size where needed. Here, we are giving the client a few options to try before resorting to a custom image request, but ultimately the client may still request a custom image, in which case the `thumbnail` property is again essentially duplicating the service from the Canvas' Resource; however, this option would ensure that an appropriate thumbnail size was selected in cases where the supplied sizes are not optimal for the thumbnail view.

## Restrictions
None

## Example

The Manifest below contains examples of the three options presented above: a Manifest thumbnail using the **Thumbnails with a IIIF image service** option, a video Canvas using the **Minimal thumbnail requirements** option, and an image Canvas using the **Thumbnails with a IIIF image service + JSON image response sizes** option. *Note: the image Canvas here specifies a level0 profile, but could be changed to a level1 profile if leaving it open for custom sizes is desirable.*

{% include manifest_links.html viewers="Mirador, UV" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]
* [Image Thumbnail for Manifest][0117]

{% include acronyms.md %}
{% include links.md %}
