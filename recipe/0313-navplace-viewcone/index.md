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
The theme of this is to help explain why a "Viewcone" and not a "Triangle"
"My favorite band is playing at Red Rock's Amphitheater and I want to know if I will be able to see the members of the band from my seats"
"I am moving through a 2D street view (like google maps) and want to know what I can see from a given point on the road."
"Indoor Example: I want to hang a photograph of my family in the house and would like to know the spot in my house where people would get the best view of the photograph"
"The greatest visibility of a masterpiece in an art gallery"


### Implementation Notes
Main job here is to explain the data required to express a viewcone.  Is starting point and heading required?  What about targets or obstacles that obstruct the view (can I see or not see something)? Do I need the entire snowcone shape in the coordinates I capture, or can clients generate a viewcone with less data (three points, a heading, a height)?  How would I instruct an implementer to do the "most reliable" or "best" expression of a viewcone through data?  How would an implementer generate a reliable dataset (how to capture and collect the points of the polygonal shape)?

"This is a not-so-smart shape that looks like a viewcone"
vs
"This is a so-smart shape that takes into account angle and distance and obstacles"


### Example
Should be very visual, show with obstacles between the origin point and object the example is trying to prove you can/can't see.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="1"' %}

## Related Recipes
* TODO

{% include acronyms.md %}
{% include links.md %}
