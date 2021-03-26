---
title: Acknowledge Content Contributors with `provider`
id: 234
layout: recipe
tags: [tbc]
summary: "tbc"
---

## Use Case

You have a IIIF resource for which you would like to include information about one or more organizations or people that contributed to providing the content of the resource. You want to include a rich set of information for each contributor so clients can make visible this information in a similarly robust way. The [`provider`](https://iiif.io/api/presentation/3.0/#provider) property allows you an elastic way to acknowledge contributions with as little as a name and as much as a name, `homepage`, one or more `logo`s, and a `seeAlso` machine-readable description for the contributor.

## Implementation Notes

What do you need to know to use this pattern?
How do you implement the pattern?

## Restrictions

None known.

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [FPO related recipe 01][0005]
* [FPO related recipe 02][0005]

{% include acronyms.md %}
{% include links.md %}

