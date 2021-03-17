---
title: Image Thumbnails on Canvases
id: 232
layout: recipe
tags: [image, presentation]
summary: "Display a thumbnail image for a Canvas resource, such that it can be used by clients to represent the object."
---

## Use Case

As a publisher of a Manifest, you may choose to declare thumbnail images on Canvases in order to optimize thumbnail generation and display by viewing clients, such as Mirador and Universal Viewer. While it is not necessary to declare a thumbnail on Canvases since clients SHOULD render thumbnails from the Resource, doing so can increase the efficiency with which thumbnails load in a viewer. This is especially noticeable in Manifests that have many Canvases, such as books and manuscripts with many high-resolution images.

This recipe outlines several different approaches to declaring thumbnails and discusses the benefits, drawbacks, and requirements for each. For a more general introduction to thumbnails, see the [Image Thumbnail for Manifest][0117] recipe.

## Implementation Notes

At a minimum, the `thumbnail` property requires the `id` and `type` properties. It is highly recommended to include `format`, `height` and `width` properties.

```json
"thumbnail": [
  {
    "id": "https://example.org/img/thumb.jpg",
    "type": "Image",
    "format": "image/jpeg",
    "width": 200,
    "height": 300
  }
]
```


When the images are IIIF images, it is recommended that a [IIIF Image API](https://iiif.io/api/image/3.0/) service be included to enable resizing. It is also possible to include additional [JSON image response](https://iiif.io/api/image/3.0/#51-image-information-request) properties, such as `sizes` or `tiles`, to potentially optimize thumbnail generation and delivery.

### Thumbnail with "deep" IIIF image service (recommended option when the thumbnail image is a IIIF image)

```json
"thumbnail":{
  "@id":"https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_001/full/max/0/default.jpg",
  "type": "Image",
  "format": "image/jpg",
  "width":100,
  "height":100,
  "service":{
    "@id":"https://iiif.io/api/image/3.0/example/reference/4f92cceb12dd53b52433425ce44308c7-ucla_bib1987273_no001_rs_001",
    "type": "ImageService3",
    "profile": "level1",
    "width":3497,
    "height":4823,
    "sizes":[
      {
         "width":,
         "height":
      },
      {
         "width":,
         "height":
      }
    ]
  }
},
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
