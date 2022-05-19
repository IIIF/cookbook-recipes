---
title: Locate Multiple Canvases on a Web Map
id: 240
layout: recipe
topic: geo-recipes
tags: [maps, geolocate, navPlace]
summary: "Use the navPlace extension to provide geolocation information for the Canvas items of an IIIF Presentation API 3.0 Manifest."
viewers:
 - id: UV
   support: none
 - id: Mirador
   support: none
---

### Use Case
You have two photographs of the subject "Laocoön" and you would like to show the current location of the works in those photographs as a Point on a web mapping platform. `navPlace` allows you to place the spatial representation (Point, Polygon, Line Segment) of your Canvas on a web map.

### Implementation Notes
This recipe describes the use of `navPlace` at a Canvas implementation level. For other applications, see related recipes below. It is important to note that `navPlace` is not semantic and cannot be used to state the purpose of the location it shows. The example uses `navPlace` to represent the current location of the item, but it is not specified or limited to that, and more accurately we can say that `navPlace` is used to show a location.

The value for `navPlace` is formatted as GeoJSON. Note that [Google Maps will display coordinates in Latitude, Longitude order](https://developers.google.com/maps/documentation/javascript/reference/coordinates
), but [GeoJSON specifies they need to be recorded in Longitude, Latitude order](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.1
). Always confirm the order of your coordinates when gathering them, as other web mapping platforms may have these format inconsistencies.

For all the information on how to use the `navPlace` property see the [implementation notes in the IIIF Extensions directory.](https://iiif.io/api/extension/navplace/#5-implementation-notes)

For a complete guide on how to use the `navPlace` property, and an example of how it is displayed in a viewer, see the [IIIF Guides entry for `navPlace`.](https://guides.iiif.io/guides/navplace/)

### Example
The Manifest contains images of the bronze by Giovanni Battista Foggini and the painting by _______. The `navPlace` property in each Canvas stores geographic information about the works represented in the photographis, in this case their current location. `navPlace` contains GeoJSON-LD, and a client can parse GeoJSON features from `navPlace`. These GeoJSON features are rendered as geometric shapes by web mapping platforms. Data from the resource such as an image URL, label or summary is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON, but this is not a required step for seeing the shape on the map.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="2, 38-55, 85-101"' %}

## Related Recipes
* [Represent Canvas Fragment as a Geographic Area in a Web Mapping Client][0139]
* [Locate a Manifest on a Web Map][0154]

{% include acronyms.md %}
{% include links.md %}
