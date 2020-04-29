---
title: Geographical Assertion Annotation 
id: 999
layout: recipe
tags: [maps, geocode, annotation]
summary: "Make a geographical assertion about the word Paris in some transcription text."
---

### Use Case
A correspondence between friends in Paris was discovered.  There is the desire to link all mentions of 'Paris' to Paris, France. 

### Implementation Abstract
An example of a Canvas that has a transcription where the word 'Paris' is goecoded to Paris, France.  The transcription could be a resource of its own, but in IIIF the most abundant use case is that the transcription is a supplement to some canvas with an image the transcription was derived from.  It is imagined this Canvas is part of some Manifest that aggregates many of the letters between these individuals.

### Implementation Notes
* `geocode` was used as the motivation throughout. The IIIF-Maps group is working on proper motivation extensions for the various kinds of assertions that could be made. The three main categories are `geocode`, `georeference` and `co-locate`.
* GeoJSON `properties` is a very generic field and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes. This community should establish conventions to inject, override or extend resource properties.
* [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)
* Any place a `Feature` is used could instead be a [`FeatureCollection`](geocollection.json) containing one or more `Features`.
* The annotation transcribing the fragment with the word "Paris" is deprioritized and thus is not embedded fully in the related data artifacts. 


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
