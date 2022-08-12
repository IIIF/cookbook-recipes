---
title: Simple Annotation — Tagging
id: 21
layout: recipe
tags: [annotation]
summary: "Tagging as a basic Annotation"
viewers:
 - Mirador  
 - Annona
topic: annotation
---

## Use Case

For a IIIF resource, you'd like to add a simple Annotation to the resource. This annotation might call out a particular element or feature of an image as a tag. Such a tag, as part of a Manifest for the resource, would become discoverable and potentially aggregated with other identical or similar tags across the IIIF resources of one or more institutions.

## Implementation Notes

This recipe demonstrates a simple way to use an Annotation to tag a IIIF resource or a portion of a IIIF resource: an Annotation with a `motivation` property that has a value of `tagging`. The foundation of tags in IIIF is the [W3C Web Annotation Data Model](http://w3.org/TR/annotation-model/), which you are encouraged to consult.

Though it is not demonstrated here, it's worth noting that Annotations such as tags are permitted to use the `behavior` property with a value of `hidden`. With that property so set, viewers and other consuming clients should not display the tag by default, but should allow the user to determine the tag's visibility.

## Restrictions

None known.

## Example

In this Manifest, we use a photograph of Göttingen from the 2019 IIIF annual conference, one that has provided the resource for some other basic recipes in this cookbook. We're introducing an Annotation to demonstrate tagging by calling out the statue on the top of a fountain, a notable landmark of its city.

Because the statue is not the sole or dominant element of the photo, we've targeted the tag to a portion of the photo using fragment selector syntax.

{% include manifest_links.html viewers="Mirador,Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="44-63"' %}

## Related Recipes

* [Fragment Selectors][0020]

{% include acronyms.md %}
{% include links.md %}

