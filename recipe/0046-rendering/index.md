---
title: Alternative Representations Through Rendering
id: 46
layout: recipe
tags: [image, presentation, canvas]
summary: "Linking to non-IIIF representations of the object, such as a PDF."
---

## Use Case

You have an archival object in IIIF format for which you would like to offer researchers the opportunity to download a PDF version. You know from previous experience that researchers using your collection like to have images and texts available for offline reading, or you know you have patrons with bandwidth concerns who need to minimize their time online, or other reasons such as wanting to provide transcriptions and translations of objects' text. Through use of the `rendering` property, you are able to alert conforming clients to the presence of this other format so they in turn can provide appropriate UX workflows to users.

## Implementation notes

This property is used for pointing a researcher to a non-IIIF representation of the resource to which it is attached. This is the biggest distinction between this property and `accompanyingCanvas`, which might seem functionally similar. In addition, this property addresses additional representations of the same resource while `accompanyingCanvas` is used for content complementary to the main resource and rendered simultaneously.

Any resource may have the `rendering` property. Each instance of it may have multiple items contained inside it, provided each has the `id`, `type`, and `label` properties at a minimum. Conforming clients should render this property in some way on a Collection, Manifest, or Canvas, but may on other resources. Keep in mind that the client's display of the property has no defined form.

## Restrictions

This property is not for use for presenting multiple IIIF versions of the same view, such as an infrared and natural light view of a painting. For that use case, you should use [Choice (simplest)][0033] or [Choice — multispectral flavoured example, with image services][0034].

## Example

In this example, the PDF to be made available is for the program at a whole, and as such the `rendering` property is for the `Manifest`. If the PDFs were available for each view or page separately, each `Canvas` would be the logical place for the corresponding PDF.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="16-27"' %}


# Related recipes

* [seeAlso][0009] for data representations of the same object
* [Choice (simplest)][0033] for showing multiple representations of the same view
* [Choice — multispectral flavoured example, with image services][0034] for showing multiple representations of the same view with Image Services

{% include acronyms.md %}
{% include links.md %}

