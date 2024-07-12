---
title: Locating an Item in Place and Time
id: 318
layout: recipe
topic: geo-recipes
tags: [maps, geolocate, navPlace, navDate]
summary: "Use navDate together with the navPlace extension to provide geographic and temporal data"
viewers:
---

### Use Case

You have one or more IIIF resources that have a date and a location associated with each, and you would like to provide these to a client for use in the user interface. For instance, you may wish the client to provide a visualization in a timeline with an associated map, or to provide the capability to filter the set based on a date range or a bounding box on a map. The data required to meet this use case can be provided by the use of both the `navDate` and `navPlace` properties on the IIIF resources. 

### Implementation Notes

The `navDate` property, as implied by its name, allows a Manifest to identify a pertinent date associated with an IIIF resource in order to help viewers provide users with date-aware navigation. Clients are not required to make use of `navDate`, and clients that do have date-aware navigation available may not default to that navigation interface. This property is described in [Navigation by Chronology][0230]

The `navPlace` property is analogous to `navDate`, but provides geographic information. The value for `navPlace` is a single [GeoJSON Feature Collection](https://iiif.io/api/extension/navplace/#222-feature-collection). A Feature Collection represents an aggregation of spatially bounded areas. This property is described in [Locate a Manifest on a Web Map][0154]. 

The `navPlace` property is not processed by the Universal Viewer or Mirador viewer at this time.

### Example

The example consists of a [Collection](collection.json) that references five Manifests. All five Manifests contain the `navDate` and `navPlace` properties, as shown below. 

The example can be displayed in a [custom viewer](https://mikeapp.github.io/maptime-demo/?iiif-content=https://preview.iiif.io/cookbook/0318/recipe/0318-navPlace-navDate/collection.json). In the viewer, click on the "Limit by Date Range" button to sort the objects by date. Adjust the ends of the timeline slider to filter the objects based on a date range.

[NavPlace and NavDate Collection](collection.json)
* [Castel Sant'Angelo, Rome](manifest-1.json)
* [The Colosseum](manifest-2.json)
* [The Arch of Titus from the Forum, Rome, ca. 1725](manifest-3.json)
* [The Temple of Vesta, Rome, 1849](manifest-4.json)
* [A View of Trajan's Forum, Rome, 1821](manifest-5.json)

{% include manifest_links.html viewers="" manifest="manifest-1.json" %}

{% include jsonviewer.html src="manifest-1.json" config='data-line="13-37"' %}

## Related Recipes
* [Locate a Manifest on a Web Map][0154]
* [Navigation by Chronology][0230]

{% include acronyms.md %}
{% include links.md %}