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

Conforming clients may render the `homepage` property in various ways, yet most likely as an HTML Anchor element for each entry. An alternative consideration could be as a button.

If an anchor is utilized for the instance, the `id` represents the destination of the link and would serve as the value for its `href` attribute.

The label is rendered as the content within the link according to the [Language of Property Values](https://iiif.io/api/presentation/3.0/#language-of-property-values). A client may also choose to provide a `lang` attribute on the anchor element with a value of the determined BCP 47 language code of the `label`.

Entries of a homepage property may also have a `language` property. These values represent the language(s) of the destination web page. A client may also render a _single_ language entry as the value for `hreflang` attribute on the anchor element.

## Restrictions

Web pages related to the Manifest that are not its home should utilize the `metadata property` as a `label` and `value` pair.

## Example

{% include manifest_links.html viewers="Mirador, Clover" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="26-36"' %}

## Related Recipes

{% include acronyms.md %}
{% include links.md %}
