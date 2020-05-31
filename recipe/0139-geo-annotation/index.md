---
title: Geographical Assertion Annotation 
id: 999
layout: recipe
tags: [maps, geocode, annotation]
summary: "Make a geographical assertion about the word Paris in some transcription text."
---

### Use Case
There is a region of interest on a Canvas that could be further described by known Earth coordinates.  That region is to be geocoded.

### Implementation Abstract
An example of a Manifest that has a Canvas fragment geocoded to Paris, France.  The Image used on this Canvas is a hosted IIIF Image API 3 fixture image.  The Canvas has the same dimensions as the image.  The word "Paris" appears on the Image and the region containing the word is targeted by 2 Annotations.  One Annotation supplements the fragment with the text 'Paris'.  The other Annotation supplies the coordinates centered on Paris, France to circumvent confusion with any other city named Paris (ex. Paris, Illinois, U.S.A.).

### Implementation Notes
* All individual items within the Manifest, as well as the Manifest, are resolvable at the URIs seen in the example.  
* `geocode` was used as the Annotation motivation throughout as a means of letting the processor know the Annotation has a body containing coordinates. The IIIF-Maps group is working on proper motivation extensions for the various kinds of geographic assertions that could be made. The three main categories are `geocode`, `georeference` and `co-locate`.  
* The Annotation could also have the `supplementing` motivation where the [Annotation body notes a purpose](https://www.w3.org/TR/annotation-model/#purpose-for-external-web-resources) of `geocode`.  
* GeoJSON `properties` is a very generic field and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes. This community should establish conventions to inject, override or extend resource properties.
* [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)
* Any place a `Feature` is used could instead be a [`FeatureCollection`](geocollection.json) containing one or more `Features`.
* Without knowing the specific reason for the assertion of 'Paris' and the assertion of coordinates, it was best to create two separate Annotations instead of one Annotation with two bodies.  This choice is the most agnostic allowing for the greatest functionality applied to these bodies as two distinct data nodes tracked with two distinct identifiers.  This choice also elevates the liklihood of being detected by the greatest spread of UIs.  The Annotations can be combined into one Annotation with two bodies, so long as you understand the implications for your use case.  

### Restrictions
Nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction.  

### The Manifest
In this example, a Manifest contains one Canvas with one Image.  The word “Paris” appears on the Image. The Canvas is supplemented with an AnnotationList containing two Annotations targeting this region of the Canvas using the [#xywh Fragment Selector syntax](https://www.w3.org/TR/annotation-model/#fragment-selector).  One Annotation asserts the textual word "Paris".  The second Annotation asserts the geographic coordinates for Paris, France.  Since the Image used is a IIIF Fixture image following [IIIF Image API 3.0](https://iiif.io/api/image/3.0/), you can see the targeted fragment of the image by supplying [the values used in the #xywh selector in the Image URL](https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f20/1300,3370,250,100/max/0/default.jpg). 

{% include jsonviewer.html src="manifest.json" config='data-line="85-113"' %}

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
