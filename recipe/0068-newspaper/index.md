---
title: A basic newspaper
id: 68
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

Digitised Newspapers are more complicated than some other types of content as the hierarchy of Titles, Volumes and Issues are intrinsic in making them useful. The date of publication is also an important part of making Newspapers available. This recipe gives an example of a basic Newspaper with two issues and links to annotations which are generated through Optical Character Recognition (OCR) software. The aim is to give a good outline of common mapping solutions for Newspapers. 

## Implementation notes

This recipe was put together by Nuno Freire from Europeana and was discussed by the IIIF Newspaper Community Group. The example is a cut down Newspaper with two issues containing two pages. The OCR is at page level rather than article level. 

Newspapers can be modeled in a number of ways but for this example we are going to treat it as a Newspaper title with two issues. For a more complete discussion on Newspaper hierarchies and how they map to IIIF see the IIIF Newspaper Guidance notes. 

The Newspaper Title in this example is for a German Newspaper called the ‘Berliner Tageblatt’ and is hosted by Europeana. The Newspaper Title in IIIF is considered to be a IIIF Collection and as well as holding the metadata for a Newspaper title it also points to the issue IIIF Manifests through the items elements. One of the important features of Newspapers is the publication date which aids navigation. In the IIIF Collection you will see the following for each issue:
```
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
The navDate gives the date of publication and is contained both in the collection as well as the Manifest. This allows viewers to present a date based navigation for Newspaper collections. 

The IIIF Manifest is the equivalent of a Newspaper Issue and in these examples they both contain two pages. The navDate is again repeated at the Manifest level and it contains enough metadata to make the issue discoverable. For each canvas in this manifest you will see the following:
```
annotations": [
    {
        "id": "https://…./0068-newspaper/newspaper_issue_1-anno_p1.json",
        "type": "AnnotationPage"
    }
]
```

Which is the way to link OCR annotations to this Newspaper issue. See the Newspaper guidance for ways to link annotations in ALTO or other text formats. For this example the annotations are using the Web Annotations model and can be directly linked from the Canvas. 

## Example

This example is made up of five files:
 1. Title Collection
 2. Issue Manifests
    * With 2 canvases / pages
 3. 2 annotations lists for the first issue

The Newspaper title collection can be seen below
[JSON-LD](newspaper_title-collection.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="newspaper_title-collection.json" }
```json
```

The first issue Manifest can be seen below:
[JSON-LD](newspaper_issue_1-manifest.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="newspaper_issue_1-manifest.json" }
```json
```

The annotation collection for the first page of the first issue can be seen below:
[JSON-LD](newspaper_issue_1-anno_p1.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="newspaper_issue_1-anno_p1.json" }
```json
```

The other assets described above can be seen by navigating the URLs in the JSON documents. Note some asserts are hosted by Europeana. 

## Related recipes

Provide a bulleted list of related recipes and why they are relevant.
 * Newspaper general guidance
 * SeeAlso 

{% include acronyms.md %}
{% include links.md %}

