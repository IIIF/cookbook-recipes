---
title: Annotating in Multiple Languages
id: 346
layout: recipe
tags: annotation
summary: "tbc"
viewers:
 - Annona
topic: 
 - annotation
---

## Use Case

You would like to make text annotations in multiple language translations on an image. Because the annotations are semantically equivalent, the expectation is that the user or client would choose which translation to display for the annotation.

## Implementation Notes

To include language variation within any single annotation, combine the Choice structure, explained more fully in [Multiple Choice of Images][0033] and [Multiple Choice of Audio Formats][0434] with the appropriate annotation structure, for example the simple version shown in [Simple Annotation — Tagging][0021].

When there are multiple equivalent annotations from which a user or client should select one, we use the Choice structure. While much of the IIIF specification uses language maps to distinguish between languages, Annotations use a language property with a value. Clients may process this mechanisim for multiple languages differently to language maps and the web annotation specification gives the following guidance:

> "Clients MAY use any algorithm to determine which resource to choose, and SHOULD make use of the information present to do so automatically, but MAY present a list and require the user to make the decision." *— from [Choice Between Bodies](https://www.w3.org/TR/annotation-model/#choice-between-bodies)*

The `body` of an Annotation uses the Choice structure, with each of its items differing only in the `language` and `value` properties. Note that an annotation's `value` and `language` in a Choice are represented as separate properties, unlike Manifest properties that use language maps.

Somewhat as with the [Multiple Choice of Audio Formats][0434] recipe, the nature of the choice in this recipe is shared among the manifest creator, the visitor, and the client. The manifest creator defines the preferred order of languages by the top-to-bottom order of each `item` in the Choice structure. The visitor uses a client's interface elements to know what manifest data is available in multiple languages and which languages, as well as to make an active choice of which to display. A client may be programmed to take actions based on the W3C Web Annotation Data Model section on "Choice Between Bodies" cited above. If the client chooses to display a choice, the [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) says it should only display one. By the same token, user experience with a client will be improved if a client indicates different language versions of an annotation even if it shows only one initially.

## Restrictions

None known.

## Example

In this example, the image is from one of a pair of six-fold screens depicting four noble accomplishments in Azuchi-Momoyama period Japan (16th/17th century CE). At its [original online home](https://emuseum.nich.go.jp/detail?langId=en&webView=&content_base_id=100320&content_part_id=0&content_pict_id=0) item text exists in four languages. To simplify things here, only Japanese and English are used.

There's one annotation, which focuses on the koto of the item's title (albeit enclosed in a cover and thus implied rather than shown). The text of the annotation takes that implication into account and describes this portion of the screen as representing a koto wrapped in a cloth.

Terms of use for this image from the e-Museum of the National Institutes for Cultural Heritage in Japan / e国宝に 独立行政法人国立文化財機構 can be found in <a href="https://emuseum.nich.go.jp/about?langId=ja">Japanese</a>, <a href="https://emuseum.nich.go.jp/about?langId=en">English</a>, <a href="https://emuseum.nich.go.jp/about?langId=zh">Chinese</a>, and <a href="https://emuseum.nich.go.jp/about?langId=ko">Korean</a>.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="58-72"' %}

## Related Recipes

* [Multiple Choice of Images in a Single View (Canvas)][0033] to see the Choice structure in an image context
* [Multiple Choice of Audio Formats in a Single View (Canvas)][0033] to see the Choice structure in an A/V context
* [Simple Annotation — Tagging][0021] for an Annotation using the tagging `motivation`
* [Displaying Multiple Values with Language Maps][0118] to see a different way of casting a property value to a language.

{% include acronyms.md %}
{% include links.md %}
