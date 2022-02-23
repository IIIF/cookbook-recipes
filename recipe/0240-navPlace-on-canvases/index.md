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
Potential Idea : You plan to view pieces of art for the subject "Laocöon". You would like to show the location of those works on a web mapping platform. This is possible using the `navPlace` property.

### Implementation Notes
For all the information on how to use the `navPlace` property see the [implementation notes in the IIIF Extensions directory.](https://iiif.io/api/extension/navplace/#5-implementation-notes) 
For a complete guide on how to use the `navPlace` property see the [IIIF Guides entry for `navPlace`.](https://preview.iiif.io/guides/41-navPlace/guides/iiif.io.api.extension.navplace/) 

### Example
The Manifest contains images of the bronze by Giovanni Battista Foggini and the painting by _______, and the map shows the locations of these works. 
The Manifest below contains two Canvases, and each Canvas has a photograph painted onto it. The `navPlace` property in the Canvases stores geographic information from the photographs. `navPlace` contains GeoJSON-LD, and a client can parse GeoJSON features from `navPlace`. These GeoJSON features are rendered as geometric shapes by a web-based map platform. Often, data from the resource such as an image URL, label or summary is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON.  Web mapping platforms typically offer built in display functionality for metadata contained in `properties`.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line=""' %}

## Related Recipes
* [Represent Canvas Fragment as a Geographic Area in a Web Mapping Client][0139]
* [Provide Geographic Coordinates for a Manifest with navPlace][0154]

{% include acronyms.md %}
{% include links.md %}
