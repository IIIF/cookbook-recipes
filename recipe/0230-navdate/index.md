---
title: Chronology with navDate
id: 230
layout: recipe
tags: [date]
summary: "tbc"
---

## Use Case

You have one or more periodical articles (journal, magazine, etc.) in IIIF form and would like to communicate their dates to a consuming client for putting in a date-based interface. For instance, you might want to have the IIIF object in a client's timeline or calendar feature. Over the spread of a group of resources, consistent and accurate use of `navDate` allows for computational addressing of the collection as data and arrangement in chronological order.

## Implementation Notes

If any of your Canvases contain a `duration` property, the `navDate` for that Canvas is for the start of the resource.

Only Collections, Manifests, Ranges, and Canvases are permitted to contain a `navDate` property, and the property may appear only once within each resource. Conforming clients are directed to ignore `navDate` on other resources

The value of the `navDate` property must be an [XSD dateTime literal](https://www.w3.org/TR/xmlschema11-2/#dateTime) with a timezone. The timezone should be in the UTC + "Z" format, but may instead have the difference from UTC given in the value in the "+hh:mm" format.

This property is intended for consumption by computer agents. More descriptive date ranges, intended for display directly to the user, should be included in `metadata` property entries.

## Restrictions

None known.

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

{ For sketching only: 
* sequence Range behavior, insofar as this is a way to order and re-order Canvases
* thumbnail-nav Range behavior for the same reason
* start for similar reasons
}

{% include acronyms.md %}
{% include links.md %}

