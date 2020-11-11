---
title: Alternative representations through rendering
id: 46
layout: recipe
tags: [tbc]
summary: "tbc"
---

https://iiif.io/api/presentation/3.0/#rendering

A resource that is an alternative, non-IIIF representation of the resource that has the rendering property. Such representations typically cannot be painted onto a single Canvas, as they either include too many views, have incompatible dimensions, or are compound resources requiring additional rendering functionality. The rendering resource must be able to be displayed directly to a human user, although the presentation may be outside of the IIIF client. The resource must not have a splash page or other interstitial resource that mediates access to it. If access control is required, then the IIIF Authentication API is recommended. Examples include a rendering of a book as a PDF or EPUB, a slide deck with images of a building, or a 3D model of a statue.

The value must be an array of JSON objects. Each item must have the id, type and label properties, and should have a format property.

    Any resource type may have the rendering property with at least one item.
    Clients should render rendering on a Collection, Manifest or Canvas, and may render rendering on other types of resource.


## Use Case

HYou hjave a manuscript object for which you also have a PDF with a transcription and translation that you want to make available to researchers. The transcription can be made available through use of the `rendering` property.

## Implementation notes

This property is used for pointing a researcher to a non-IIIF representation of the resource to which it is attached. This is the biggest distinction between this property and `accompanyingCanvas`, which might seem functionally similar. In addition, this property addresses additional representations of the same resource while `accompanyingCanvas` is used for content complementary to the main resource and rendered simultaneously.

## Restrictions

This property is not for use for presenting multiple IIIF views of the same resource, such as an infrared and natural light view of a painting. For that use case, you should use [].

## Example

{ Narrative }

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="NN"' %}


# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}

