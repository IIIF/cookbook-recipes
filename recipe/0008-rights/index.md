---
title: Rights statement
id: 8
layout: recipe
tags: [text, presentation]
summary: "You want to assert a license or rights statement that applies to the content of the resource, such as the JSON of a Manifest or the pixels of an image."
---

## Use Case

You are able to implement the inclusion of a license, rights, or other important statement about a resource by using the `rights`, `requiredStatement`, and `metadata` properties. This recipe will focus on the first two; see [the Presentation 3.0 spec on `metadata`](https://iiif.io/api/presentation/3.0/#metadata) for more information about that property.

While you can use either `rights` and `requiredStatement` for the semantic value of asserting important information (reproduction rights, ownership, collection name), the properties do have material differences. These are the most salient:
+ Content: The `rights` value must be a CreativeCommons license URI, a RightsStatements.org URL, or added through the extension process. The `requiredStatement` value, on the other hand can be any content, such as a copyright or institutional URI or text.
+ Rendering: Clients must render `requiredStatement` content on every resource type (even if hidden at first), but `rights` content may or may not be rendered visibly.
+ Property Value: The `rights` property value must be a string, where the `requiredStatement` value must be a single JSON object with `label` and `value` properties and `metadata` values must be an array of JSON objects, where each object has the `label` and `value` properties.
+ Resource Applicability: Any resource type may have `rights` or `requiredStatement`. However, `rights` is only for license or rights to the content, including the non-visible content, while `requiredStatement` can be any text the publishing organization deems critical to display to the user.

If user visibility of the information or a publisher-defined label is paramount, use `requiredStatement` or `metadata`. Resources may include all three properties.

## Implementation notes

How does one implement the pattern?

*Draw lessons from [GitHub discussion of HTTP v HTTPS	](https://github.com/IIIF/api/issues/1874) and put them in here*

## Restrictions

None known.

## Example

[JSON-LD](manifest.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-line="15-27" data-src="manifest.json" }
```json
```

# Related recipes

* [Simplest Manifest - Single Image File][0001]
* [Embedding HTML][0007] (Nearly identical manifest, but focusing on a different part of the spec.)

{% include acronyms.md %}
{% include links.md %}

