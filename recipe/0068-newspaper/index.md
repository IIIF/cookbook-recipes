---
title: A basic newspaper
id: 68
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

Digitized Newspapers are more complicated than some other types of content as the hierarchy of Titles, Volumes and Issues are important in making them accessible. The date of publication and providing access to OCR data are also important to the viewing experience. This recipe gives an example of a basic Newspaper with two issues and links to text generated from Optical Character Recognition (OCR) software. The aim is to give a good outline of common mapping solutions for Newspapers. 

## Implementation notes

This recipe was put together by Nuno Freire from Europeana and was discussed by the IIIF Newspaper Community Group. The example is a cut down Newspaper with two issues containing two pages. The OCR is at page level rather than article level. The example is for a German Newspaper called the ‘Berliner Tageblatt’ and is hosted by Europeana. In the IIIF domain a Newspaper Title is considered to be a __IIIF Collection__ and points to issue __IIIF Manifests__ through the `items` element. An issue in this example is considered to be the unit or edition that was published on a particular date. For a more complete discussion on Newspaper hierarchies and how they map to IIIF see the IIIF Newspaper Guidance notes. 

### Date of publication or navDate
One of the important features of Newspapers is the publication date which can allow the user to navigate issues by the date they were published. To achieve this we use the special [navDate](https://iiif.io/api/presentation/3.0/#navdate) property. This `navDate` should be added both to the items in a collection and also in the issue manifest. This allows viewers to present a date based navigation for Newspaper collections. 

The `navDate` is added to the collection in the items property for example:

Full JSON: [newspaper_title-collection.json](newspaper_title-collection.json)

{: class="line-numbers line-highlight" data-line="10,20"}
```json
"items": [
    {
      "id": "https://../newspaper_issue_1-manifest.json",
      "type": "Manifest",
      "label": {
        "de": [
          "Berliner Tageblatt - 1925-02-16"
        ]
      },
      "navDate": "1925-02-16T00:00:00Z"
    },
    {
      "id": "https://../newspaper_issue_2-manifest.json",
      "type": "Manifest",
      "label": {
        "de": [
          "Berliner Tageblatt - 1925-03-13"
        ]
      },
      "navDate": "1925-03-13T00:00:00Z"
    }
]
```

The `navDate` should also be present in the issue Manifest and can be seen in the example below:

Full JSON: [newspaper_issue_1-manifest.json](newspaper_issue_1-manifest.json)

{: class="line-numbers line-highlight" style="max-height: 15em;" data-line="9"}
```json
{
    "id": "https://.../newspaper_issue_1-manifest.json",
    "type": "Manifest",
    "label": {
            "de": [
                    "Berliner Tageblatt - 1925-02-16"
            ]
    },
    "navDate": "1925-02-16T00:00:00Z"
}, 
```

For Editions, a temporal value can be inserted to enforce navigation order. `navDate` is not an assertion of when an issue was published but instead a datetime useful for navigation. Therefore, you can use a `06:00` timestamp for a morning edition and a `17:00` for an evening edition to provide browse order.

### Linking to Annotations
Digitized Newspapers often have associated OCR text and to make this available in a IIIF viewer it needs to be in the form of W3C annotations linked from the Newspaper page. An example of this link between page (or IIIF canvas) can be seen highlighted below:

Full JSON: [newspaper_issue_1-manifest.json](newspaper_issue_1-manifest.json)

{: class="line-numbers line-highlight" data-line="35-40"}
```json
{
  "id": "https://iiif.europeana.eu/presentation/9200355/BibliographicResource_3000096302513/canvas/p1",
  "type": "Canvas",
  "label": {
    "none": [
      "p. 1"
    ]
  },
  "items": [
    {
      "id": "https://iiif.europeana.eu/presentation/9200355/BibliographicResource_3000096302513/annotation_page_painting/ap1",
      "type": "AnnotationPage",
      "items": [
        {
          "id": "https://iiif.europeana.eu/presentation/9200355/BibliographicResource_3000096302513/annotation/p1",
          "type": "Annotation",
          "motivation": "painting",
          "body": {
            "id": "https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p1/full/max/0/default.jpg",
            "type": "Image",
            "format": "image/jpeg",
            "service": [
              {
                "id": "https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p1",
                "type": "ImageService3",
                "profile": "level1"
              }
            ]
          },
          "target": "https://iiif.europeana.eu/presentation/9200355/BibliographicResource_3000096302513/canvas/p1"
        }
      ]
    }
  ],
  "annotations": [
    {
      "id": "https://../newspaper_issue_1-anno_p1.json",
      "type": "AnnotationPage"
    }
  ]
},
```

The linked annotations are in the form of an AnnotationPage and an example is below. 

Full JSON: [newspaper_issue_1-anno_p1.json](newspaper_issue_1-anno_p1.json)

{: class="line-numbers line-highlight" data-line="9, 16"}
```json
{
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": "https://../newspaper_issue_1-anno_p1.json",
    "type": "AnnotationPage",
    "items": [
        {
            "id": "https://data.europeana.eu/annotation/9200355/BibliographicResource_3000096302513/20b3b1f4cb15f062e53fd50d584d66ff",
            "type": "Annotation",
            "motivation": "supplementing",
            "body": {
                "type": "TextualBody",
                "format": "text/plain",
                "language": "de",
                "value": "84"
            },
            "target": "https://iiif.europeana.eu/presentation/9200355/BibliographicResource_3000096302513/canvas/p1#xywh=182,476,59,43"
        },
 
```

__Note__:
 * The annotation `motivation` for OCR content should be `supplementing`
 * The target of the annotation should be the Canvas ID followed by a # then the x, y, width and height of the portion of the image the text represents. 

### Linking to ALTO text

As well as linking to annotations, it is a common use case with Newspapers to link to other formats of the OCR text including ALTO. This is achieved by using a `seeAlso` property within the canvas. For example:

Full JSON: [newspaper_issue_1-manifest.json](newspaper_issue_1-manifest.json)

{: class="line-numbers line-highlight" data-line="9-15"}
```json
{
  "id": "https://iiif.europeana.eu/presentation/9200355/BibliographicResource_3000096302513/canvas/p1",
  "type": "Canvas",
  "label": {
    "none": [
      "p. 1"
    ]
  },
  "seeAlso": [{
      "id":"https://../newspaper_issue_1-alto_p1.xml",
      "type": "Text",
      "format":"application/xml",
      "profile": "http://www.loc.gov/standards/alto/",
      "label": { "en": ["ALTO XML"] }
  }],
  "items": [
    {
        ...
    }
  ],
  "annotations": [
    {
      "id": "https://../newspaper_issue_1-anno_p1.json",
      "type": "AnnotationPage"
    }
  ]
},
```


## Example

The complete example is made up of a number of different files:
1. Newspaper Title IIIF Collection - [newspaper_title-collection.json](newspaper_title-collection.json)
2. 1st Issue Manifest - [newspaper_issue_1-manifest.json](newspaper_issue_1-manifest.json)
* Page 1
  * Annotations - [newspaper_issue_1-anno_p1.json](newspaper_issue_1-anno_p1.json)
  * Linked ALTO - [newspaper_issue_1-alto_p1.xml](newspaper_issue_1-alto_p1.xml)
* Page 2
  * Annotations - [newspaper_issue_1-anno_p2.json](newspaper_issue_1-anno_p2.json)
  * Linked ALTO - [newspaper_issue_1-alto_p2.xml](newspaper_issue_1-alto_p2.xml)
3. 2nd Issue Manifest - [newspaper_issue_2-manifest.json](newspaper_issue_2-manifest.json)
    * Page 1
        * Annotations - [newspaper_issue_2-anno_p1.json](newspaper_issue_2-anno_p1.json)
        * Linked ALTO - [newspaper_issue_2-alto_p1.xml](newspaper_issue_2-alto_p2.xml)
    * Page 2
        * Annotations - [newspaper_issue_2-anno_p2.json](newspaper_issue_2-anno_p2.json)
        * Linked ALTO - [newspaper_issue_2-alto_p2.xml](newspaper_issue_2-alto_p2.xml)

__Note__:

The first issue links to a version 3.0 image API endpoint:

{: class="line-numbers line-highlight" data-line="6-10"}
```json
"body": {
    "id": "https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p1/full/max/0/default.jpg",
    "type": "Image",
    "format": "image/jpeg",
    "service": [
      {
        "id": "https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p1",
        "type": "ImageService3",
        "profile": "level1"
      }
    ]
},
```

but the second issue links to Europeana hosted version 2 images:

{: class="line-numbers line-highlight" data-line="6-10"}
```json
"body": {
    "id": "https://iiif.europeana.eu/image/3UU6R3RRZZGU2VNISCQX7N474GR7X4VMGYBTIWV2SNCBRGSR2WAA/presentation_images/ea1ba210-ffd3-11e5-b68d-fa163e60dd72/node-2/image/SBB/Berliner_Tageblatt/1925/03/13/0/F_SBB_00001_19250313_054_123_0_001/full/full/0/default.jpg",
    "type": "Image",
    "format": "image/jpeg",
    "service": [
      {
        "@id": "https://iiif.europeana.eu/image/3UU6R3RRZZGU2VNISCQX7N474GR7X4VMGYBTIWV2SNCBRGSR2WAA/presentation_images/ea1ba210-ffd3-11e5-b68d-fa163e60dd72/node-2/image/SBB/Berliner_Tageblatt/1925/03/13/0/F_SBB_00001_19250313_054_123_0_001",
        "@type": "ImageService2",
        "profile": "http://iiif.io/api/image/2/level1.json"
      }
    ]
},
```
This was to ensure there is an example hosted by Europeana and also an example with images available as version 3.0. 

## Related recipes

Provide a bulleted list of related recipes and why they are relevant.
 * Newspaper general guidance
 * SeeAlso 

{% include acronyms.md %}
{% include links.md %}

