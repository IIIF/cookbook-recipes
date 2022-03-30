---
title: Represent a Manifest as a Geographic Area in a Web Mapping Client Using navPlace
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
You have a photograph of the Laocoön bronze and you would like to show the current location of the bronze as a Point on a web mapping platform. Use of `navPlace` allows for computational addressing of geographic coordinates and arrangement of representations of those resources in WGS84 coordinate space. The web mapping platforms that accomplish this offer varying degrees of interactive behavior, a portion of which are consistent between the platforms. Often, you can interchange between different projections of the surface of the Earth to find a projection that best suits your geographic data.


### Implementation Notes
For all the information on how to use the `navPlace` property see the [implementation notes in the IIIF Extensions directory.](https://iiif.io/api/extension/navplace/#5-implementation-notes) 
For a complete guide on how to use the `navPlace` property see the [IIIF Guides entry for `navPlace`.](https://preview.iiif.io/guides/41-navPlace/guides/iiif.io.api.extension.navplace/) 


### Example
TBD - The map shows the location of the objected represented in the image, the Laocoön bronze by Giovanni Battista Foggini, on display at the Getty Center. 
The Manifest below is of an image of the Laocoön bronze by Giovanni Battista Foggini, and the map shows the location of the Getty Center where it is  displayed. 
The Manifest contains one Canvas with a photograph painted onto it. The `navPlace` property in the Manifest stores geographic information from the photograph. `navPlace` contains GeoJSON-LD, and a client can parse GeoJSON features from `navPlace`. These GeoJSON features are rendered as geometric shapes by a web-based map platform. Often, data from the resource such as an image URL, label or summary is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON.  Web mapping platforms typically offer built in display functionality for metadata contained in `properties`.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line=""' %}

## Related Recipes
* [Represent Canvas Fragment as a Geographic Area in a Web Mapping Client][0139]
* [Provide Geographic Coordinates for Canvases in a Manifest with navPlace][0240]

{% include acronyms.md %}
{% include links.md %}
