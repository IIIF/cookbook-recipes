---
title: Multiple Geographical Assertions
layout: default
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
{
   "id":"https://iif.example.org/annotation/12345",
   "type":"Annotation",
   "@context":"http://iiif.io/api/presentation/3/context.json",
   "motivation":"geocode",
   "body":{
      "id":"https://example.org/geojson/id/123",
      "@context":"http://geojson.org/geojson-ld/geojson-context.jsonld",
      "type":"Feature",
      "properties":{
         "label":"String this geometry node should use as a label.",
         "description":"Some description to go along with node."
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            7,
            7
         ]
      }
   },
   "target":"https://iiif.example.org/canvas/123"
}
```
You can target the same resource with many of these Annotations that represent separate geographic assertions.


### Example 2
In this example, the agent does own the resource.  The agent still wants to use Annotations to describe the resource and wants to put those Annotations directly on the resource.  This can be done using an AnnotationPage.
``` json-doc
{
   "id":"https://iiif.example.org/canvas/123",
   "type":"Canvas",
   "@context":"http://iiif.io/api/presentation/3/context.json",
   "label":{
      "none":[
         "pg. 2"
      ]
   },
   "height":1000,
   "width":750,
   "items":[],
   "annotations":[
      {
         "@context":"http://iiif.io/api/presentation/3/context.json",
         "id":"https://example.org/iiif/annopage/123",
         "type":"AnnotationPage",
         "items":[
            {
               "id":"https://example.com/annotation/12345",
               "type":"Annotation",
               "@context":"http://iiif.io/api/presentation/3/context.json",
               "motivation":"geocode",
               "body":{
                  "id":"https://example.org/geojson/id/123",
                  "@context":"http://geojson.org/geojson-ld/geojson-context.jsonld",
                  "type":"Feature",
                  "properties":{
                     "label":"String this geometry node should use as a label.",
                     "description":"Some description to go along with node."
                  },
                  "geometry":{
                     "type":"Point",
                     "coordinates":[
                        7,
                        7
                     ]
                  }
               },
               "target":"https://iiif.example.org/canvas/123"
            },
            .
            .
            .
         ]
      }
   ]
}
```

### Example 3 
In this example, the agent does own the resource.  The agent wants to put the assertion directly on the resource without using the AnnotationPage. 
``` json-doc
{
   "id":"https://example.org/iiif/book1/canvas/p2",
   "type":"Canvas",
   "@context":"http://iiif.io/api/presentation/3/context.json",
   "label":{
      "none":[
         "pg. 2"
      ]
   },
   "height":1000,
   "width":750,
   "items":[],
   "service":[
      {
         "id":"https://example.org/geo/service/point(7,7)&format=geojson",
         "type":"GeoJSON_Serivce",
         "profile":"http://geojson.org/geojson-spec.html",
         "@context":"http://geojson.org/geojson-ld/geojson-context.jsonld",
         "properties":{
            "type":"Feature",
            "label":"String this geometry node should use as a label.",
            "description":"Some description to go along with node.",
            "motivation":"geocode"
         },
        "geometry":{
               "type":"Point",
               "coordinates":[
                  7,
                  7
               ]
            }
      },
      .
      .
      .
   ]
}
```
This has a small issue with how type clashes, but we can handle that within properties. However, that means FeatureCollections could not be used here, since FeatureCollections must not have properties. There would be no way to reconcile the type conflict. It is paramount the service return an array of Features here instead of a FeatureCollection.

# Presentation API 2
### Example 1
In this example, the agent does not own the resource and is attempting to make multiple third party assertion.  This can be done using an AnnotationList.
``` json-doc
{
   "@id":"http://example.org/annolist/123",
   "@context":"http://iiif.io/api/presentation/2/context.json",
   "@type":"sc:AnnotationList",
   "resources":[
      {
         "@type":"oa:Annotation",
         "motivation":"geocode",
         "resource":{
            "@id":"https://example.org/geojson/id/123",
            "@context":"http://geojson.org/geojson-ld/geojson-context.jsonld",
            "@type":"Feature",
            "properties":{
               "label":"String this geometry node should use as a label.",
               "description":"Some description to go along with node."
            },
            "geometry":{
               "type":"Point",
               "coordinates":[
                  7,
                  7
               ]
            }
         },
         "on":"https://iiif.example.org/canvas/123"
      },
       .
       .
       .
   ]
}
```

### Example 2
In this example, the agent does own the resource.  The agent still wants to use Annotations to describe the resource and wants to put those Annotations directly on the resource.  This can be done using an AnnotationList.
``` json-doc
{
   "@context":"http://iiif.io/api/presentation/2/context.json",
   "@id":"http://example.org/iiif/book1/canvas/p1",
   "@type":"sc:Canvas",
   "label":"p. 1",
   "height":1000,
   "width":750,
   "images":[],
   "otherContent":[
      {
         "@id":"http://example.org/annolist/123",
         "@context":"http://iiif.io/api/presentation/2/context.json",
         "@type":"sc:AnnotationList",
         "resources":[
            {
               "@type":"oa:Annotation",
               "motivation":"geocode",
               "resource":{
                  "@id":"https://example.org/geojson/id/123",
                  "@context":"http://geojson.org/geojson-ld/geojson-context.jsonld",
                  "@type":"Feature",
                  "properties":{
                     "label":"String this geometry node should use as a label.",
                     "description":"Some description to go along with node."
                  },
                  "geometry":{
                     "type":"Point",
                     "coordinates":[
                        7,
                        7
                     ]
                  }
               },
               "on":"https://iiif.example.org/canvas/123"
            },
             .
             .
             .
         ]
      }
   ]
}
```

### Example 3
In this example, the agent does own the resource.  The agent wants to put the assertion directly on the resource.  It is a bit different since service is not an array. That means your service will need to return a single FeatureCollection containing all the geographic data Features.
``` json-doc
{
   "@context":"http://iiif.io/api/presentation/2/context.json",
   "@id":"http://example.org/iiif/book1/canvas/p1",
   "@type":"sc:Canvas",
   "label":"p. 1",
   "height":1000,
   "width":750,
   "images":[],
   "otherContent":[],
   "service":{
      "@id":"https://example.org/geo/service/point-collection()&format=geojson",
      "@context":"http://geojson.org/geojson-ld/geojson-context.jsonld",
      "profile":"http://geojson.org/geojson-spec.html",
      "@type":"FeatureCollection",
      "features":[
         {
            "@type":"Feature",
            "properties":{
               "label":"String this geometry node should use as a label.",
               "description":"Some description to go along with node.",
               "motivation":"geocode"
            },
            "geometry":{
               "type":"Point",
               "coordinates":[
                  7,
                  7
               ]
            }
         }
      ]
   }
}
```

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116] [0116]
* [https://github.com/IIIF/iiif-stories/issues/119] [0119]
* [https://github.com/IIIF/iiif-stories/issues/125] [0125]
* [https://github.com/IIIF/iiif-stories/issues/135] [0135]

## Related Recipes
* [Geographical Assertios] [0TBD] - It is the same problem, only with a single assertion instead of multiple.
* [Annotation Specific Resources] [0023] - The same Annotation techniques seen here will work on specific resources.
* [Transcription/Translation] [0092] - The same Annotation aggregates AnnotationList and AnnotationPage combined with motivation will achieve this

{% include acronyms.md %}
{% include links.md %}