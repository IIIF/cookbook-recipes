---
title: Multimedia Canvas
id: 499
layout: recipe
tags: Complex Object
summary: "tbc"
viewers:
 - Annona
 - UV
 - Mirador
 - Clover
 - Glycerine
topic: 
 - complex
---

## Use Case

You want to engage in some form of digital storytelling with one or more AV resources painted onto the same Canvas as a still image that will serve as a background. You want part of the still image to remain visible behind any video AV resources while they play. This storytelling might happen in the context of teaching narrative techniques in curricular settings, as a component of scholarly communications around research output, or for other reasons and in other contexts.

## Implementation Notes

This recipe pulls together techniques and structures described in previous recipes. 
Multiple `item`s on one Canvas as in 0036
Differing dimensions of a resource and Canvas as in 0004 but sizing and placing the resource 
New: Mixing video (AV) and still image resources

## Restrictions

No restrictions known.

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Simple Image Manifest][0001]
* [Image and Canvas with Differing Dimensions][0004] for thinking through relative dimensioning of a resource and a Canvas

{% include acronyms.md %}
{% include links.md %}

