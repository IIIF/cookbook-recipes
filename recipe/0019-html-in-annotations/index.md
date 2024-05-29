---
title: HTML in Annotations
id: 19
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
  - Mirador
  - Annona
  - Glycerine Viewer
topic: 
 - basic
code:
 - iiif-prezi3
---

## Use Case

You want to create an Annotation on a Canvas that contains a link or other HTML feature that can not be expressed in plain text. In this recipe we'll discuss the specifics of using HTML in the Annotation body, see [Simplest Annotation][0266] for a general description of the Annotation structure and an example of a plain text Annotation body.

## Implementation Notes

The body of an Annotation can be a simple piece of plain text that is embedded in the Annotation as in the [Simplest Annotation][0266] example. It can also be a piece of HTML instead of plain text or it can be a URL pointing to an external HTML document. In the following example we are using an embedded HTML body.

The `body` property of the Annotation is an object with a `type` of `TextualBody` that contains the HTML text in a `value` property and specifies the format `text/html` in a `format` property and optionally the language (e.g. `de` for German) in a `language` property.

Please note that the `language` and `value` properties in the Annotation body are not a language map used with labels or descriptions in the Manifest. You can not use the [Internationalization and Multi-language Values][0006] pattern for multilingual content in an Annotation body. You can instead put a list of multiple `TextualBody` objects with different `language` properties in the `body` property of the Annotation but viewers may show all languages at the same time or not support this pattern at all.

## Restrictions

The W3C [Web Annotation specification](https://www.w3.org/TR/annotation-model/#embedded-textual-body) does not specify which HTML elements are allowed in the body of an Annotation but all viewers will effectively limit the HTML elements you can use in the Annotation for technical and security reasons.

The [IIIF Presentation specification](https://iiif.io/api/presentation/3.0/#45-html-markup-in-property-values) contains explicit restrictions for HTML content in Property Values that clients should enforce (see [Embedding HTML in descriptive properties][0007]).

Although the Property Values rules do not technically apply to HTML Annotation bodies it seems advisable to follow these rules as the lowest common denominator:

* Your HTML should be well-formed XML and therefore should be wrapped in an element such as `p` or `span`.
* To alert a consuming application that your content is HTML, the first character in your string should be `<` and the last character should be `>`.
* These are the tags that the client may support and others may be stripped: `a`, `b`, `br`, `i`, `img`, `p`, `small`, `span`, `sub`, and `sup` tags and `href` attributes on the `a` tag, and `src` and `alt` on the `img` tag.

If you have requirements outside of these rules you may be able to configure a custom instance of a IIIF viewer to allow more HTML elements (Mirador defines [configurable rules](https://github.com/ProjectMirador/mirador/blob/master/src/lib/htmlRules.js)) but this would limit the general usefulness and reusability of your IIIF Manifests and Annotations.

## Example

This example Manifest contains an embedded Annotation containing the HTML text "Göttinger Marktplatz mit Gänseliesel Brunnen" with a link to the Wikipedia Article "Gänseliesel-Brunnen (Göttingen)" behind the words "Gänseliesel Brunnen" and an image of the Wikipedia logo. The Annotation has the motivation `commenting` targeting the whole Canvas. The Annotation is the single content of an Annotation Page contained in the `annotations` property of the Canvas.

{% include manifest_links.html viewers="Mirador,Annona, Glycerine Viewer" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="53-58"' %}

## Related Recipes

* [Simplest Annotation][0266] for a general description of Annotations and an example of a plain text body
* [Embedding HTML in descriptive properties][0007] for the use of HTML in Property Values

{% include acronyms.md %}
{% include links.md %}

