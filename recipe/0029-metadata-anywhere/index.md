---
title: Metadata on any resource
id: 29
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

I have interesting information to show at all levels of the IIIF model - how do I do that?

## Implementation notes

An ordered list of descriptions to be displayed to the user when they interact with the resource, given as pairs of human readable label and value entries. The content of these entries is intended for presentation only; descriptive semantics should not be inferred. An entry might be used to convey information about the creation of the object, a physical description, ownership information, or other purposes.

The value of the metadata property must be an array of JSON objects, where each item in the array has both label and value properties. The values of both label and value must be JSON objects, as described in the languages section.

## Restrictions

Language maps and arrays required... see...

## Example

Describe in prose and provide examples, e.g.:

Credit: John Dee performing an experiment before Queen Elizabeth I. Oil painting by Henry Gillard Glindoni. Credit: Wellcome Collection. Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="10-59, 84-97, 137-150"' %}

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}
