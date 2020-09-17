---
title: Geolocate Manifest to a Point
id: 182
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Make a geographic Web Annotation to geolocate a IIIF Presentation API 3.0 Manifest to a geographic point."
---

### Use Case 
You have a special photograph taken during an event that you have encoded inside a IIIF Presentation 3.0 Manifest. You would like to geolocate the Manifest to the site of the event in such a way that the geographic coordinates will render in an open source mapping tool, such as Leaflet. The Manifest is to be geolocated to the coordinates known from the photograph.  

### Implementation Notes
* This Manifest extends the Manifest used in the [simple image service recipe][0005]. See that recipe for more information about the Manifest.
* The third party [GeoJSON-LD](https://geojson.org/geojson-ld/) context is included alongside the IIIF Presentation 3 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation 3 context does not describe those terms. The field `@context` can be an array, and when it is the IIIF Presentation API 3.0 context must be the last item in the array.  

### Restrictions
Nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction.

### Manifest

{% include jsonviewer.html src="manifest.json" config='data-line="56-78"' %}

### Interface Example For This Recipe Manifest
There are robust viewers that support IIIF entities and the Annotations that supplement them.  However, these viewers have not yet taken into account rendering coordinate assertions beyond the plain text understanding of their bodies.  The IIIF Maps Community Group is considering the possibility of plugins to support coordinate rendering systems, such as Leaflet embedded in viewing windows.  For now, you can see the coordinate Annotation on the Manifest [render directly in a leaflet viewer](http://geo.rerum.io/geolocate/viewAnnotations.html?manifest=https://preview.iiif.io/cookbook/0182-geolocated-simple-manifest/recipe/0182-geolocated-simple-manifest/manifest.json).

## Related Recipes
* [Geolocate Canvas Fragment to a Point][TBD]
* [Geolocate Manifest to a Polygonal Area][TBD]
* [Rights][0008]

{% include acronyms.md %}
{% include links.md %}
