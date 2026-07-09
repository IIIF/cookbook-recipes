---
title: IIIF Cookbook
layout: page
hero:
  image: "assets/images/heroes/smithsonian_cookbook.webp"
---

The [IIIF Presentation API][prezi3] specifies a standardized way to describe complex digital objects. The resource types and properties of the specification are the building blocks of interoperable representations, for rendering by viewers and other software clients. This cookbook gathers together many examples of these representations (usually IIIF Manifests), in order to:

* provide many more examples than the specification alone can do, for reference and learning;
* encourage publishers to adopt common patterns in modeling classes of complex objects;
* enable client software developers to support these patterns, for consistency of user experience (when desirable);
* demonstrate the applicability of IIIF to a broad range of use cases.

The issues of the [Cookbook Recipes repository][cookbook-issues] are used to identify and discuss cookbook recipes, prior to their inclusion in the final cookbook site.

{{ theme.block-center-start }}
## Viewer Support
As part of the work to aid implementation the Cookbook group have developed a Viewer Matrix which shows which recipe is supported by which IIIF viewer.

{% include misc/button.html button_link="recipe/matrix/" button_label="IIIF v3 viewer support" %}
{% include misc/button.html button_link="recipe/matrix-v4/" button_label="IIIF v4 viewer support" %}
{{ theme.block-end }}

## Presentation API Versions

The cookbook contains recipes primarily for version 3 of the IIIF Presentation API. Where a recipe has been written for only version 4, or for both versions 3 and 4, that is indicated following the recipe title.

## Code samples

As well as viewer support, the cookbook provides links to code samples in various development libraries to aid developers who hope to re-create these recipes in Code. You can see a full list of recipes with code samples in the [code samples](recipe/code/) page.

# Contributing

Anyone is welcome to submit a recipe idea or work on implementing a recipe. Advice and support can be received from the IIIF Cookbook channel on the IIIF Slack. For detailed information on how to contribute please see the [Cookbook process][cookbook-process].

# The Recipes

## Building a manifest in stages, adding more complexity at each stage

* Simplest Manifest - Image ([version 3][0001] / [version 4][0001-4])
* Simplest Manifest - Audio ([version 3][0002] / [version 4][0002-4])
* Simplest Manifest - Video ([version 3][0003] / [version 4][0003-4])
* Simplest Manifest - 3D ([version 4][0608-4])
* Image and Canvas with Differing Dimensions ([version 3][0004])
* Support Deep Viewing with Basic Use of a IIIF Image Service ([version 3][0005])
* Internationalization and Multi-language Values ([version 3][0006])
* Displaying Multiple Values with Language Maps ([version 3][0118])
* Embedding HTML in descriptive properties ([version 3][0007])
* Metadata on any Resource ([version 3][0029])
* Rights statement\(s\) ([version 3][0008])
* Simple Manifest - Book ([version 3][0009])
* Book behavior (paging) variations ([version 3][0011])
* Addressing a spatial region ([version 3][0299])
* Viewing direction and its effect on navigation ([version 3][0010])
* Missing Images in a Sequence ([version 3][0283])
* Image Thumbnail for Manifest ([version 3][0117])
* Implementation discussion: Thumbnails on Canvases ([version 3][0232])
* Load a Preview Image Before the Main Content ([version 3][0013])
* Audio Presentation with Accompanying Image ([version 3][0014])
* Load Manifest Beginning with a Specific Canvas ([version 3][0202])
* Begin playback at a specific point - Time-based media ([version 3][0015])
* Navigation by Chronology ([version 3][0230])
* Locate a Manifest on a Web Map ([version 3][0154])
* Locate Multiple Canvases on a Web Map ([version 3][0240])
* Acknowledge Content Contributors ([version 3][0234])
* Simple Collection ([version 3][0032])
* Reuse parts of a Manifest ([version 3][0464])


## Textual and other supplementary content

* Using Transcripts with A/V Content ([version 3][0017])
* Scholarly Annotation of a Poetry Reading ([version 3][0103])
* Using Captions and Subtitles with Video Content ([version 3][0219])
* Providing Alternative Representations ([version 3][0046])
* Transcripts, Captions, and Subtitles - General Considerations ([version 3][0231])
    * Providing Access to Transcript Files of A/V Content ([version 3][0017])
    * Using Caption Files with Video Content ([version 3][0219] / [version 4][0219-4])

## Other kinds of annotations
(These are also building blocks for segmentation, below)

* Simplest Annotation ([version 3][0266])
* HTML in Annotations ([version 3][0019])
* CSS in an Annotation ([version 3][0045])
* Simple Annotation - Tagging ([version 3][0021])
* Annotation with a Non-Rectangular Polygon ([version 3][0261])
* Tagging with an External Resource ([version 3][0258])
* Redirecting from one Canvas to another resource (Hotspot linking) ([version 3][0022])
* Annotate a specific images or layers ([version 3][0326])
* Annotating a specific point of an image ([version 3][0135])
* Geographic coordinates ([version 3][0139])
* Embedded or Referenced Annotations ([version 3][0269])
* Linking external Annotations targeting a Canvas to a Manifest ([version 3][0306])
* Using Annotation collections ([version 3][0309])
* Image in annotations ([version 3][0377])
* Annotating in Multiple Languages ([version 3][0346])
* Visible Text Resource on a Canvas ([version 3][0561])


## Internal structure

* Table of Contents for Book Chapters ([version 3][0024])
* Table of contents for A/V content ([version 3][0026])
* Adding Thumbnail Navigation and `no-nav` to a Video Resource ([version 3][0229])
* Alternative Page Sequences ([version 3][0027])


## Higher-level structure

* Multi-volume Work with Individually-bound Volumes ([version 3][0030])
* Multiple Volumes in a Single Bound Volume ([version 3][0031])


## Segmentation and complex resources

* Multiple choice of images in a single view ([version 3][0033])
* Foldouts, Flaps, and Maps ([version 3][0035])
* Composition from Multiple Images ([version 3][0036])
* Rendering Resources Sequentially on a Timeline ([version 3][0560])
* Rendering Multiple Media Types on a Time-Based Canvas ([version 3][0489])
* Image Rotation Two Ways ([version 3][0040])


## Linking

* Linking to Web Page of an Object (homepage) ([version 3][0047])
* Linking to Structured Metadata ([version 3][0053])


## Sharing IIIF content
Recipes using [Content State API](https://iiif.io/api/content-state/1.0/)

* Loading a manifest with a viewer using a link ([version 3][0466])
* Open a specific region of a canvas in a viewer ([version 3][0485])
* Sharing a link for opening two or more Canvases ([version 3][0540])
* Drag and drop ([version 3][0599])


## Technical

* Making IIIF Presentation API v2 and v3 manifests available at the same URL ([version 3][0057])


## Real-world complex objects (ideally taken from actual collections)

* Multiple Choice of Audio Formats in a Single View (Canvas) ([version 3][0434])
* Table of Contents for Multiple A/V files on a Single Canvas ([version 3][0064])
* Table of Contents for Multiple A/V files on Multiple Canvases ([version 3][0065])
* Basic Newspaper ([version 3][0068])
* Using Caption and Subtitle Files in Multiple Languages with Video Content ([version 3][0074])
* Locating an Item in Place and Time ([version 3][0318])


{% include acronyms.md %}
{% include links.md %}
