---
title: Geographical Assertion Annotation 
id: 999
layout: recipe
tags: [maps, geocode, annotation]
summary: "Make a geographical assertion about the word Paris in some transcription text."
---

### Use Case
There is a region of interest on a canvas that could be further described by known Earth coordinates.  That region is to be geocoded.

### Implementation Abstract
An example of a Manifest that has a Canvas fragment geocoded to Paris, France.  The image used on this Canvas is a hosted IIIF Image API 3 fixture image supplied by the BnF.  The Canvas has the same dimensions as the image.  The word 'Paris' appears on the image and the region containing the word is targeted by 2 Annotations.  One Annotation supplements the fragment with the word 'Paris'.  The other Annotation geocodes the fragment to Paris, France so that the fragment is not confused with any other city named Paris in the word (ex. Paris, Illinois, U.S.A.)

### Implementation Notes
* `geocode` was used as the motivation throughout. The IIIF-Maps group is working on proper motivation extensions for the various kinds of assertions that could be made. The three main categories are `geocode`, `georeference` and `co-locate`.
* GeoJSON `properties` is a very generic field and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes. This community should establish conventions to inject, override or extend resource properties.
* [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)
* Any place a `Feature` is used could instead be a [`FeatureCollection`](geocollection.json) containing one or more `Features`.
* Without knowing the specific reason for the assertion of 'Paris' and the assertion of coordinates, it was best to leave them as two separate Annotations instead of one Annotation with two bodies.  This choice is the most agnostic allowing for the greatest functionality applied to these bodies as two distinct data nodes tracked with two distinct identifiers and the liklihood of being detected by the greatest spread of UIs.  The Annotations can be combined into one Annotation with two bodies, so long as you understand the implications for your use case.  

### The Canvas containing a jpeg that has a word of interest to geocode.
[JSON-LD](canvas.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="canvas.json" }
```json
```

# Break-Down Of The Important Parts
### The Canvas Content
[JSON-LD](contentPage.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="content.json" }
```json
```

### The Canvas supplementing data to further describe the content
[Text](supplementingPage.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="supplementingPage.json" }
```json
```

### The specific Annotation which geocodes the region of the canvas with the word 'Paris' to Paris, France.
[JSON-LD](geoAnno.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="geoAnno.json" }
```json
```

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
