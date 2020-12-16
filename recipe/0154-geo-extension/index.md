---
title: Represent Manifest on a Map with navPlace Extension
id: 154
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Use the navPlace extension to provide geolocation information about an IIIF Presentation API 3 Manifest."
---

### Use Case 
You would like to see your IIIF Presentation API 3 Manifest represented on open source world map based user interfaces such as Leaflet or Google Maps. This could mean simply displaying a geometric shape on a map, but may include more data from the resource in connection with the geometric shape to facilitate robust functionality within the MapUI.

### Implementation Notes
This Manifest extends the Manifest used in the [simple image service recipe][0005]. See that recipe for more information about the Manifest.

The third party [GeoJSON-LD](https://geojson.org/geojson-ld/) context is included alongside the IIIF Presentation 3 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation 3 context does not describe those terms. The field `@context` can be an array, and when it is the IIIF Presentation API 3 context must be the last item in the array.  

Note that [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)

### Restrictions
Applications that strictly follow Linked Data practices will find that nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction. Be aware if you plan to serialize JSON-LD into other semantic data formats or markup languages such as RDF.

### Example
`navPlace` contains GeoJSON-LD, which is supported by a number of open source mapping systems. A client can parse out `navPlace` from a Manifest and pass the GeoJSON into MapUI systems resulting in rendered geometric shapes on a world map. Often, data from the resource such as an image URL, label or description is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON. You can see the coordinates from the extension [render in a Leaflet viewer](http://geo.rerum.io/geolocate/leaflet_view.html?manifest=notyet.json). You can also see a serialization of these coordinates into `<feature>`s [render in a MapML implementation](http://geo.rerum.io/geolocate/mapML-view.html?manifest=notyet.json).  

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="59-82"' %}

## Related Recipes
* [Geolocate Manifest to a Point][TBD]
* [Geolocate Manifest to a Polygonal Area][TBD]

{% include acronyms.md %}
{% include links.md %}