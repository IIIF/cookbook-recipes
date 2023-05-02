---
id: 313
title: Viewcone
topic: geo-recipes
tags: [maps, geolocate, navPlace]
summary: "Use the navPlace extension to express a visual viewcone from a given point on a map."
layout: recipe
viewers:

---

### Use Case
I would like to represent on a web map the orientation of a photograph, the point of origin and the visible radius. 

The application can go from showing the photographer's point of view in old photographs georeferenced on a historical map, to placing archeological findings with the correct reference point in focus, to finding the optimal placement for a work of art on an art gallery, using either the visitor's starting point as the origin, or the work of art itself. 

### Implementation Notes
The necessary data to generate the viewcone can / must be collected using external tools such as Google Earth, to pinpoint the origin point (the photographer's point of view) latitude, longitude and heading. Drawing the viewcone arch can be done manually feeding the coordinates for each point that form the radius, taken from Google Earth, or approximately by determining a default angle (narrow, wide, extra wide) and distance (short, far, infinite). The precise coordinates extracted from Google Earth will provide highest accuracy, and will be necessary to create reliable machine readable data. However, end users who can allow a larger margin of error might find it easier to use the default "sizes" for opening and distance instead, in case of missing the precise radius coordinates. 

Obstacles that might obscure part of the field of view in the viewcone are currently not supported. 


### Example
Should be very visual, show with obstacles between the origin point and object the example is trying to prove you can/can't see.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="1"' %}

## Related Recipes
* TODO

{% include acronyms.md %}
{% include links.md %}
