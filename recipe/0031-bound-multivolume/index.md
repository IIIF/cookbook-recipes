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

Ranges are used to represent a structure within a resource by grouping Canvases together. Ranges can include Canvases, parts of Canvases, or other Ranges, creating a tree structure which, in this use case, delineates the individual volumes bound within the material object.

Ranges are contained within the `structures` property and require a `label` property to display in the viewing client's index (`labels` are not inherited from a referenced Canvas, so you will need to explicitly include the `label` property in the Range). Within a Range, resources are included as an array of resources using the `items` property. These structures can be made hierarchical simply by nesting an `items` array within another `items` array. This is useful for further subdividing the volumes into chapters.

The `behavior` property can also be applied to Ranges. For more information on how `behavior` affects navigation in Ranges, see the [IIIF Presentation API on Ranges](https://iiif.io/api/presentation/3.0/#54-range) and the [Ranges and the `behavior` Property][229] recipe.

## Restrictions

??

## Example

In this example, the seven volumes of *Gottesdienstliche Ceremonien, Oder H. Kirchen-Gebräuche Und Religions-Pflichten Der Christen* have been bound into a single physical volume. The Manifest contains a Range to represent the top-level structure (the physical volume) and additional embedded Ranges to represent each of the discrete textual volumes. This will produce an index of the constituent volumes like so:

* ...
* ...
* ...

The example is a truncated version of [*Gottesdienstliche Ceremonien, Oder H. Kirchen-Gebräuche Und Religions-Pflichten Der Christen*][https://digital.library.ucla.edu/catalog/ark:/21198/zz001hd85r] and includes only the first three volumes for brevity.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Book with Table of Contents][0024]
* [Multi-volume Work with Individually-bound Volumes][0030]
* [Paged Collections][0032]

{% include acronyms.md %}
{% include links.md %}
