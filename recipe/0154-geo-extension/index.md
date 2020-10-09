---
title: navPlace Extension
id: 997
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Make a geographical assertion about a IIIF resource via the navPlace extension."
---

### Use Case 
You have a special photograph taken during an event that you plan to encode inside a IIIF Presentation API 3 Manifest. You would like to geolocate the Manifest to the coordinates obtained from the photograph metadata. You want the coordinates to render in open source mapping systems, such as [Leaflet](https://leafletjs.com/).

### Implementation Notes
* This Manifest extends the Manifest used in the [simple image service recipe][0005]. See that recipe for more information about the Manifest.
* The third party [GeoJSON-LD](https://geojson.org/geojson-ld/) context is included alongside the IIIF Presentation 3 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation 3 context does not describe those terms. The field `@context` can be an array, and when it is the IIIF Presentation API 3 context must be the last item in the array.  

### Restrictions
Nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction.

### Manifest

{% include jsonviewer.html src="manifest.json" config='data-line="59-82"' %}

### Interface Example For This Recipe Manifest
There are robust viewers that support IIIF resource types. However, these viewers have not yet taken into account rendering coordinate assertions beyond the plain text understanding of the Annotation bodies. The [IIIF Maps Community Group](https://iiif.io/community/groups/maps/) is considering plugins to support coordinate rendering systems, such as Leaflet embedded in viewing windows.

## Related Recipes
* [Geolocate Canvas Fragment to a Point][TBD]
* [Geolocate Manifest to a Polygonal Area][TBD]

{% include acronyms.md %}
{% include links.md %}