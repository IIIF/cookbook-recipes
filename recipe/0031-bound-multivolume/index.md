---
title: Multiple Volumes in a Single Bound Volume
id: 31
layout: recipe
tags: [sammelband, multi-volume]
summary: "Recipe for a multi-volume object where the volumes are bound together in a single codex."
viewers:
- UV
- Mirador
topic:
 - structure
---

## Use Case

This recipe should be considered alongside [Book with Table of Contents][0024] and [Multi-volume Work with Individually-bound Volumes][0030]. Each use case, including this one, involves modeling the resource to reflect the structure of both the object and the text within to generate the most appropriate viewing experience for a user.

This recipe considers the use case of a multi-volume object where the volumes were bound together in a single codex subsequent to their issue. Another use case might be a [Sammelband](https://folgerpedia.folger.edu/Sammelbands) where independently printed fascicles of separate works were later bound together or where discrete manuscript codicological units were combined subsequent to their creation resulting in a composite manuscript.

In both cases, we have a single material object comprising two or more discrete textual objects, which suggests using a single Manifest to represent the resource and using Ranges to delineate the distinct textual objects.

Compare this with the [Multi-volume Work with Individually-bound Volumes][0030] example where individual Manifests for each volume are collocated using a single IIIF Collection to represent the work as a whole.

## Implementation Notes

Ranges are used to represent organizational structure within a resource by grouping Canvases together. Ranges can include Canvases, parts of Canvases, or other Ranges, creating a tree structure which, in this use case, delineates the individual volumes bound within the material object.

Ranges are contained within the `structures` property and require a `label` property to display in the viewing client's index (`labels` are not inherited from a referenced Canvas, so you will need to explicitly include the `label` property in the Range). Within a Range, resources are included as an array of resources using the `items` property. These structures can be made hierarchical simply by nesting an `items` array within another `items` array. This is useful for further subdividing the volumes into chapters. As well, each `items` array can take metadata elements in addition to `label` to further describe each volume, for example to add authors, origin dates, etc. For more information on descriptive metadata in Manifests, see the [Metadata on any Resource][0029] recipe.

The `behavior` property can also be applied to Ranges. For more information on how `behavior` affects navigation in Ranges, see the [IIIF Presentation API on Ranges](https://iiif.io/api/presentation/3.0/#54-range) and the [Ranges and the `behavior` Property][0229] recipe.

## Example

This example uses the seven volumes of [*Gottesdienstliche Ceremonien, Oder H. Kirchen-Gebräuche Und Religions-Pflichten Der Christen*](https://digital.library.ucla.edu/catalog/ark:/21198/zz001hd85r) which have been bound into a single physical volume (truncated to only a few pages of each of the first 2 volumes here for brevity). The Manifest contains a Range to represent the top-level structure (the physical codex) and additional embedded Ranges to represent each of the discrete textual volumes as well as the front matter.
```
{
    "structures": [
{
      "id": "…range/r0", // “Gottesdienstliche Ceremonien…”
      "type": "Range",
      "items": [
        { // “Front Matter”
              "id": "…range/r1",
              "type": "Range",
              "items": [ {"…canvas/p1"}, {"…canvas/p2"} ]
        },
        { // “Erste Ausgabe…”
              "id": "…range/r2",
              "type": "Range",
              "items”: [ {"…canvas/p3"}, {"…canvas/p4”} ]
        },
        { // “Zweyte Ausgabe…”
              "id": "…range/r3",
              "type": "Range",
              "Items": [ {"…canvas/p5"}, {"…canvas/p6"} ]
        },
```

This will produce an index of the constituent volumes like so:

* Front Matter
* Erste Ausgabe... (Vol. 1)
* Zweyte Ausgabe... (Vol. 2)

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="246-315"'%}

## Related Recipes

* [Book with Table of Contents][0024]
* [Multi-volume Work with Individually-bound Volumes][0030]
* [Paged Collections][0032]

{% include acronyms.md %}
{% include links.md %}
