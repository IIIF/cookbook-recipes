---
title: CSS in an Annotation
id: 45
layout: recipe
tags: [style]
summary: "Using an external CSS stylesheet in an annotation body, annotations can be styled in limited ways"
viewers:
 - Theseus
topic:
 - basic
code:
 - iiif-prezi3
---

## Use Case

You have two different authors who have each made an annotation on a visual resource. You'd like to distinguish the authors visually in the presentation, putting each annotation text in a different text color.

## Implementation Notes

Using CSS in annotations is covered in the W3C Web Annotation Data Model. For a look at its approach to styles in Web Annotations, see [the W3C Web Annotation Data Model's Styles section](https://www.w3.org/TR/annotation-model/#styles). Note in particular changes needed to the `target` property if styling is intended for a IIIF Canvas.

Annotations can be styled using CSS in three ways. This recipe focuses on using an external stylesheet. To add CSS using an external stylesheet, insert the stylesheet's URI as the the value of a `stylesheet` property on the Annotation. The `styleClass` property can then be used to reference rules in that external stylesheet, such as in the annotation `body` or composite `target` containing a `source` as well. It is advisable to set appropriate CORS headers for the stylesheet to improve its chances of working in generic viewers.

Viewer behavior and the specifics of an annotation's `target` will have effects, but broadly speaking, using CSS to style the `body` of an annotation will style the content of the annotation and a CSS class in the `target` will style the annotation's highlight on a Canvas.

The two other methods for adding CSS to a manifest are inline CSS and an inline stylesheet. To see how to use an inline stylesheet, see [Image Rotation Two Ways][0040]. To see how to use inline CSS, see [Visible Text Resource on a Canvas][0561]. Each of these also shows styling a IIIF resource in an annotation with a `motivation` of `painting` — that is, styling content that can be expected to be visible in the content space of a viewer.

## Restrictions

See the Restrictions section of the [HTML in Annotations][0019] recipe for a brief discussion of limitations to markup in annotations. These limitations can affect, in turn, the possible selectors in your external stylesheet.

The CSS approach depends wholly on viewer implementation of CSS as applied to a resource. Viewers have no requirement to support CSS styling. Browser-based viewers may defer CSS implementation in whole or in part to the browser. Consequently, and also for reasons of accessibility, annotations should not rely on styling for semantics and should be readable by a human or machine without styling.

One example: Since IIIF Canvas dimensions are unit-less, using pixels for text size is valid but may be interpreted variably across viewers or other clients.

## Example

This recipe focuses on annotations with motivations other than painting and on an external CSS stylesheet. The Theseus viewer is included here for its support of styling the annotation text, but it does not currently support styling the `target`.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="56,60,71,78,82,93"' %}

### Stylesheet
{% include jsonviewer.html src="style.css" %}

## Related Recipes

* [Image Rotation Two Ways][0040], for an inline CSS stylesheet used with a IIIF resource
* [HTML in Annotations][0019], a complementary recipe for markup, including a fuller discussion of markup use cautions
* [Visible Text Resource on a Canvas][0561], for inline CSS used with a painted textual resource

{% include acronyms.md %}
{% include links.md %}


