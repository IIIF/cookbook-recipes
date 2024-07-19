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

Similar to the initiatives crafted by other communities of practice in efforts to limit the scraping of images and text using “noai” and “noimageai” meta HTML tags, users of the IIIF APIs may consider implementing a set of tags/statements in their IIIF manifests to help better regulate ML/AI content scraping and non-consented or attributed use of IIIF powered content in ML/AI applications.

## Implementation Notes

Use of these standardized ML/AI Usage tags/statements in IIIF Manifests will always need to be paired with sophisticated, up-to-date DevOps and data security practices within the context of a repository environment.

Recommendation is to use a single applicable tag/statement, based on the particular concerns associated with an asset's use in ML/AI applications.

### Using `rights` statement URIs sourced from Wikidata

The examples shown here reference the Wikidata URIs for the different statements. As described in the [IIIF Presentation 3.0 `rights` property](https://iiif.io/api/presentation/3.0/#rights), URIs should be sourced from Creative Commons or RightsStatements.org. For URIs that do not reference either of these sources, the [`extensions`](https://iiif.io/api/presentation/3.0/#46-linked-data-context-and-extensions) mechanism using a source found in one of the [IIIF Registry of Known Extensions](https://iiif.io/api/registry/) can also be used. Wikidata is included in the  [Profiles Registry](https://iiif.io/api/registry/profiles/).

Please see the [goals statement on Stable URIs Development and Maintenance in the Ethical ML/AI Usage Tags Project Repository](https://github.com/alliomeria/ethical_ml_usage_tags/blob/main/README.md#stable-uris-development-and-maintenance) for information about the longer term plans regarding related URIs. When those stable URIs are finalized, a proposal will be made to add to the [Rights Registry](https://iiif.io/api/registry/rights/).

Aside from providing a link reference which typically leads to a static webpage that describes a license/statement in greater detail, a machineable outcome of the usage of Creative Commons or RightsStatement.org URIs within the `rights` property is the display of the corresponding license/statement icon or badge within one of the standard IIIF viewers (as shown in the example below). In the future, there may be ways to extend the machineable outcomes associated with these ML/AI Usage tags/statements (or other `rights` values) in ways that direct responses to machine-mediated interactions.

#### For machines, within [`rights`](https://iiif.io/api/presentation/3.0/#rights)

* No AI

```JSON
{ "rights": "https://www.wikidata.org/wiki/Q127515163" }
```

* No Image AI

```JSON
{ "rights": "https://www.wikidata.org/wiki/Q127516405" }
```

* Regulated ML/AI Use Permitted - Attribution Required

```JSON
{ "rights": "https://www.wikidata.org/wiki/Q127516763" }
```

* Regulated ML/AI Use Permitted - Consent Required

```JSON
{ "rights": "https://www.wikidata.org/wiki/Q127518037" }
```

#### For humans (public display), within [`requiredStatement`](https://iiif.io/api/presentation/3.0/#requiredstatement)

```JSON 
{
  "requiredStatement": {
    "label": { "en": [ "No AI" ] },
    "value": { "en": [ "Material related to this Digital Object should not be used for AI or ML training datasets." ] }
  }
}
```
```JSON
{
  "requiredStatement": {
  "label": { "en": [ "No Image AI" ] },
  "value": { "en": [ "Image-based material related to this Digital Object should not be used for AI or ML training datasets." ] }
  }
}
```
```JSON
{
  "requiredStatement": {
  "label": { "en": [ "Regulated ML/AI Use Permitted - Attribution Required" ] },
  "value": { "en": [ "material related to this Digital Object may be used for AI or ML training datasets, as long as Standard Attribution of source Digital Object Title and URL is maintained and referenced publicly for the ML/AI dataset." ] }
  }
}
```
```JSON
{
  "requiredStatement": {
  "label": { "en": [ "Regulated ML/AI Use Permitted - Consent Required" ] },
  "value": { "en": [ "Material related to this Digital Object may be used for AI or ML training datasets, if Prior Written Consent is obtained from the Source Holding Institution and Standard Attribution is maintained and referenced publicly." ] }
  }
}
```

#### Additional Considerations

* Simple use cases (apply per manifest) versus complex uses casses (apply per item/canvas)

* IIIF is an API based framework, geared to machine mediated interactions but: **IIIF resources are for humans** 

* As we, professionally and personally, decide to use or integrate ML/AI tools into our repositories, we need to keep in mind our curatorial legacies and the complex nature of our own content.

* ML/AI technology will continue to shift over time and require diligent application and monitoring, for the rest of our professional lives.

## Restrictions

No known restrictions.

## Example

The [IIIF 3.0 Specs](https://iiif.io/api/presentation/3.0/) restrict `rights` to a single value string format, and `requiredStatement` to a single value JSON Object. The example shown below uses a singe applicable ML/AI Usage statement Wikidata URI in `rights`, paired with a set of two human-readable `value` statements (one for ML/AI usage and one for a standard Creative Commons reference) in `requiredStatement` (structured as a single JSON object).

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="15-28"' %}

## Related Recipes

* [Rights][0008] for demonstrating use of `rights` and `requiredStatement`
