---
title: Simple Annotation — Tagging
id: 21
layout: recipe
tags: [annotation]
summary: "Tagging as a basic annotation"
---

## Use Case

For a IIIF resource, you'd like to add a simple annotation to the resource. This commentary might call out a particular element or feature of an image with a tag. Such a tag, as part of a manifest for the resource, would become discoverable and potentially aggregated with other identical or similar tags across the IIIF resources of one or more institutions.

## Implementation Notes

This recipe demonstrates one of many possibilities for using an Annotation to tag a resource or a portion of a resource. At the base of tags in IIIF is the [W3 Web Annotation Data Model](http://w3.org/TR/annotation-model/), which you are encouraged to consult. A tag in IIIF is a web annotation with a `motivation` or `purpose` of `tagging`. Use `motivation` on the Annotation when there is one Annotation `body` of the type TextualBody, and use `purpose` within an Annotation `body` when it 

It's worth noting that Annotations such as tags are permitted to use the `behavior` property with a value of `hidden` if viewers and other consuming clients should be told to not display the tag.

## Restrictions

None known.

## Example

In this manifest, we use the same photograph of Göttingen from the 2019 IIIF annual conference, a photo that has provided the resource for some other basic recipes. We're introducing an annotation to demonstrate tagging by calling out the statue on the top of a fountain, a notable landmark of its city.

Because the statue is not the sole or dominant element of the photo, we've targeted the tag to a portion of the photo using fragment selector syntax. The fragment could also be implemented by turning the `target` of the tagging annotation into a JSON object.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="64-98"' %}

## Related Recipes

* [Fragment Selectors][0020]
* [Annotation in the context of a particular content resource][0023]

{% include acronyms.md %}
{% include links.md %}

