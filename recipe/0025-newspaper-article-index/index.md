---
title: Navigation by Newspaper Article
id: 25
layout: recipe
tags: [text, image, newspaper]
summary: "Using Ranges to build a navigable index for newspaper articles spanning multiple non-consecutive pages"
viewers:
- Theseus
topic: structure
property: structures
---

## Use Case

Newspaper articles can span multiple non-consecutive pages and typically occupy specific column regions within those pages. You want to guide the reader through this fragmented content with a structural index that establishes the logical reading sequence.


## Implementation Notes

Ranges are used to represent the logical structure within an object, by grouping or reordering Canvases relative to their default sequence in the `items` property of the Manifest, forming a hierarchical tree structure. A Range can contain Canvases, parts of Canvases, or nested Ranges to introduce hierarchy among them. The top-level Range represents the broader index, while nested Ranges represent individual logical units, such as individual newspaper articles. These ranges inform the viewer that the resources are intended to be consumed in a particular order. Viewers should only present Ranges to the user if they have a label and do not have a `behavior` value of `no-nav`. All Canvases or parts of Canvases that belong to a Range must be included within its `items` property or within the `items` of a descendant Range.

A Range can handle complex layouts where text occupies only part of a page or spans multiple, non-consecutive pages:

- Parts of Canvases can represent portions of text, such as article columns. They may be targeted using a SpecificResource with a Selector, as defined in the [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/#fragment-selector). The IIIF Presentation API 3.0 ([§5.3](https://iiif.io/api/presentation/3.0/#53-canvas)) recommends using the `FragmentSelector` class, as it allows refinement by other Selectors and is consistent with use cases that cannot be represented directly using a URI fragment. `FragmentSelector` is also preferred over the `ImageApiSelector` because it targets the Canvas rather than a specific image. Since a Canvas may be composed of multiple images, a Canvas-level selector ensures that article boundaries remain valid regardless of the Canvas composition.

- Canvases and parts of Canvases do not need to be contiguous or in the same order as in the Manifest’s `items` property, but they can appear in any order required by the logical structure. This can support an article that starts on the front page and continues on page four.

To associate supplementary content such as OCR transcriptions, Ranges may link to an Annotation Collection using the `supplementary` property. The referenced collection contains annotations targeting specific Canvas areas within the Range and linking content resources to those targeted regions. For more information on Annotation Collections, see the [Grouping Annotations into Collections](https://iiif.io/api/cookbook/recipe/0309-annotation-collection/) recipe.


## Restrictions

None


## Example

In the following example, the “Tagesneuigkeiten” (Today’s News) section of the newspaper spans two non-consecutive pages. The section begins with two partial columns on page 2, is then interrupted by other content, and continues with two full columns on page 5.

We define a top-level Range that serves as the structural index for the entire newspaper issue, with each nested Range containing an article. The Range dedicated to the “Tagesneuigkeiten” contains four partial Canvases in their intended reading sequence, each targeting a specific column region using a `FragmentSelector`. For demonstration purposes, a second Range is given for “Das Turnier”, the article occupying most of page 3. When the user selects an article from the index, the viewer should display the first region of the article and allow the user to move through the reading sequence defined in the Range's `items` property.

{% include manifest_links.html viewers="Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="207-318"' %}

## Related Recipes

* [Basic Newspaper][0068]
* [Table of Contents for Book Chapters][0024]
* [Grouping Annotations into Collections][0309]

{% include acronyms.md %}
{% include links.md %}
