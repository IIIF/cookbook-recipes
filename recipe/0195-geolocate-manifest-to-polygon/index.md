---
title: Geolocate Manifest to a Polygonal Area
id: 195
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Make a geographic Web Annotation to geolocate a Presentation API 3 Manifest to a polygonal geographic area."
---

### Use Case 
You have a special photograph taken during an event that you have encoded inside a IIIF Presentation API 3 Manifest. You would like to geolocate the Manifest to the outiline of the city in which the event took place (Göttingen, Germany). You want the geographic coordinates to render in open source mapping systems, such as [Leaflet](https://leafletjs.com/).  You would like to geolocate the Manifest to the outline of Göttingen, Germany [using software that generates IIIF Presentation API 3.0 Annotations](http://geo.rerum.io/geolocate/annotate.html).

### Implementation Notes
* This Manifest extends the Manifest used in the [simple image service recipe][0005]. See that recipe for more information about the Manifest.
* The third party [GeoJSON-LD](https://geojson.org/geojson-ld/) context is included alongside the IIIF Presentation API 3.0 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation API 3 context does not describe those terms. The field `@context` can be an array, and when it is the Presentation API 3 context must be the last item in the array.  

### Restrictions
Nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction.  

### Manifest

{% include jsonviewer.html src="manifest.json" config='data-line="59-108"' %}

### Interface Example For This Recipe Manifest
There are robust viewers that support IIIF resource types and the Annotations that describe them.  However, these viewers have not yet taken into account rendering coordinate assertions beyond the plain text understanding of the Annotation bodies.  The [IIIF Maps Community Group](https://iiif.io/community/groups/maps/) is considering plugins to support coordinate rendering systems, such as Leaflet embedded in viewing windows.  For now, you can see the coordinates in the body of the Annotation on the Manifest [render in a Leaflet viewer](http://geo.rerum.io/geolocate/viewAnnotations.html?manifest=https://preview.iiif.io/cookbook/0182-geolocated-simple-manifest/recipe/0182-geolocated-simple-manifest/manifest.json).

## Related Recipes
* [Geolocate Canvas Fragment to a Point][TBD]
* [Geolocate Manifest to a Point][TBD]

{% include acronyms.md %}
{% include links.md %}
