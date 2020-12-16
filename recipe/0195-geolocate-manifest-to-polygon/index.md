---
title: Represent Manifest as a Geometric Polygon on a Map
id: 195
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Make a Web Annotation to provide geographic information about an IIIF Presentation API 3 Manifest."
---

### Use Case 
You would like to see your IIIF Presentation API 3 Manifest represented as a polygon on open source world map based user interfaces such as [Leaflet](https://leafletjs.com/examples/geojson/) or [Google Maps](https://developers.google.com/maps/documentation/javascript/importing_data). This could mean simply displaying a geometric shape on a map, but may include more data from the resource in connection with the geometric shape to facilitate robust functionality within the MapUI.

### Implementation Notes
This Manifest extends the Manifest used in the [simple image service recipe][0005]. See that recipe for more information about the Manifest.

The third party [GeoJSON-LD](https://geojson.org/geojson-ld/) context is included alongside the IIIF Presentation 3 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation 3 context does not describe those terms. The field `@context` can be an array, and when it is the IIIF Presentation API 3.0 context must be the last item in the array. 

Note that [`geometry` has more specific options than `Polygon`.](https://tools.ietf.org/html/rfc7946#section-3.1)

### Restrictions
Applications that strictly follow Linked Data practices will find that nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction. Be aware if you plan to serialize JSON-LD into [other semantic data formats or markup languages](https://www.w3.org/TR/json-ld11/#relationship-to-other-linked-data-formats) such as RDF.  

### Example
The Manifest contains one Annotation Page with one Annotation. The Annotation body is GeoJSON-LD, which is supported by a number of open source mapping systems. A client can parse out the Annotation from the Manifest and pass the Annotation body into MapUI systems resulting in rendered geometric shapes on a world map. Often, data from the resource such as an image URL, label or description is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON. You can see the coordinates in the body of the Annotation on the Manifest [render in a Leaflet viewer](http://geo.rerum.io/geolocate/leaflet_view.html?manifest=https://preview.iiif.io/cookbook/0195-geolocate-manifest-to-polygon/recipe/0195-geolocate-manifest-to-polygon/manifest.json). You can also see a serialization of these coordinates into `<feature>`s [render in a MapML implementation](http://geo.rerum.io/geolocate/mapML-view.html?manifest=https://preview.iiif.io/cookbook/0195-geolocate-manifest-to-polygon/recipe/0195-geolocate-manifest-to-polygon/manifest.json).  

{% include manifest_links.html viewers="" manifest="manifest.json" %}

## Related Recipes
* [Geolocate Manifest to Multiple Polygons][TBD]
* [Geolocate Manifest to a Point][TBD]
* [Tagging Annotation][0021]

{% include acronyms.md %}
{% include links.md %}
