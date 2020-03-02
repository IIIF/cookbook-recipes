---
title: Rights statement
id: 8
layout: recipe
tags: [text, presentation]
summary: "You want to assert a license or rights statement that applies to the content of the resource, such as the JSON of a Manifest or the pixels of an image."
---

## Use Case

Why is this pattern is important?
This pattern shows you how to implement the inclusion of a license or rights statement by using the `rights`, `requiredStatement`, and `metadata` properties.

Comparisons
+ Rendering
	+ Clients must render `requiredStatement` content on every resource type, but `rights` content may or may not be rendered. (`metadata` variant?)
	+ Even though clients must render `requiredStatement`, it may be hidden at first
+ Applicability
	+ Any resource type may have `rights` or `requiredStatement` (`metadata`?)
+ Content
	+ `rights` value "must be drawn from the set of Creative Commons license URIs, the RightsStatements.org rights statement URIs, or those added via the extension mechanism"
	+ `requiredStatement` can be any content
+ Format
	+ `rights` value is a string
	+ `requiredStatement` and `metadata` are formatted similarly, as JSON objects; however, `requiredStatement` is a single object where `metadata` is an array of JSON objects


```
rights

A string that identifies a license or rights statement that applies to the content of the resource, such as the JSON of a Manifest or the pixels of an image. The value must be drawn from the set of Creative Commons license URIs, the RightsStatements.org rights statement URIs, or those added via the extension mechanism. The inclusion of this property is informative, and for example could be used to display an icon representing the rights assertions.

If displaying rights information directly to the user is the desired interaction, or a publisher-defined label is needed, then it is recommended to include the information using the requiredStatement property or in the metadata property.

The value must be a string. If the value is drawn from Creative Commons or RightsStatements.org, then the string must be a URI defined by that specification.

    Any resource type may have the rights property.
    Clients may render rights on any resource type.
```

```
requiredStatement

Text that must be displayed when the resource is displayed or used. For example, the requiredStatement property could be used to present copyright or ownership statements, an acknowledgement of the owning and/or publishing institution, or any other text that the publishing organization deems critical to display to the user. Given the wide variation of potential client user interfaces, it will not always be possible to display this statement to the user in the client’s initial state. If initially hidden, clients must make the method of revealing it as obvious as possible.

The value of the property must be a JSON object, that has the label and value properties, in the same way as a metadata property entry. The values of both label and value must be JSON objects, as described in the languages section.

    Any resource type may have the requiredStatement property.
    Clients must render requiredStatement on every resource type.
```

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

