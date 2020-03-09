---
title: Multiple Geographical Assertions
id: 140
layout: recipe
tags: [maps, geocode, annotation]
summary: "Make multiple geographical assertions about a IIIF resource."
---

### Use Case
Geographical knowledge of a IIIF resource is obtained.  There is the need to assert that geographical information about the resource.


### Implementation Notes
There are multiple scenarios that drive which pattern one may use to achieve this.  If the agent making the assertion owns the resource, they may change the state of that resource to include the assertions directly on the JSON-LD object.  Other scenarios include entirely third party assertions where the agent does not own the resource or even have permission to view it.

Note that geocode was used as the motivation throughout.  The IIIF-Maps group is working on proper motivation extensions for the various kinds of assertions that could be made.  The three main categories are geocode, georeference and co-locate.

Note that the GeoJSON properties is a very generic field. This community should seek to put some rails on what goes into that field. If, for example, the targeted resource has a label and the properties field contains a label, the consuming interface must make a choice on which to preference for UI/UX purposes. This could be a way to inject, override or extend resource properties.

Note that geometry can be more than just a Point.

Note that target values can include hash or SVG selectors. This would allow someone to annotate a portion/slice/frame/fragment of a resource.


### Restrictions
In Presentation API 3, there is a minor conflict with the "type" field.  
FeatureCollections must not have properties.
See Presentation API 3 Example 3.


# Presentation API 3
### Example 1
In this example, the agent does not own the resource and it attempting multiple third party assertion.  This can be done using Annotations.
``` json-doc
[JSON-LD](anno.json)
```

You can target the same resource with many of these Annotations that represent separate geographic assertions.


### Example 2
In this example, the agent does own the resource.  The agent still wants to use Annotations to describe the resource and wants to put those Annotations directly on the resource.  This can be done using an AnnotationPage.
``` json-doc
[JSON-LD](canvasAndAnnos.json)
```

### Example 3 
In this example, the agent does own the resource.  The agent wants to put the assertion directly on the resource without using the AnnotationPage. 
``` json-doc
[JSON-LD](canavsAndService.json)
```
This has a small issue with how type clashes, but we can handle that within properties. However, that means FeatureCollections could not be used here, since FeatureCollections must not have properties. There would be no way to reconcile the type conflict. It is paramount the service return an array of Features here instead of a FeatureCollection.

# Presentation API 2
### Example 1
In this example, the agent does not own the resource and is attempting to make multiple third party assertion.  This can be done using an AnnotationList.
``` json-doc
[JSON-LD](prezi2list.json)
```

### Example 2
In this example, the agent does own the resource.  The agent still wants to use Annotations to describe the resource and wants to put those Annotations directly on the resource.  This can be done using an AnnotationList.
``` json-doc
[JSON-LD](prezi2canvasandannos.json)
```

### Example 3
In this example, the agent does own the resource.  The agent wants to put the assertion directly on the resource.  It is a bit different since service is not an array. That means your service will need to return a single FeatureCollection containing all the geographic data Features.
``` json-doc
[JSON-LD](prezi2canvasandservice.json)
```

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116] [0116]
* [https://github.com/IIIF/iiif-stories/issues/119] [0119]
* [https://github.com/IIIF/iiif-stories/issues/125] [0125]
* [https://github.com/IIIF/iiif-stories/issues/135] [0135]

## Related Recipes
* [Geographical Assertinos] [0TBD] - It is the same problem, only with a single assertion instead of multiple.
* [Annotation Specific Resources] [0023] - The same Annotation techniques seen here will work on specific resources.
* [Transcription/Translation] [0092] - The same Annotation aggregates AnnotationList and AnnotationPage combined with motivation will achieve this

{% include acronyms.md %}
{% include links.md %}