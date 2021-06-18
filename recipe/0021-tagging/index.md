---
title: Simple Annotation — Tagging
id: 21
layout: recipe
tags: [annotation]
summary: "Tagging as a basic annotation"
---

## Use Case

For a IIIF resource, you'd like to associate commentary with the resource. This commentary might call out a particular element or feature of an image

## Implementation Notes

What do you need to know to use this pattern?
How do you implement the pattern?

It's worth noting that Annotations such as tags are permitted to use the `behavior` property with a value of `hidden` if viewers and other consuming clients should be told to not display the tag.

## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.? 

Delete this section if it is not needed.
If you don't know what the restrictions might be initially, just leave the following line:
**Unknown - Help Needed**

## Example

In this manifest, we use the same photograph from the IIIF annual conference in [year] from some other basic recipes. The annotation to demonstrate tagging notes the statue on the top of a fountain, which in turn is a notable landmark of its city.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="64-98"' %}

## Related Recipes

* 0001
* 0008 rights/required statement
* 

{% include acronyms.md %}
{% include links.md %}

