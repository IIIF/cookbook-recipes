---
title: Geolocate Manifest to a Polygonal Area
id: 195
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Make a geographic Web Annotation to geolocate a Presentation API 3 Manifest to a polygonal geographic area."
---

### Use Case 
There is a photo that was taken during an IIIF event. A IIIF Presentation API 3 Manifest will created using the photograph. The Manifest is to be geolocated to the bounding area of Göttingen, Germany where the event took place. Unfortunately, the exact coordinates are not known.  

### Implementation Notes
* This Manifest extends the Manifest used in the [rights recipe](0008). If you have any questions about the Manifest, please see the rights recipe for more information. 
* The third party [GeoJSON-LD](https://geojson.org/geojson-ld/) context is included alongside the IIIF Presentation 3 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation 3 context does not describe those terms. The field `@context` can be an array, and when it is the Presentation API 3 context must be the last item in the array.  

### Restrictions
Nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction.  

### Manifest

{% include jsonviewer.html src="manifest.json" config='data-line="68-123"' %}

### Interface Example For This Recipe Manifest
[Manifest Coordinates in Leaflet](http://geo.rerum.io/geolocate/viewAnnotations.html?manifest=https://preview.iiif.io/cookbook/0195-geolocate-manifest-to-polygon/recipe/0195-geolocate-manifest-to-polygon/manifest.json)

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116](https://github.com/IIIF/iiif-stories/issues/116)
* [https://github.com/IIIF/iiif-stories/issues/119](https://github.com/IIIF/iiif-stories/issues/119)
* [https://github.com/IIIF/iiif-stories/issues/125](https://github.com/IIIF/iiif-stories/issues/125)
* [https://github.com/IIIF/iiif-stories/issues/135](https://github.com/IIIF/iiif-stories/issues/135)

## Related Recipes
* [Geolocate Canvas Fragment to a Point][TBD]
* [Geolocate Manifest to a Point][TBD]
* [Rights][0008]

{% include acronyms.md %}
{% include links.md %}
