---
title: Locate Multiple Canvases on a Web Map
id: 240
layout: recipe
topic: geo-recipes
tags: [maps, geolocate, navPlace]
summary: "Use the navPlace extension to provide geolocation information for the Canvas items of an IIIF Presentation API 3.0 Manifest."
viewers:
---

### Use Case
You have two photographs of the subject Laocoön, one of a bronze statue and the other of a painting. You would like to show where the two works are located as Points on a web mapping platform. `navPlace` allows you to place the spatial representation (Point, Polygon, Line Segment) of your Canvas on a web map.

### Implementation Notes
This recipe describes the use of `navPlace` at a Canvas implementation level, and is largely similar to the recipe to * [Locate a Manifest on a Web Map][0154]. The main difference to note is that each Canvas will need its own Feature Collection, as described below. Other related recipes are listed in the links at the bottom of the page. 

It is important to note that `navPlace` is not semantic and cannot be used to state the purpose of the location it shows. The example uses `navPlace` to represent the current location of the items, but it is not specified or limited to that, and more accurately we can say that `navPlace` is used to show a location.

The value for `navPlace` is a single [GeoJSON Feature Collection](https://iiif.io/api/extension/navplace/#222-feature-collection). A Feature Collection represents an aggregation of spatially bounded areas. A Feature Collection has a `type` property that must be “FeatureCollection”. A Feature Collection has a `features` list that contains [GeoJSON Features](https://iiif.io/api/extension/navplace/#223-feature). Each Feature type has coordinates that correspond to a shape such as a Point or Polygon. An `id` is not required in an embedded Feature Collection, but is required when the value is a [referenced](https://iiif.io/api/extension/navplace/#13-terminology) Feature Collection. In this case, each Canvas is showing individual locations and so each Canvas needs its own Feature Collection.

Note that [GeoJSON specifies coordinates be recorded in Longitude, Latitude order](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.1
), but [Google Maps will display coordinates in Latitude, Longitude order](https://developers.google.com/maps/documentation/javascript/reference/coordinates
). Always confirm the order of your coordinates when gathering them, as other web mapping platforms may have these format inconsistencies.

For technical specifics on implementing the `navPlace` property see the [implementation notes in the IIIF Extensions directory](https://iiif.io/api/extension/navplace/#5-implementation-notes). You can also refer to the [IIIF Guides entry](https://guides.iiif.io/guides/navplace/) for step-by-step hands-on details on implementation.

The `navPlace` property is not processed by the Universal Viewer or Mirador viewer at this time.

### Example
The Manifest contains images of the bronze by Giovanni Battista Foggini and the painting _Laocoön_ by El Greco. The `navPlace` property in each Canvas stores geographic information about the works represented in the photographs, in this case their current location. `navPlace` contains GeoJSON-LD, and a client can parse GeoJSON features from `navPlace`. These GeoJSON features are rendered as geometric shapes by web mapping platforms. Data from the resource such as an image URL, label or summary is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON, but this is not a required step for seeing the shape on the map.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="3, 24-50, 90-113"' %}

## Related Recipes
* [Represent Canvas Fragment as a Geographic Area in a Web Mapping Client][0139]
* [Locate a Manifest on a Web Map][0154]
* [Navigation by Chronology][0230]

{% include acronyms.md %}
{% include links.md %}
