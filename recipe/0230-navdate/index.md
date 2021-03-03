---
title: Chronology with navDate
id: 230
layout: recipe
tags: [date]
summary: "tbc"
---

## Use Case

You have one or more IIIF resources that have dates associated with them, and would like to communicate their dates to a consuming client for putting in a date-based interface. For instance, you might want to have the IIIF object presented in a timeline or calendar feature. Over the spread of a group of resources, consistent use of `navDate` allows for computational addressing of the collection as data and arrangement in chronological order.

## Implementation Notes

The `navDate` property, somewhat as implied by its name, allows a manifest to identify a pertinent date associated with an IIIF resource in order to help viewers provide users with date-aware navigation. This property is intended for consumption by computer agents. More descriptive date ranges, intended for display directly to the user, should be included in `metadata` property entries.

The value of the `navDate` property must be an [XSD dateTime literal](https://www.w3.org/TR/xmlschema11-2/#dateTime) with a timezone. The timezone should be in the UTC + "Z" format, but may instead have the difference from UTC given in the value in the "+hh:mm" format. If a Canvas using `navDate` also contains a `duration` property, the `navDate` for that Canvas is the date and time of the start of the resource's content. Use "01" for an unknown month or day, and "00" for any unknown time portion.

Only Collections, Manifests, Ranges, and Canvases are permitted to contain a `navDate` property, and the property may appear only once within each resource. Conforming clients are directed to ignore `navDate` on other resources

## Restrictions

None known.

## Example

Note that this recipe presents merely one Canvas with a `navDate` property in part due to the lack of viewer support at this time. If you have access to an interface that provides date-aware navigation, you may expand this manifest with other maps in this series, available at the [US Library of Congress](https://www.loc.gov/maps/?q=Chesapeake+and+Ohio+Canal&fa=contributor%3Aunited+states.+national+park+service&st=list&c=100).

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="19"' %}

The direct link to the fixture is a useful convenience.

## Related Recipes

{ For sketching only: 
* sequence Range behavior, insofar as this is a way to order and re-order Canvases
* thumbnail-nav Range behavior for the same reason
* start for similar reasons
* [0006] newspaper
}

{% include acronyms.md %}
{% include links.md %}

