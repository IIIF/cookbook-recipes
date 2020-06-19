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
* Note that these extension values are not Annotations.  This means there is no motivation or purpose.  Proper extensions will include @context vocabulary to describe the motivation and purpose for the extension. The main motivations/purposes for this geographic extension are `geocode`, `georeference`, `geolocate`, `georectify`, and `co-locate`. 
* GeoJSON `properties` is a very generic field and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes. This community should establish conventions to inject, override or extend resource properties.
* [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)

### Restrictions
This extension has not yet been implemented yet.  @context and vocabulary do not exist for it. Therefore it is not valid at this time and merely exists for demonstration purposes.

### Manifest With navPlace Extension
In this example, the navPlace extension was used to place the geographic assertion directly on the resource.
[JSON-LD](manifestWithNavPlace.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifestWithnavPlace.json" }
```json
```


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
