---
title: Resources on a Timeline
id: 560
layout: recipe
tags: timleline
summary: "Placing resources on a timeline independent of format and individual duration"
viewers:
topic:
 - realWorldObject
---

## Use Case

You have a group of photographs taken in a temporal sequence that you would like to present as a simulation of animation, in the manner of a zoetrope.

## Implementation Notes

What do you need to know to use this pattern?
How do you implement the pattern?

This recipe is very similar to [Composition from Multiple Images][0036], which describes using multiple IIIF resources on a single Canvas. The substantial difference between that recipe and this one is the incorporation of the `duration` property and timing fragment references in the `target` URLs.

## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.?

Delete this section if it is not needed.
If you don't know what the restrictions might be initially, just leave the following line:
**Unknown - Help Needed**

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="UV, Mirador, Annona, Clover, Ramp, Aviary, Glycerine, Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

* [Composition from Multiple Images][0036] for using multiple IIIF resources on a single Canvas
