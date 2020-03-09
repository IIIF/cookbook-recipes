---
title: Geographical Assertion
layout: default
tags: [maps, geocode, annotation]
summary: "Make a geographical assertion about a IIIF resource."
---

### Use Case
Geographical knowledge of a IIIF resource is obtained. There is the need to assert that geographical information about the resource.

### Implementation Notes
* There are multiple scenarios that drive which pattern one may use to achieve this. If the agent making the assertion owns the resource, they may change the state of that resource to include the assertion directly on the JSON-LD object. Other scenarios include entirely third party assertions where the agent does not own the resource or even have permission to view it.
* `geocode` was used as the motivation throughout. The IIIF-Maps group is working on proper motivation extensions for the various kinds of assertions that could be made. The three main categories are `geocode`, `georeference` and `co-locate`.
* GeoJSON `properties` is a very generic field. If, for example, the targeted resource has a `label` and the `properties` field contains a `label`, the consuming interface must make a choice on which to preference for presentation purposes. This community should establish conventions to inject, override or extend resource properties.
* `geometry` can be more than just a `Point`.
* `target` values can include hash or SVG selectors. This would allow someone to annotate a fragment of a resource.

### Restrictions
In Presentation API 3, there is a minor conflict with the `type` field. See Presentation API 3 Example 3.

# Presentation API 3
### Example 1: third party annotation
In this example, the agent does not own the resource and it attempting a third party assertion. This can be done using an Annotation.
```json-doc
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
            48.86,
            2.34
         ]
      }
   },
   "target":"https://iiif.example.org/canvas/123"
}
```

### Example 2: embedded annotation
In this example, the agent does own the resource. The agent still wants to use Annotation to describe the resource and wants to put that Annotation directly on the resource. This can be done using an AnnotationPage.
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
         "id":"https://iiif.example.org/iiif/annopage/123",
         "type":"AnnotationPage",
         "items":[
            {
               "id":"https://iiif.example.org/annotation/12345",
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
                        48.86,
                        2.34
                     ]
                  }
               },
               "target":"https://iiif.example.org/canvas/123"
            }
         ]
      }
   ]
}
```

### Example 3: GeoJSON service
In this example, the agent does own the resource. The agent wants to put the assertion directly on the resource without using the AnnotationPage. 
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
   "service":[
      {
         "id":"https://example.org/geo/service/point(48.86,2.34)&format=geojson",
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
                   48.86,
                   2.34
               ]
          }
       }
   ]
}
```
**NOTE:** this GeoJSON had to type itself as a "Feature" inside its own `properties` field. This is because `type` is a required key descriptor for a service which causes a conflict between IIIF Presentation API 3 and GeoJSON standards.

# Presentation API 2
If an older API must be supported, note that the object structure is slightly different and some containers, like `AnnotationPage` are not available.
### Example 1: third party annotation
In this example, the agent does not own the resource and it attempting a third party assertion. This can be done using an AnnotationList.
``` json-doc
{
 "@id":"http://iiif.example.org/annolist/123",
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
                48.86,
                2.34
             ]
          }
       },
       "on":"https://iiif.example.org/canvas/123"
    }
 ]
}
```

### Example 2: embedded AnnotationList
In this example, the agent does own the resource. The agent still wants to use Annotation to describe the resource and wants to put that Annotation directly on the resource. This can be done using an AnnotationList within `otherContent`.
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
                        48.86,
                        2.34
                     ]
                  }
               },
               "on":"https://iiif.example.org/canvas/123"
            }
         ]
      }
   ]
}
```

### Example 3: GeoJSON service
In this example, the agent does own the resource. The agent wants to put the assertion directly on the resource without using the AnnotationPage. 
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
      "@id":"https://example.org/geo/service/point(48.86,2.34)&format=geojson",
      "@type":"Feature",
      "@context":"http://geojson.org/geojson-ld/geojson-context.jsonld",
      "profile":"http://geojson.org/geojson-spec.html",
      "properties":{
         "type":"Feature",
         "label":"String this geometry node should use as a label.",
         "description":"Some description to go along with node.",
         "motivation":"geocode"
      },
      "geometry":{
         "type":"Point",
         "coordinates":[
            48.86,
            2.34
         ]
      }
   }
}
```
**NOTE:** this GeoJSON had to type itself as a "Feature" inside its own `properties` field. This is because `type` is a required key descriptor for a service which causes a conflict between IIIF Presentation API 3 and GeoJSON standards.

## Related IIIF Stories
* [https://github.com/IIIF/iiif-stories/issues/116] [0116]
* [https://github.com/IIIF/iiif-stories/issues/119] [0119]
* [https://github.com/IIIF/iiif-stories/issues/125] [0125]
* [https://github.com/IIIF/iiif-stories/issues/135] [0135]

## Related Recipes
* [Multiple Geographical Assertions] [0TBD] - It is the same problem, only multiple assertions instead of a single assertion.
* [Annotation Specific Resources] [0023] - The same Annotation techniques seen here will work on specific resources.
* [Transcription/Translation] [0092] - The same Annotation aggregates AnnotationList and AnnotationPage combined with motivation will achieve this

{% include acronyms.md %}
{% include links.md %}
