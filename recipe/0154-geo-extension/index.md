---
title: navPlace Extension
id: 997
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Make a geographical assertion about a IIIF resource via the navPlace extension."
---

### Use Case
Geographical knowledge of a IIIF resource is obtained. There is the need to assert that geographical information about the resource.

### Implementation Notes
* Note that these extension values are not Annotations.  This means there is no motivation or purpose.  Proper extensions will include @context vocabulary to describe the motivation and purpose for the extension.  You can see an example of this in the @context of the JSON Manifest below. The main motivations/purposes for the geographic extension are `geocode`, `georeference`, `geolocate`, `georectify`, and `co-locate`. 
* GeoJSON `properties` is a very generic field and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes. This community should establish conventions to inject, override or extend resource properties.
* [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)
* `navPlace_ex1` and `navPlace_ex2` are both proper examples of how the extension could be implemented.  The value for the extension key could either be an Object or an Array.  The types used in the Object or Array could be `Feature`s and/or `FeatureCollection`s.  A described object will not contains multiple `navPlace` values.

### Restrictions
This extension has not yet been implemented yet.  @context and vocabulary do not exist for it. Therefore it is not valid at this time and merely exists for demonstration purposes.

### Manifest With navPlace Extension
In this example, the navPlace extension was used to place the geographic assertion directly on the resource.

{% include jsonviewer.html src="manifestWithnavPlace.json" config='data-line="39-82"' %}

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116](https://github.com/IIIF/iiif-stories/issues/116)
* [https://github.com/IIIF/iiif-stories/issues/119](https://github.com/IIIF/iiif-stories/issues/119)
* [https://github.com/IIIF/iiif-stories/issues/125](https://github.com/IIIF/iiif-stories/issues/125)
* [https://github.com/IIIF/iiif-stories/issues/135](https://github.com/IIIF/iiif-stories/issues/135)

## Related Recipes
* [0TBD]() -
* [0TBD]() -
* [0TBD]() -

{% include acronyms.md %}
{% include links.md %}
