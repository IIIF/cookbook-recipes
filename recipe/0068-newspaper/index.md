---
title: Basic Newspaper
id: 68
layout: recipe
tags: [structural, content:image, transcript, presentation]
summary: "An introduction to a relatively simple multi-issue title newspaper with OCR content"
viewers:
 - Mirador
 - Annona
 - UV
topic: 
 - realWorldObject
---

## Use Case

Digitized Newspapers are more complicated than some other types of content as the hierarchy of Titles, Volumes and Issues are important in making them accessible. The date of publication and providing access to OCR data are also important to the viewing experience. This recipe gives an example of a basic Newspaper with two issues and links to text generated from Optical Character Recognition (OCR) software. The aim is to give a good outline of common mapping solutions for Newspapers. 

## Implementation notes

This recipe was put together by Nuno Freire from Europeana and was discussed by the IIIF Newspaper Community Group. The example is a cut down Newspaper with two issues containing two pages. The OCR is at page level rather than article level. The example is for a German Newspaper called the ‘Berliner Tageblatt’ and is hosted by Europeana. In the IIIF domain a Newspaper Title is considered to be a [__IIIF Collection__][0032] and points to each issue, represented as __IIIF Manifests__, in a member of the `items` element. An issue in this example is considered to be the unit or edition that was published on a particular date. For a more complete discussion on Newspaper hierarchies and how they map to IIIF see the IIIF Newspaper Guidance notes. 

### Navigate by Date
(For a full discussion of navigation by chronological order, see [Navigation by Chronology][0230].)

One important feature of newspapers is their publication date, which IIIF manifests can provide to viewers to allow navigation of issues by chronology. To achieve this we use the `navDate` property. This property should be added both to the items in a collection and to each issue's manifest. Viewers are not required to make use of `navDate`, and viewers that do have date-aware navigation available may not default to that navigation interface.

Because manifests have no enforced truth relation to digital objects, an arbitrary temporal value can be inserted to enforce navigation order for newspaper editions. You could, for instance, use `T06:00:00+00:00` in the timestamp portion of a `navDate` property value for a morning edition and `T17:00:00+00:00` for an evening edition just to provide browse order. If you can insert the actual publication time and time zone or time zone offset for an edition, so much the better.

### Linking to OCR Text

#### As Annotations
Digitized newspapers often have associated OCR text. To make this available inside a IIIF viewer, it needs to be in the form of one or more Annotations in the appropriate manifest, structured substantially similarly to [the captions or subtitles of an A/V file][0219]. Each OCR file should correspond to a Canvas, and should be an Annotation in an Annotation Page, with
+ a `motivation` of `supplementing`,
+ the URI of the OCR file in the `id` property of the Annotation body, and
+ the `target` set to the applicable Canvas.

If an OCR file does not represent the entire Canvas, the Annotation's `target` should include a fragment in [#xywh Fragment Selector syntax](https://www.w3.org/TR/annotation-model/#fragment-selector) of the portion of the Canvas the OCR represents. For more detail, see the recipe [Using Caption and Subtitle Files with Video Content][0219].

#### Linking Directly to an ALTO File

As well as linking to Annotations, it is a common use case with newspapers to link to other formats of the content, including the open XML Schema [ALTO](https://www.loc.gov/standards/alto/). This is achieved by using a `rendering` property on the Canvas, as the ALTO content is a alternative representation of the page. ALTO content differs from OCR in that it is a representation of a portion of a newspaper object, not an alternative format of the content of a portion of a newspaper. For more detail on using additional files connected to a newspaper, see the [Providing Alternative Representations][0046] recipe.

## Example

To demonstrate the files that might be included in even a basic newspaper presentation, we've included a number of manifests:
1. Newspaper Title IIIF Collection - [newspaper_title-collection.json](newspaper_title-collection.json)
2. Issue 1 Manifest - [newspaper_issue_1-manifest.json](newspaper_issue_1-manifest.json)
	* Page 1
		* Annotations - [newspaper_issue_1-anno_p1.json](newspaper_issue_1-anno_p1.json)
		* Linked ALTO - [newspaper_issue_1-alto_p1.xml](newspaper_issue_1-alto_p1.xml)
	* Page 2
		* Annotations - [newspaper_issue_1-anno_p2.json](newspaper_issue_1-anno_p2.json)
		* Linked ALTO - [newspaper_issue_1-alto_p2.xml](newspaper_issue_1-alto_p2.xml)

3. Issue 2 Manifest - [newspaper_issue_2-manifest.json](newspaper_issue_2-manifest.json)
	* Page 1
		* Annotations - [newspaper_issue_2-anno_p1.json](newspaper_issue_2-anno_p1.json)
		* Linked ALTO - [newspaper_issue_2-alto_p1.xml](newspaper_issue_2-alto_p2.xml)
	* Page 2
		* Annotations - [newspaper_issue_2-anno_p2.json](newspaper_issue_2-anno_p2.json)
		* Linked ALTO - [newspaper_issue_2-alto_p2.xml](newspaper_issue_2-alto_p2.xml)

We won't display all of them here, as that would get unreadable. However, the Manifest for the title (structured as a IIIF Collection) may be of greatest utility.

{% include manifest_links.html viewers="Mirador, Annona, UV, Clover" manifest="newspaper_title-collection.json" %}

{% include jsonviewer.html src="newspaper_title-collection.json" %}

## Related recipes

- [Simplest Manifest - Image][0001]
- [Simplest Collection][0032]
- [Providing Alternative Representations][0046] for thinking through how to connect additional files relating to a newspaper
- [Using Caption and Subtitle Files with Video Content][0219] for a discussion parallel to how to treat alternate forms of a digitized newspaper's content
- [Navigation by Chronology][0230]

{% include acronyms.md %}
{% include links.md %}

