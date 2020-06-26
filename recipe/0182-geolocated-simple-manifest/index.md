---
title: Geolocated Simple Manifest
id: 182
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Geolocate a simple Manifest"
---

### Use Case 
There is a photo taken from an event being encoded as a IIIF Presentation API 3.0 Manifest. The camera captured coordinate metadata for the photo. Those coordinates are used to geolocate the Manifest.

### Implementation Notes
* All individual items within the Manifest, as well as the Manifest, are resolvable at the URIs seen in the example.  
* The Manifest used was taken from the [rights](https://github.com/IIIF/cookbook-recipes/issues/8) recipe. 

### Restrictions
Nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction.  

{% include jsonviewer.html src="manifest.json" config='data-line=""' %}

## Related IIIF Stories
* 

## Related Recipes
* [Geolocating Assertion](https://github.com/IIIF/cookbook-recipes/issues/139)

{% include acronyms.md %}
{% include links.md %}
