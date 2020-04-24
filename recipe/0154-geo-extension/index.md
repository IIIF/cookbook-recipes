---
title: Geographical Assertion Service
id: 997
layout: recipe
tags: [maps, geocode, annotation]
summary: "Make a geographical assertion about a IIIF resource via service block."
---

### Use Case
Geographical knowledge of a IIIF resource is obtained. There is the need to assert that geographical information about the resource.

### Implementation Notes
* `geocode` was used as the motivation throughout. The IIIF-Maps group is working on proper motivation extensions for the various kinds of assertions that could be made. The three main categories are `geocode`, `georeference` and `co-locate`.
* GeoJSON `properties` is a very generic field and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes. This community should establish conventions to inject, override or extend resource properties.
* [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)

### Restrictions
In [Presentation API 3](https://iiif.io/api/presentation/3.0/), there is a minor collision with the `type` field.

### Manifest With GeoJSON Service
In this example, the agent does own the resource. The agent wants to put the assertion directly on the resource without using the AnnotationPage. 
[JSON-LD](manifestAndService.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifestAndService.json" }
```json
```
**NOTE:** The `type` is represented as an array to include the required GeoJSON type "Feature" and required IIIF [service type descriptor](https://iiif.io/api/presentation/3.0/#service).  The recipe includes a scoped context at the top level to describe this so it can be both a GeoJSON Feature and a described Service. 

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116](https://github.com/IIIF/iiif-stories/issues/116)
* [https://github.com/IIIF/iiif-stories/issues/119](https://github.com/IIIF/iiif-stories/issues/119)
* [https://github.com/IIIF/iiif-stories/issues/125](https://github.com/IIIF/iiif-stories/issues/125)
* [https://github.com/IIIF/iiif-stories/issues/135](https://github.com/IIIF/iiif-stories/issues/135)

## Related Recipes
* [Geographical Assertions via Service] [0TBD]() -
* [Geographical Assertions via Annotation] [0TBD]() -
* [Geographical Assertion via Annotation] [0TBD]() -

{% include acronyms.md %}
{% include links.md %}
