---
title: Geographical Assertion Annotation 
id: 999
layout: recipe
tags: [maps, geocode, annotation]
summary: "Make a geographical assertion about the word Paris in some transcription text."
---

### Use Case
A correspondence between friends in Paris was discovered.  There is the desire to link all mentions of 'Paris' to Paris, France. 

### Implementation Notes
* `geocode` was used as the motivation throughout. The IIIF-Maps group is working on proper motivation extensions for the various kinds of assertions that could be made. The three main categories are `geocode`, `georeference` and `co-locate`.
* GeoJSON `properties` is a very generic field and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes. This community should establish conventions to inject, override or extend resource properties.
* [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)


### The Transcription Text
[Text](transcription.txt)

### The Annotation
[JSON-LD](anno.json)

### In an AnnotationPage
[JSON-LD](annoPage.json)

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116](https://github.com/IIIF/iiif-stories/issues/116)
* [https://github.com/IIIF/iiif-stories/issues/119](https://github.com/IIIF/iiif-stories/issues/119)
* [https://github.com/IIIF/iiif-stories/issues/125](https://github.com/IIIF/iiif-stories/issues/125)
* [https://github.com/IIIF/iiif-stories/issues/135](https://github.com/IIIF/iiif-stories/issues/135)

## Related Recipes
* [0TBD]()
* [0TBD]()
* [0TBD]()

{% include acronyms.md %}
{% include links.md %}
