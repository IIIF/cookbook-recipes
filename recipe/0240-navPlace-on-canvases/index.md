---
title: Represent Canvases in Manifest on a Web Map with navPlace
id: 240
layout: recipe
tags: [maps, geolocate, navPlace]
summary: "Use the navPlace extension to provide geolocation information for the Canvas items of an IIIF Presentation API 3.0 Manifest."
# Note that navPlace support is not baked into the viewers yet.
viewers:
 - id: UV
   support: none
 - id: Mirador
   support: none
---

### Use Case
Under Development
Potential Idea : Multiple representations of a physical artifact (statue) such as photos from different angles, sketches/drawings, etc.  Each of those representations will be a Canvas.  Each canvas will have a different geographic region associated with it.  Though we cannot assert physical location through navPlace, the "label" or "summary" of that Canvas can note "Current location of statue" or "location where sketch was drawn".


### Implementation Notes
IIIF has a registered API extension called `navPlace` which is used to associate geographic coordinates with IIIF resource types, and it is leveraged here to meet the use case. 

Note that [`geometry` has more types besides `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)

### Restrictions
Applications that strictly follow Linked Data practices will find that nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction. Be aware if you plan to serialize JSON-LD into [other semantic data formats or markup languages](https://www.w3.org/TR/json-ld11/#relationship-to-other-linked-data-formats) such as RDF.

### Example
The Manifest below contains two Canvases. Each Canvas has one Image with a photograph painted onto it. Those Canvases also contain the `navPlace` property which stores geographic information about the photograph. `navPlace` contains GeoJSON-LD, which is supported by a number of open source mapping systems. A client can parse `navPlace` from a Canvas and pass the GeoJSON into a web map resulting in rendered geometric shapes on a world map. Often, data from the resource such as an image URL, label or description is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line=""' %}

## Related Recipes
* [Represent Canvas Fragment as a Geographic Area in a Web Mapping Client][0139]
* [Provide Geographic Coordinates for a Manifest with navPlace][0154]

{% include acronyms.md %}
{% include links.md %}
