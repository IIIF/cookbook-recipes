---
title: Linking to Structured Metadata Through seeAlso
id: 53
layout: recipe
tags: [metadata,presentation]
summary: "tbc"
---

## Use Case

You have a IIIF format resource for which you would like to offer researchers the opportunity to download a PDF version. You know from previous experience that researchers using your collection like to have images and texts available for offline reading, or you know you have patrons with bandwidth concerns who need to minimize their time online, or other reasons such as wanting to provide transcriptions and translations of objects' text. Through use of the `rendering` property, you are able to alert conforming clients to the presence of this other format (or yet other formats, such as ePub) so they in turn can provide appropriate UX workflows to users.

## Implementation Notes

This property is used for pointing a viewer to a non-IIIF resource with information about IIIF resource to which it is attached. Most frequently, the non-IIIF resource will be structured metadata, and to be most effective, the target resource should be machine-readable.

Three other properties may seem similar, so it's worth highlighting the differences. 

### homepage
Where `rendering` presents an additional representation of the same resource, [`homepage`](https://iiif.io/api/presentation/3.0/#homepage) points to a webpage _about_ the object represented by the resource.

### accompanyingCanvas
An `accompanyingCanvas` resource is a IIIF resource presented simultaneously with the main resource, where a target of `rendering` is not IIIF-compatible and must be viewed outside the main resource's viewer. In addition, `accompanyingCanvas` is used for content complementary to the main resource while `rendering` points to additional representations of the same resource.

### rendering
Unlike `seeAlso`, the `rendering` property provides the URI of an alternate representation of the current resource, such as in PDF or ePub format.

Any resource may have the `seeAlso` property. Each instance of it may have multiple items contained inside it, provided each has the `id` and `type` properties; `label`, `format`, and `profile` are strongly recommended properties. Conforming clients may process this property in some way, but the outcomes of a client's processing has no defined form.

## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.? 

Delete this section if it is not needed.
If you don't know what the restrictions might be initially, just leave the following line:
**Unknown - Help Needed**

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="UV, Mirador, Tify, Curation" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

