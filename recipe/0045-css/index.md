---
title: CSS in an Annotation Body
id: 45
layout: recipe
tags: [style]
summary: "Using an external CSS stylesheet in an annotation body, annotations can be styled in limited ways"
viewers:
topic:
 - basic
code:
 - iiif-prezi3
---

## Use Case

Two different authors have each made an annotation on a visual resource. To distinguish their authors, each will be in a different text color.

## Implementation Notes

Using CSS to alter resource presentation styles is not specified in the [IIIF Presentation 3.0 API](https://iiif.io/api/presentation/3.0/) except insofar as the Presentation API incorporates types from the W3C Web Annotation Data Model. For a more detailed look at the model's approach to styles in Web Annotations, see [the W3C Web Annotation Data Model's Styles section](https://www.w3.org/TR/annotation-model/#styles).

CSS can be added in 3 ways: inline, with an inline stylesheet, or with an external stylesheet. Inline styles are written conventionally, using markup elements as content containers or style delimiters. See [HTML in Annotations][0019] for a brief discussion of limitations to markup in annotations. Inline stylesheets and external stylesheets are incorporated in similar ways. For each, the `target` property of an Annotation contains two subsidiary properties, `source` and `styleClass`. The former takes the URI of the Canvas containing the IIIF resource to be annotated and the latter takes an arbitrary string with a class name. Each also uses a `stylesheet` property at the same level as the Annotation's `id`.

For an inline stylesheet, the `stylesheet` property has two subsidiary properties, `type` and `value`. The `type` value is invariantly `CssStylesheet`, and the `value` is a CSS rule for a class whose name is the same as the `styleClass` value used in the Annotation's `target`.

For an external stylesheet, the `stylesheet` property value is a string containing the stylesheet's URI.

## Restrictions

The CSS approach depends wholly on viewer implementation of CSS as applied to a resource. Viewers have no requirement to support CSS styling. Browser-based viewers may defer CSS implementation in whole or in part to the browser. Consequently, and also for reasons of accessibility, annotations should not rely on styling for semantics and should be readable by a human or machine without styling.

One example: Since IIIF Canvas dimensions are unit-less, using pixels for text size is valid but may be interpreted variably across viewers or other clients.

## Example

This recipe focuses on annotations with motivations other than painting and on an external CSS stylesheet. For styling a IIIF resource that uses a `motivation` of `painting`, see [Image Rotation Two Ways][0040] (inline stylesheet) and [Visible Text Resource on a Canvas][0561] (inline CSS). A viewer might render the manifest in this recipe as shown in this image:

![One possible rendering of this recipe's manifest](image_css_external_stylesheet.png)

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="56,60,75,79"' %}

## Related Recipes

* [Image Rotation Two Ways][0040], for an inline CSS stylesheet used with a IIIF resource
* [HTML in Annotations][0019], a complementary recipe (for markup), including a brief discussion of cautions
* [Visible Text Resource on a Canvas][0561], for inline CSS used with a painted textual resource

{% include acronyms.md %}
{% include links.md %}


