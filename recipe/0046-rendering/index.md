---
title: Providing Alternative Representations
id: 46
layout: recipe
tags: [image, presentation, canvas]
summary: "Linking to non-IIIF representations of the object, such as a PDF."
---

## Use Case

You have an archival object in IIIF format for which you would like to offer researchers the opportunity to download a PDF version. You know from previous experience that researchers using your collection like to have images and texts available for offline reading, or you know you have patrons with bandwidth concerns who need to minimize their time online, or other reasons such as wanting to provide transcriptions and translations of objects' text. Through use of the `rendering` property, you are able to alert conforming clients to the presence of this other format (or yet other formats, such as ePub) so they in turn can provide appropriate UX workflows to users.

## Implementation notes

This property is used for pointing a viewer to a non-IIIF representation of the resource to which it is attached. In general, the other representation will need a distinct client for viewing from the one used for the IIIF resource.

Three other properties may seem similar, so it's worth highlighting the differences. 

### homepage
Where `rendering` presents an additional representation of the same resource, [`homepage`](https://iiif.io/api/presentation/3.0/#homepage) points to a webpage _about_ the object represented by the resource.

### accompanyingCanvas
An `accompanyingCanvas` resource is a IIIF resource presented simultaneously with the main resource, where a target of `rendering` is not IIIF-compatible and must be viewed outside the main resource's viewer. In addition, `accompanyingCanvas` is used for content complementary to the main resource while `rendering` points to additional representations of the same resource.

### seeAlso
Unlike `rendering`, the `seeAlso` property provides the URI of a machine-readable resource related to the current resource. In most cases, this will be metadata in a format such as Dubin Core, MODS, or RDF.

Any resource may have the `rendering` property. Each instance of it may have multiple items contained inside it, provided each has the `id`, `type`, and `label` properties at a minimum. Conforming clients should render this property in some way on a Collection, Manifest, or Canvas, but may on other resources. Note particularly that the client's display of the property has no defined form.

## Restrictions

This property is not for use for presenting multiple IIIF versions of the same view, such as an infrared and natural light view of a painting. For that use case, you should use [Choice (simplest)][0033] or [Choice — multispectral flavored example, with image services][0034].

## Example

In this example, the PDF to be made available is for the program as a whole, and as such the `rendering` property is on the Manifest. If PDFs were available for each view or page separately, each Canvas would be the logical place for the corresponding PDF.

To see the property in action in Mirador, toggle the sidebar by activating the three-line ("hamburger") menu in the upper left-hand corner of the content window. You should then, in the "Related" area, see the link under the "Alternate formats" heading.

{% include manifest_links.html viewers="Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="16-27"' %}


# Related recipes

* [seeAlso][0009] for data representations of the same object
* [Audio Presentation with Accompanying Image][0014], using `accompanyingCanvas` to present one IIIF resource simultaneously with another
* [Choice (simplest)][0033] for showing multiple representations of the same view
* [Choice — multispectral flavored example, with image services][0034] for showing multiple representations of the same view with Image Services
* [homepage][0047] for pointing to a web page about the object represented by the current resource
* [A museum object][0059] for using `rendering` to provide a 3D model

{% include acronyms.md %}
{% include links.md %}

