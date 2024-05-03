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

You have an image that you want to annotate for viewing by a global or other polylingual audience. So that as many of your intended audience as possible and practical are able to understand the annotations on your artifact, you want to present each annotation in some or all of their languages.

## Implementation Notes

To include language variation within any single annotation, combine the Choice structure, explained more fully in [Multiple Choice of Images][0033] and [Multiple Choice of Audio Formats][0434] with the appropriate annotation structure, for example the simple version shown in [Simple Annotation — Tagging][0021]. This recipe introduces one practical real-world situation for doing that.

The `body` of an Annotation uses the Choice structure, with each of its items differing only in the `language` and `value` properties. Note that an annotation's `value` and `language` in a Choice are represented as separate properties, unlike Manifest properties that use language maps.

Somewhat as with the [Multiple Choice of Audio Formats][0434] recipe, the nature of the choice in this recipe is shared among the manifest creator, the visitor, and the client. The manifest creator defines the preferred order of languages, the visitor's browser sends to the client its preferred language, and the client negotiates the interaction of the preceding to provide an interface to the visitor. (It is expected that any client will be capable of displaying the entire Unicode set, obviating client-based reasons to conceal any annotation language version.)

For the user interface to the multiple language versions of an annotation, a client is expected to provide a visitor with a clear way to know there are equivalent annotations in multiple languages, with identifying information about which languages are in use, and with a way to switch between languages at will.

## Restrictions

None known.

## Example

In this example, the image is from one of a pair of six-fold screens depicting four noble accomplishments in Azuchi-Momoyama period Japan (16th/17th century CE). At its [original online home](https://emuseum.nich.go.jp/detail?langId=en&webView=&content_base_id=100320&content_part_id=0&content_pict_id=0), the e-Museum of the National Institutes for Cultural Heritage in Japan, item text exists in four languages. To simplify things here, only Japanese and English are used.

There's one annotation, which focuses on the koto of the item's title, albeit enclosed in a cover and thus implied rather than shown. The text of the annotation takes that implication into account and describes this portion of the screen as representing a koto wrapped in a cloth.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Multiple Choice of Images in a Single View (Canvas)][0033] to see the Choice structure in an image context
* [Multiple Choice of Audio Formats in a Single View (Canvas)][0033] to see the Choice structure in an A/V context
* [Simple Annotation — Tagging][0021] for an Annotation using the tagging `motivation`
* [Displaying Multiple Values with Language Maps][0118] to see a different way of casting a property value to a language.

{% include acronyms.md %}
{% include links.md %}
