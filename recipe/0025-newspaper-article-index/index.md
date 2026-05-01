---
title: Newspaper Article Index
id: 25
layout: recipe
tags: [text, image, newspaper]
summary: "Using Ranges to create an index to navigate complex documents"
viewers:
topic: structure
property: structures
---

## Use Cases

You have a complex document with text scattered across multiple Canvas regions:

- Newspaper articles can span multiple, non-consecutive pages and typically occupy specific portions of these pages.

- You have digitized an unbound book by photographing flat bifolios. Each image captures two non-consecutive pages side by side, such as pages 1 and 16. To read the text in its proper logical order, the reader must view the same image twice at different points of the reading sequence, each time focusing on a specific region of the Canvas.

You need to guide the reader through the fragmented text by providing a structural index that establishes the logical reading sequence.


## Implementation Notes

Ranges are used to represent the logical structure within an object, by grouping or ordering Canvases beyond their default order in the `items` property of the Manifest, creating a tree structure. A Range can contain Canvases, parts of Canvases, or nested Ranges to introduce hierarchy among them. The top-level Range represents the broader index, while nested Ranges represent individual logical units, such as individual newspaper articles.

Every entry in the `items` property of a Range must be a JSON object and have both id and type properties. Viewers should only present Ranges to the user if they have a label and do not have a `behavior` value `no-nav`. All Canvases or parts of Canvases that belong to a Range must be included within its `items` property or within the `items` of a descendant Range.

A Range can handle complex layouts where text occupies only part of a page or spans multiple, non-consecutive pages:

- Parts of Canvases can represent portions of text, such as article columns. They may be targeted using a Specific Resource with a Selector, as defined in the Web Annotation data model, which recommends using the FragmentSelector class for this purpose.

- Canvases and parts of Canvases do not need to be contiguous or in the same order as in the Manifest’s `items` property, but they can appear in any order required by the logical structure. This can support an article that starts on the front page and continues on page four.

Ranges may link to an Annotation Collection using the supplementary property. The referenced collection contains annotations targeting specific Canvas areas within the Range and linking content resources to those Canvases, such as OCR text.


## Restrictions

None


## Example

In the following example, the “Tagesneugkeiten” (Today’s News) section of the newspaper spans 2 non-consecutive pages. The section begins with two partial columns on page 2, is then interrupted by other content, and concludes with two full columns on page 5.

We define a top-level Range that acts as the structural index for the entire newspaper issue, with each nested Range containing a section/article. The Range dedicated to the “Tagesneugkeiten” section contains four partial Canvases in their intended reading sequence, each targeting a specific column region using a FragmentSelector.

When the user selects an article from the index, the viewer must display the corresponding page and follow the reading sequence defined in the `items` property of the Range. There is no predetermined display behavior for partial Canvases: the viewer may crop the Canvas or highlight the region of interest to direct the user.


{% include manifest_links.html viewers="UV, Mirador, Glycerine Viewer, Theseus, TIFY" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="324-414"' %}

## Related Recipes

* [Basic Newspaper][0068]
* [Table of Contents for Book Chapters][0024]

{% include acronyms.md %}
{% include links.md %}
