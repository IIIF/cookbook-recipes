---
title: Book (behavior variations)
id: 11
layout: recipe
tags: image, text, layout
summary: "A sample manifest for informing a client how the canvases should be displayed to the viewer in order to read the contents authentically in accordance with how the resources relate to one another and should function related to their layout."
---

## Use Case

I have objects that have the concept of recto and verso; are paged. I have objects that have no such concept. I have objects that are photographed in different ways (one image per page, oneimage per pair of open pages, etc).

The `behavior` property tells a presentation client one part of how to display a sequence of resources to a viewer.

... inform a client of the appropriate presentation configuration and navigational cues for a variety of resource relationships. Some examples include book view layout for books imaged with one image per page, or if imaged with one image per 2-page spread, or images that can be stitched together in the viewer for a continuous view, such as a scroll imaged in multiple shots, or individual items such as inserts, foldouts, etc.

## Implementation notes

The property is permissible for all resource types, but some values (`unordered`, `individuals`, `continuous`, `paged`) are permissible only for `Collection`, `Manifest`, and `Range`, while others (`facing-pages`, `non-paged`) are permissible only on `Canvas`. Clients should process the property on any resource type.

The default `behavior` value, if not specified, is `individuals` for Layout Behaviors (as opposed to Temporal, Collection, Range, and Miscellaneous Behaviors).

In addition to `behavior`, you may want to use the `viewingDirection` property (see also [Book (paging variations)][0010] recipe), for example `right-to-left` or `top-to-bottom`, depending on the expected user experience for viewing your resource(s) or the specificities of the physical object and its digital surrogate. Interactions between `viewingDirection` and `behavior`, especially when they are set on multiple and/or hierarchical resources, need special attention. You are recommended to read [the Presentation 3.0 spec on `behavior`](https://iiif.io/api/presentation/3.0/#behavior) carefully and to keep current with future releases.


## Restrictions

None known

## Example 1: `behavior` `paged`

This manifest shows the playbill for "Akiba gongen kaisen-banashi," "Futatsu chōchō kuruwa nikki", and "Godairiki koi no fūjime", kabuki performances at the Chikugo Theater in Osaka from the fifth month of Kaei 2 (May, 1849).

[JSON-LD](manifest-rtl.json)
[View in Universal Viewer](https://universalviewer.io/examples/#?manifest={{ site.url }}{{ site.baseurl }}{{ page.url }}manifest-rtl.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-line="15" data-src="manifest-rtl.json" }
```json
```

## Example 2: `behavior` `continuous`

This manifest represents an Ethiopian scroll, written in Gez for Walata Eyasus (secular name Berenash), that contains prayers to guard against epilepsy and for the binding of demons. Its full length is 2.245m and is roughly .11m wide over its length.

Note that as of the writing of this recipe, the `behavior` value of `continuous` has no noticeable effect in the Universal Viewer demonstration linked below. However, for forward compatibility it is a part of the manifest.

[JSON-LD](manifest-ttb.json)
[View in Universal Viewer](https://universalviewer.io/examples/#?manifest={{ site.url }}{{ site.baseurl }}{{ page.url }}manifest-ttb.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-line="15-18" data-src="manifest-ttb.json" }
```json
```
## Example 3: `behavior` `individuals`

This manifest represents an Ethiopian scroll, written in Gez for Walata Eyasus (secular name Berenash), that contains prayers to guard against epilepsy and for the binding of demons. Its full length is 2.245m and is roughly .11m wide over its length.

Note that as of the writing of this recipe, the `behavior` value of `continuous` has no noticeable effect in the Universal Viewer demonstration linked below. However, for forward compatibility it is a part of the manifest.

[JSON-LD](manifest-ttb.json)
[View in Universal Viewer](https://universalviewer.io/examples/#?manifest={{ site.url }}{{ site.baseurl }}{{ page.url }}manifest-ttb.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-line="15-18" data-src="manifest-ttb.json" }
```json
```

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.

* [Book (simplest)][0009]
* [Book (paging variations)][0011]
* [Thumbnails][0012]
* [Table of contents (ranges) - book chapters][0024]

{% include acronyms.md %}
{% include links.md %}
