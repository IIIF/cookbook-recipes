---
title: IIIF cookbook recipes
layout: default
tags: [maps, geocode, annotation]
summary: "Make a geographical assertion about a IIIF resource."
---

### Use Case
Geographical knowledge of a IIIF resource is obtained.  There is the need to assert that geographical information about the resource.


### Implementation Notes
There are multiple scenarios that drive which pattern one may use to achieve this.  If the agent making the assertion owns the resource, they may change the state of that resource to include the assertion directly on the JSON-LD object.  Other scenarios include entirely third party assertions where the agent does not own the resource or even have permission to view it.

### Restrictions
In Presentation API 3, there is a conflict with the "type" field.  

# Presentation API 3
### Example 1
## In this example, the Agent does not own the resource and it attempting a third party assertion.  This can be done using an Annotation.
``` json-doc
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
}
```

### Example 2
## In this example, the Agent does own the resource.  The Agent still wants to use Annotation to describe the resource and wants to put that Annotation directly on the resource.  This can be done using an AnnotationPage.
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
   "items":[

   ],
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
            }
         ]
      }
   ]
}
```

### Example 2
## In this example, the Agent does own the resource.  The Agent wants to put the assertion directly on the resource without using the AnnotationPage. 
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
   "items":[

   ],
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
       }
   ]
}
```


# Presentation API 2
### Example 1
## In this example, the Agent does not own the resource and it attempting a third party assertion.  This can be done using an AnnotationList.
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
    }
 ]
}
```

### Example 2
## In this example, the Agent does own the resource.  The Agent still wants to use Annotation to describe the resource and wants to put that Annotation directly on the resource.  This can be done using an AnnotationList.
``` json-doc
{
   "@context":"http://iiif.io/api/presentation/2/context.json",
   "@id":"http://example.org/iiif/book1/canvas/p1",
   "@type":"sc:Canvas",
   "label":"p. 1",
   "height":1000,
   "width":750,
   "images":[

   ],
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
            }
         ]
      }
   ]
}
```

### Example 3
## In this example, the Agent does own the resource.  The Agent wants to put the assertion directly on the resource without using the AnnotationPage. 
``` json-doc
{
   "@context":"http://iiif.io/api/presentation/2/context.json",
   "@id":"http://example.org/iiif/book1/canvas/p1",
   "@type":"sc:Canvas",
   "label":"p. 1",
   "height":1000,
   "width":750,
   "images":[

   ],
   "otherContent":[

   ],
   "service":{
      "@id":"https://example.org/geo/service/point(7,7)&format=geojson",
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
            7,
            7
         ]
      }
   }
}
```