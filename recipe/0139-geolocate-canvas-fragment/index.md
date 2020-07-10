---
title: Geolocated Canvas Fragment
id: 139
layout: recipe
tags: [maps, geolocate, annotation]
summary: "Make a geographic Web Annotation to provide geolocation information about a fragment of a Canvas."
---

### Use Case 
There is a region of interest on a Canvas that could be further described by known Earth coordinates. That region is to be supplemented with geolocation information.

### Implementation Abstract
An example of a Manifest that has a Canvas fragment geolocated via a geographic point. The word "Paris" appears on the image and the region containing the word is targeted by two Annotations. One Annotation supplements the fragment with the text "Paris". The other Annotation supplies coordinates centered on Paris, France in order to supply a geographic reference.

### Implementation Notes
* All individual items within the Manifest, as well as the Manifest, are resolvable at the URIs seen in the example. 
* The third party GeoJSON-LD context is included alongside the IIIF Presentation 3 context. This supplies the vocabulary terms for the GeoJSON-LD Annotation bodies since the IIIF Presentation 3 context does not describe those terms. The field `@context` can be an array, and when it is the Presentation API 3 context must be the last item in the array. 
* `supplementing` was used as the Annotation motivation throughout. The IIIF-Maps group is working on proper motivation extensions for the various kinds of geographic assertions that could be made. The proposed motivations are `geocode`, `georeference`, `geolocate`, `georectify`, and `co-locate`.
* The Annotation could also keep the `supplementing` motivation and the [Annotation body could note a purpose](https://www.w3.org/TR/annotation-model/#purpose-for-external-web-resources).  Usually, purpose is used to represent multiple motivations.  
* GeoJSON `properties` is a very generic field and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes.
* [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)
* Any place the type Feature is used could instead be a [FeatureCollection](geocollection.json) containing one or more Features.
* Without knowing the specific reason for the assertion of "Paris" and the assertion of coordinates, it was best to create two separate Annotations instead of one Annotation with two bodies. This choice is the most agnostic allowing for the greatest functionality applied to these bodies as two distinct data nodes tracked with two distinct identifiers. This choice also elevates the likelihood of being detected by the greatest spread of UIs. The Annotations can be combined into one Annotation with two bodies, so long as you understand the implications for your use case.  

### Restrictions
Nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction.

### The Manifest
This Manifest contains one Canvas with one Image, and the Canvas has the same size dimensions as the Image. The word “Paris” appears on the Image. The Canvas is supplemented with an Annotation Page containing two Annotations targeting this region of the Canvas using the [#xywh Fragment Selector syntax](https://www.w3.org/TR/annotation-model/#fragment-selector).  The first Annotation asserts the textual word "Paris". The second Annotation asserts the geographic coordinates for a central point in Paris, France. Since the Image used is a IIIF Fixture image following [IIIF Image API 3.0](https://iiif.io/api/image/3.0/), you can see the targeted fragment of the Image by supplying [the values used in the #xywh selector to the Image URL](https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f20/1300,3370,250,100/max/0/default.jpg). 

{% include jsonviewer.html src="manifest.json" config='data-line="84-112"' %}

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116](https://github.com/IIIF/iiif-stories/issues/116)
* [https://github.com/IIIF/iiif-stories/issues/119](https://github.com/IIIF/iiif-stories/issues/119)
* [https://github.com/IIIF/iiif-stories/issues/125](https://github.com/IIIF/iiif-stories/issues/125)
* [https://github.com/IIIF/iiif-stories/issues/135](https://github.com/IIIF/iiif-stories/issues/135)

## Related Recipes
* [Geographic Extension][]
* [Geolocate Manifest][]

{% include acronyms.md %}
{% include links.md %}
