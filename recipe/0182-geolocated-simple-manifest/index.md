---
title: Geolocated Manifest
id: 182
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Geolocate a Manifest"
---

### Use Case 
There is a photo taken from an event being encoded as a IIIF Presentation API 3.0 Manifest. I would like to geolocate the Manifest to the event's main building using coordinates.  

### Implementation Notes
* All individual items within the Manifest, as well as the Manifest, are resolvable at the URIs seen in the example.
* The Manifest used was taken from the [rights](https://github.com/IIIF/cookbook-recipes/issues/8) recipe. If you have any questions about the Manifest, visit that recipe to learn more.
* The third party GeoJSON-LD context is included alongside the IIIF Presentation 3 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation 3 context does not describe those terms. The field `@context` can be an array, and when it is the Presentation API 3 context must be the last item in the array.  

### Restrictions
Nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction.  

### Manifest

{% include jsonviewer.html src="manifest.json" config='data-line="68-95"'  %}

### Interface Example For This Recipe Manifest
[Manifest Corrdinates in Leaflet](http://geo.rerum.io/geolocate/viewAnnotations.html?manifest=https://raw.githubusercontent.com/IIIF/cookbook-recipes/0182-geolocated-simple-manifest/recipe/0182-geolocated-simple-manifest/manifest.json)

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116](https://github.com/IIIF/iiif-stories/issues/116)
* [https://github.com/IIIF/iiif-stories/issues/119](https://github.com/IIIF/iiif-stories/issues/119)
* [https://github.com/IIIF/iiif-stories/issues/125](https://github.com/IIIF/iiif-stories/issues/125)
* [https://github.com/IIIF/iiif-stories/issues/135](https://github.com/IIIF/iiif-stories/issues/135)

## Related Recipes
* [Geolocate Canvas Fragment](https://github.com/IIIF/cookbook-recipes/issues/139)

{% include acronyms.md %}
{% include links.md %}
