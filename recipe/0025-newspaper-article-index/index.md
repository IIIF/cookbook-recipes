---
title: Newspaper Article Index
id: 25
layout: recipe
tags: [text, image, newspaper]
summary: "Using Ranges to build a navigable index for newspaper articles spanning multiple non-consecutive pages"
viewers:
topic: structure
property: structures
---

## Use Cases

Newspaper articles can span multiple non-consecutive pages and typically occupy specific column regions within those pages. You want to guide the reader through this fragmented content with a structural index that establishes the logical reading sequence.


## Implementation Notes

Ranges are used to represent the logical structure within an object, by grouping or reordering Canvases relative to their default sequence in the `items` property of the Manifest, forming a hierarchical tree structure. A Range can contain Canvases, parts of Canvases, or nested Ranges to introduce hierarchy among them. The top-level Range represents the broader index, while nested Ranges represent individual logical units, such as individual newspaper articles.

Every entry in the `items` property of a Range must be a JSON object and have both `id` and `type` properties. Viewers should only present Ranges to the user if they have a label and do not have a `behavior` value of `no-nav`. All Canvases or parts of Canvases that belong to a Range must be included within its `items` property or within the `items` of a descendant Range.

A Range can handle complex layouts where text occupies only part of a page or spans multiple, non-consecutive pages:

- Parts of Canvases can represent portions of text, such as article columns. They may be targeted using a Specific Resource with a Selector, as defined in the [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/#fragment-selector), which recommends using the FragmentSelector class for this purpose.

- Canvases and parts of Canvases do not need to be contiguous or in the same order as in the Manifest’s `items` property, but they can appear in any order required by the logical structure. This can support an article that starts on the front page and continues on page four.

To associate supplementary content such as OCR transcriptions, Ranges may link to an Annotation Collection using the `supplementary` property. The referenced collection contains annotations targeting specific Canvas areas within the Range and linking content resources to those targeted regions. More on Annotation Collections [here](https://iiif.io/api/presentation/3.0/#58-annotation-collection).


## Restrictions

None


## Example

In the following example, the “Tagesneuigkeiten” (Today’s News) section of the newspaper spans two non-consecutive pages. The section begins with two partial columns on page 2, is then interrupted by other content, and continues with two full columns on page 5.

We define a top-level Range that serves as the structural index for the entire newspaper issue, with each nested Range containing an article. The Range dedicated to the “Tagesneuigkeiten” contains four partial Canvases in their intended reading sequence, each targeting a specific column region using a FragmentSelector. When the user selects an article from the index, the viewer should display the first region of the article and allow the user to move through the reading sequence defined in the Range's `items` property. There is no predetermined display behavior for partial Canvases: the viewer may crop the Canvas or highlight the region of interest to direct the user.

Each article Range is linked to an Annotation Collection that contains the OCR transcription of each article.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="334-440"' %}


## Related Recipes

* [Basic Newspaper][0068]
* [Table of Contents for Book Chapters][0024]

{% include acronyms.md %}
{% include links.md %}
