---
title: Multiple Volumes in a Single Bound Volume
id: 31
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
- UV
- Mirador
topic:
 - structure
---

## Use Case

This recipe should be considered alongside [Book with Table of Contents][0024] and [Multi-volume Work with Individually-bound Volumes][0030]. Each use case, including this one, involves modeling the resource to reflect the structure of both the object and the text within to generate the most appropriate viewing experience for a user.

This recipe considers the use case of a multi-volume object where the volumes are bound together in a single volume. Take for example a Sammelband where separately printed fascicles of a printed work or discrete codicological units comprising a composite manuscript were subsequently bound together. Another example might be a single work published in multiple volumes that is later distributed as a single bound volume.

In both cases, we have a single material object comprising two or more discrete textual objects, which suggests using a single Manifest to represent the resource and using Ranges to delineate the distinct textual objects.

Compare this with the [Multi-volume Work with Individually-bound Volumes][0030] example where individual Manifests for each volume are collocated using a single IIIF Collection to represent the work as a whole.

## Implementation Notes

What do you need to know to use this pattern?
How do you implement the pattern?

## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.?

Delete this section if it is not needed.
If you don't know what the restrictions might be initially, just leave the following line:
**Unknown - Help Needed**

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Book with Table of Contents][0024]
* [Multi-volume Work with Individually-bound Volumes][0030]
* [Paged Collections][0032]

{% include acronyms.md %}
{% include links.md %}
