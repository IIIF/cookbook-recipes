---
title: Locate a Manifest on a Web Map
id: 154
layout: recipe
tags: [maps, geolocate, navPlace]
summary: "Use the navPlace extension to provide geolocation information about an IIIF Presentation API 3.0 Manifest."
# Note that navPlace support is not baked into the viewers yet.
viewers:
 - id: UV
   support: none
 - id: Mirador
   support: none
---

### Use Case
You have a photograph of the Laocoön bronze and you would like to show the current location of the bronze as a Point on a web mapping platform. `navPlace` allows you to place the spatial representation (Point, Polygon, Line Segment) of your Manifest on a web map. 


### Implementation Notes
For all the information on how to use the `navPlace` property see the [implementation notes in the IIIF Extensions directory.](https://iiif.io/api/extension/navplace/#5-implementation-notes) 
For a complete guide on how to use the `navPlace` property see the [IIIF Guides entry for `navPlace`.](https://preview.iiif.io/guides/41-navPlace/guides/iiif.io.api.extension.navplace/) 


### Example
The map shows the location of the object represented in the image, the Laocoön bronze by Giovanni Battista Foggini, on display at the Getty Center. 
The Manifest contains one Canvas with a photograph painted onto it. The `navPlace` property in the Manifest stores geographic information about the photograph. `navPlace` contains GeoJSON-LD, and a client can parse GeoJSON features from `navPlace`. These GeoJSON features are rendered as geometric shapes by a web mapping platform. Data from the resource such as an image URL, label or summary is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON, but this is not a required step for seeing the shape on the map.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line=""' %}

## Related Recipes
* [Represent Canvas Fragment as a Geographic Area in a Web Mapping Client][0139]
* [Provide Geographic Coordinates for Canvases in a Manifest with navPlace][0240]

{% include acronyms.md %}
{% include links.md %}
