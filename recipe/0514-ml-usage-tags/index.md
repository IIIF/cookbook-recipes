---
title: IIIF ML/AI Usage Tags Recipe
id: 
layout: recipe
tags: [rights, requiredStatement]
summary: "Ethical ML/AI Use Tags for IIIF Manifests"
viewers:
 - Mirador
 - UV
topic: note
property: rights, requiredStatement   
---

## Use Case

Similar to the initiatives crafted by other content communities in efforts to limit the scraping of images and text using “noai” and “noimageai” meta HTML tags, users of the IIIF APIs may consider implementing a set of tags their IIIF manifests to help better regulate ML/AI content scraping and non-consented or attributed use of IIIF powered content in ML/AI applications.

## Implementation Notes

Use of these standardized ML/AI Usage tags in IIIF Manifests will always need to be paired with sophisticated, up-to-date DevOps and data security practices within the context of a repository environment.

Recommendation to use a single applicable tag, based on the particular concerns associated with an asset's use in ML/AI applications.

#### For humans, within [`requiredStatement`](https://iiif.io/api/presentation/3.0/#requiredstatement)

```JSON 
{
  "requiredStatement": {
    "label": { "en": [ "No AI" ] },
    "value": { "en": [ "Material related to this IIIF Manifest should not be used for AI or ML training datasets." ] }
  }
}
```
```JSON
{
  "requiredStatement": {
  "label": { "en": [ "No Image AI" ] },
  "value": { "en": [ "Image-based material related to this IIIF Manifest should not be used for AI or ML training datasets." ] }
  }
}
```
```JSON
{
  "requiredStatement": {
  "label": { "en": [ "Regulated ML/AI Use Permitted - Attribution Required" ] },
  "value": { "en": [ "Material related to this IIIF Manifest may be used for AI or ML training datasets, as long as Standard Attribution of source content is maintained for the ML/AI dataset. Original URL of source IIIF manifest must be maintained and referenced." ] }
  }
}
```
```JSON
{
  "requiredStatement": {
  "label": { "en": [ "Regulated ML/AI Use Permitted - Consent Required" ] },
  "value": { "en": [ "Material related to this IIIF Manifest may be used for AI or ML training datasets, if Prior Written Consent is obtained from the source holding institution. Standard Attribution of source content must be maintained for the ML/AI dataset. Original URL of source IIIF manifest must be maintained and referenced." ] }
  }
}
```

#### For machines, within [`rights`](https://iiif.io/api/presentation/3.0/#rights)

* URIs to be pursued for machineable interactions, pending further discussions within the IIIF and wider repository communities during Summer 2024 and onwards.

#### Additional Considerations

* Simple use cases (apply per manifest) versus complex uses casses (apply per item/canvas)

* IIIF is an API based framework, geared to machine mediated interactions but: **IIIF resources are for humans** 

* As we, professionally and personally, decide to use or integrate ML/AI tools into our repositories, we need to keep in mind our curatorial legacies and the complex nature of our own content.

* ML/AI technology will continue to shift over time and require diligent application and monitoring, for the rest of our professional lives.

## Restrictions

No known restrictions.

## Example

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="16-28"' %}

## Related Recipes

* [Rights][0008] for demonstrating use of `rights` and `requiredStatement`
