---
title: Navigation by Chronology
id: 230
layout: recipe
tags: [date]
summary: "tbc"
---

## Use Case

You have one or more IIIF resources that have dates associated with them, and would like to communicate their dates to a consuming client for putting in a date-based interface. For instance, you might want to have the IIIF object presented in a timeline or calendar feature. Over the spread of a group of resources, consistent use of [`navDate`](https://iiif.io/api/presentation/3.0/#navdate) allows for computational addressing of the collection as data and arrangement in chronological order.

## Implementation Notes

The `navDate` property, somewhat as implied by its name, allows a manifest to identify a pertinent date associated with an IIIF resource in order to help viewers provide users with date-aware navigation. Clients are not required to make use of `navDate`, and clients that do have date-aware navigation available may not default to that navigation interface.

This property is intended for consumption only by computer agents. More descriptive date ranges, intended for display directly to humans, should be included in `metadata` property entries.

The value of the `navDate` property must be an [XSD dateTime literal](https://www.w3.org/TR/xmlschema11-2/#dateTime) with a timezone. The timezone should be in the UTC + "Z" format, but may instead have the difference from UTC given in the value in the "+hh:mm" format. If a Canvas using `navDate` also contains a `duration` property, the `navDate` for that Canvas is the date and time of the start of the resource's content. Use "01" for an unknown or inexact month or day, and "00" for any unknown or inexact time portion.

Only Collections, Manifests, Ranges, and Canvases are permitted to contain a `navDate` property, and the property may appear only once within each resource. Conforming clients are directed to ignore `navDate` on other resources.

## Restrictions

None known.

## Example

This recipe presents an imaginary Collection containing 2 instances from the run of a particular national park map held at the United States' Library of Congress. If you want to expand this example locally, you may find other maps in this series, at the [Library of Congress website](https://www.loc.gov/maps/?q=Chesapeake+and+Ohio+Canal&fa=contributor%3Aunited+states.+national+park+service&st=list&c=100).


### Collection

{% include manifest_links.html viewers="UV, Mirador" manifest="navdate-collection.json" %}

{% include jsonviewer.html src="navdate-collection.json" config='data-line="35,45"' %}

### 1986 Map

{% include manifest_links.html viewers="UV, Mirador" manifest="navdate_map_2-manifest.json" %}

{% include jsonviewer.html src="navdate_map_2-manifest.json" config='data-line="10"' %}

### 1987 Map

{% include manifest_links.html viewers="UV, Mirador" manifest="navdate_map_1-manifest.json" %}

{% include jsonviewer.html src="navdate_map_1-manifest.json" config='data-line="10"' %}


## Related Recipes

* [Table of Contents for Book Chapters][0024] demonstrates ordering resources with a Range
* [Alternative Sequence (via `sequence` Range)][0027] demonstrates providing an order for resources different from the default
* [A manuscript with multiple orderings][0070] demonstrates a real-world issue and how multiple ordering possibilities address it
* [Thumbnail range for video navigation][0073] shows how to order thumbnails from a video resource for navigation
* [Basic Newspaper][0068] demonstrates use of `navDate` with multiple Manifests

{% include acronyms.md %}
{% include links.md %}

