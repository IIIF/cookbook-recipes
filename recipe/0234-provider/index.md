---
title: Acknowledge Content Contributors
id: 234
layout: recipe
tags: provider
summary: "Include a rich set of information for each content contributor so clients can make this information visible."
viewers:
 - id: Mirador
   support: partial
 - Glycerine Viewer
 - Theseus
topic: property
property: provider
---

## Use Case

You have a IIIF resource for which you would like to include information about one or more organizations or people that contributed to providing the content of the resource. You want to include a rich set of information for each contributor so clients can make visible this information in a similarly robust way. The [`provider`](https://iiif.io/api/presentation/3.0/#provider) property allows you an extensible way to acknowledge contributions with as little as a `label` and as much as a `label`, `homepage`, a `logo`, and a `seeAlso` machine-readable description for the contributor.

## Implementation Notes

So that a client can display one or more content contributors for a resource, the `provider` property conveys information in the form of an [Agent](http://purl.org/dc/terms/Agent) resource. This resource must contain, at a minimum:
+ `id`, an authoritative and unique URI for the contributor,
+ `type`, always the string "Agent", and
+ `label`, a human-readable name for the contributor.

In addition, `provider` is structured data, can contain multiple Agents, and can contain information about assets other than plain text, distinguishing it from [`requiredStatement`](https://iiif.io/api/presentation/3.0/#requiredstatement).

To make the information more usable and interconnected for a reader, `provider` as an Agent is strongly recommended to have both [`homepage`](https://iiif.io/api/presentation/3.0/#homepage) and [`logo`](https://iiif.io/api/presentation/3.0/#logo) properties. These will allow a reader to go to the contributor's website and find more. Note that the `id` for the Agent may, but does not have to be, the same as the `id` for the `homepage`.

## Restrictions

None known.

## Example

In this example, we reuse the front page of a kabuki playbill that was contributed to the IIIF Cookbook by UCLA Library Digital Collections. The `id` for them as an Agent is the US Library of Congress authority ID for the UCLA Library, the `homepage` is their actual homepage, the `logo` is also for the library as a whole, and the `seeAlso` is the US Library of Congress MADS/XML. In your use of this property, you might want to and be able to unify the information in the property differently.

Only Mirador implements `provider`, and only partially. The property must be on the Manifest level, Mirador will only display the text from a `label` and the image from a  `logo` under `provider`, and the information will only be found in the list of manifests.

{% include manifest_links.html viewers="Mirador, Glycerine Viewer, Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="15-82"' %}

## Related Recipes

* [Linking to Web Page of an Object][0047] for demonstrating the use of `homepage` at the Manifest level
* [Add Identifying Graphic][0217] for demonstrating the use of `logo`
* [Linking to Structured Metadata][0053] for demonstrating the use of `seeAlso`
* [Rights][0008] for demonstrating use of `requiredStatement`

{% include acronyms.md %}
{% include links.md %}
