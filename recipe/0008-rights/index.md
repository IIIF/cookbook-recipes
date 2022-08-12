---
title: Rights statement
id: 8
layout: recipe
tags: [text, presentation]
summary: "You want to assert a license or rights statement that applies to the content of the resource, such as the JSON of a Manifest or the pixels of an image."
viewers:
 - UV
 - Mirador
 - Annona
topic: property
property: rights, requiredStatement
---

## Use Case

You are able to implement the inclusion of a license, rights, or other important statement about a resource (e.g. a Manifest's JSON or an image's pixels) by using the `rights`, `requiredStatement`, and `metadata` properties. This recipe will focus on the first two; see [the Presentation 3.0 spec on `metadata`](https://iiif.io/api/presentation/3.0/#metadata) for more information about that property.

While you may use `rights` and `requiredStatement` similarly for the function of asserting certain important information (e.g. reproduction rights, ownership, collection name), the properties do have material differences. These are the most salient:
+ **Content**: The `rights` value must be a Creative Commons license URI, a RightsStatements.org URL, or added through the extension process. The `requiredStatement` value, on the other hand, can be any content, such as a copyright or institutional URI or text.
+ **Rendering**: Clients must render `requiredStatement` content on every resource type (even if hidden at first), but `rights` content may or may not be rendered visibly.
+ **Property Value**: The `rights` property value must be a string, and must be a URI defined by Creative Commons or RightsStatement.org if you are using one of those specifications. On the other hand, the `requiredStatement` value must be a single JSON object with `label` and `value` properties; `metadata` values must be an array of JSON objects, where each object has the `label` and `value` properties.
+ **Resource Applicability**: Any resource type may have `rights` or `requiredStatement`. However, `rights` is only for license or rights to the resource, while `requiredStatement` can be any text the publishing organization deems critical to display to the user.

If user visibility of the information or a publisher-defined label is paramount, use `requiredStatement` or `metadata`. Resources may include all three properties.

## Implementation notes

Because the `rights` property may not necessarily be visible to the user, it should be considered primarily machine-oriented. Therefore, URIs in this property should use target entities' machine-actionable URIs and their appropriate protocols. In the cases of Creative Commons licenses or RightsStatements.org statements, those protocols are HTTP, not HTTPS. Note, though, that clients may rewrite the content to use HTTPS if and as the URIs are made visible to users.

Conversely, since `requiredStatement` values must be displayed or easily displayable to the user, URIs in this property should use target entities' human-readable URIs. For Creative Commons licenses or RightsStatements.org statements, URIs for human-readable content use HTTPS.

## Restrictions

None known.

## Example

{% include manifest_links.html viewers="UV, Mirador, Annona" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="15-27"' %}

# Related recipes

* [Simplest Manifest - Single Image File][0001]
* [Embedding HTML][0007] (Nearly identical manifest, but focusing on a different part of the spec.)

{% include acronyms.md %}
{% include links.md %}

