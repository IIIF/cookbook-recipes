---
title: Chronology with navDate
id: 230
layout: recipe
tags: [date]
summary: "tbc"
---

## Use Case

You have one or more periodical articles (journal, magazine, etc.) in IIIF form and would like to communicate their dates to a consuming client for the client to put in a chronological framing. For instanct, you might want to have the IIIF object in a timeline or calendar, with similar or disparate objects. Over the spread of a collection, consistent and accurate use of `navDate` allows for computational addressing of the collection as data 

## Implementation Notes

What do you need to know to use this pattern?
How do you implement the pattern?

## Restrictions

This property is intended for consumption by computer agents. More descriptive date ranges, intended for display directly to the user, should be included in `metadata` property entries.

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

