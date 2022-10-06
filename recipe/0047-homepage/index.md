---
title: Linking to Web Page of an Object
id: 47
layout: recipe
tags: [metadata, presentation]
summary: "tbc"
viewers:
  - Mirador
  - Clover
topic: property
property: homepage
---

## Use Case

You have a IIIF Manifest representing an object that is also represented by one or more web pages. These web pages may be published by the organization responsible for the object as well as its Manifest resource. For each homepage entry, an actionable route would be provided to a web page able to be displayed to the user.

## Implementation Notes

Conforming clients may render the `homepage` property in various ways, yet most likely as an HTML anchor element for each entry. An alternative consideration could be as a button.

If an anchor is utilized for the instance, the `id` represents the destination of the link and would serve as the value for its `href` attribute.

The label is rendered as the content within the link according to the [Language of Property Values](https://iiif.io/api/presentation/3.0/#language-of-property-values). A client may also choose to provide a `lang` attribute on the anchor element with a value of the determined BCP 47 language code of the `label`.

Entries of a homepage property may also have a `language` property. These values represent the language(s) of the destination web page. A client may also render a _single_ language entry as the value for `hreflang` attribute on the anchor element.

## Restrictions

Web pages related to the Manifest that are not its home should utilize the `metadata property` as a `label` and `value` pair.

## Example

In this example we have a Manifest representing an object housed at the Yale Center for British Art. A `homepage` property is at the Manifest level with one entry. The single instance references the URL at which a user could be displayed a web page of the object’s catalog entry.

_Greenland Falcon._ Beeswax on panel by George Stubbs. Credit: Yale Center for British Art, Paul Mellon Collection. Public Domain Dedication (CC0 1.0 Universal)

{% include manifest_links.html viewers="Mirador, Clover" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="60-74"' %}

## Related Recipes

* [Acknowledge Content Contributors][0234] for demonstrating the use of `homepage` for a `provider`
* [Linking to Structured Metadata][0053] for demonstrating the use of `seeAlso`

{% include acronyms.md %}
{% include links.md %}
