---
title: Image Rotation with Image Service
id: 40
layout: recipe
tags: image, manipulation
summary: Rotating a portion of an image using a IIIF Image API service
viewers:
topic: 
 - basic
---

## Use Case

You have a codex that has been scanned and prepared for online display. The work was digitized by scanning single pages, and one page's image is mistakenly rotated 90 degrees. Rather than altering the original scan files or re-scanning the work, you'd like to make an adjustment at the presentation level so viewers will display the page in the same layout as the other pages.

## Implementation Notes


## Restrictions

This approach is not usable if you do not have a IIIF Image API service for the image, or if your image server does not allow rotation through service calls.

## Example

For this recipe, we conveniently had a work on hand that had one page of a spread oriented perpendicularly to the facing page. Inconveniently, the work was scanned as spreads, making rotation a little more difficult. The outcome was to use both the image's IIIF API Image service for rotation and a fragment specifier to direct the service to rotate just the image portion desired. 

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Image Rotation with CSS][0039]

{% include acronyms.md %}
{% include links.md %}

