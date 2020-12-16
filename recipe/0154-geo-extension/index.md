---
title: Represent Manifest on a Map with navPlace Extension
id: 154
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Make a geographical assertion about a IIIF resource via the navPlace extension."
---

### Use Case 
You would like to see your IIIF Presentation API 3 Manifest represented on open source world map based user interfaces such as Leaflet or Google Maps. This could mean simply displaying a geometric shape on a map, but may include more data from the resource in connection with the geometric shape to facilitate robust functionality within the MapUI.

### Implementation Notes
* This Manifest extends the Manifest used in the [simple image service recipe][0005]. See that recipe for more information about the Manifest.
* The third party [GeoJSON-LD](https://geojson.org/geojson-ld/) context is included alongside the IIIF Presentation 3 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation 3 context does not describe those terms. The field `@context` can be an array, and when it is the IIIF Presentation API 3 context must be the last item in the array.  

### Restrictions
Applications that strictly follow Linked Data practices will find that nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction. Be aware if you plan to serialize JSON-LD into other semantic data formats or markup languages such as RDF.

### Example
There are robust viewers that support IIIF resource types. However, these viewers have not yet taken into account rendering coordinate assertions beyond the plain text understanding of the Annotation bodies. The [IIIF Maps Community Group](https://iiif.io/community/groups/maps/) is considering plugins to support coordinate rendering systems, such as Leaflet embedded in viewing windows.

{% include jsonviewer.html src="manifest.json" config='data-line="59-82"' %}

## Related Recipes
* [Geolocate Canvas Fragment to a Point][TBD]
* [Geolocate Manifest to a Polygonal Area][TBD]

{% include acronyms.md %}
{% include links.md %}