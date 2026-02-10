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

{% include misc/button.html button_link="recipe/matrix/" button_label="See IIIF viewer support" %}
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
* Simplest Manifest - Audio (Presentation API [v3][0002] / [v4][0002-4])
* [Simplest Manifest - Video][0003] - [version 4][0003-4]
* [Simplest Manifest - 3D][0608-4]
* [Image and Canvas with Differing Dimensions][0004]
* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]
* [Internationalization and Multi-language Values][0006]
* [Displaying Multiple Values with Language Maps][0118]
* [Embedding HTML in descriptive properties][0007]
* [Metadata on any Resource][0029]
* [Rights statement\(s\)][0008]
* [Simple Manifest - Book][0009]
* [Book behavior (paging) variations][0011]
* [Addressing a spatial region][0299]
* [Viewing direction and its effect on navigation][0010]
* [Missing Images in a Sequence][0283]
* [Image Thumbnail for Manifest][0117]
* [Implementation discussion: Thumbnails on Canvases][0232]
* [Load a Preview Image Before the Main Content][0013]
* [Audio Presentation with Accompanying Image][0014]
* [Load Manifest Beginning with a Specific Canvas][0202]
* [Begin playback at a specific point - Time-based media][0015]
* [Navigation by Chronology][0230]
* [Locate a Manifest on a Web Map][0154]
* [Locate Multiple Canvases on a Web Map][0240]
* [Acknowledge Content Contributors][0234]
* [Simple Collection][0032]
* [Reuse parts of a Manifest][0464]


## Textual and other supplementary content

* [Transcription of image-based content][016]
* [Using Transcripts with A/V Content][0017]
* [Using Captions and Subtitles with Video Content][0219]
* [Providing Alternative Representations][0046]
* [Transcripts, Captions, and Subtitles - General Considerations][0231]
    * [Providing Access to Transcript Files of A/V Content][0017]
    * [Using Annotations for Timed Text][0079]
    * [Using Caption and Subtitle Files with Video Content][0219]
    * [A Side-by-side Transcript of a Video Recording][0253]


## Other kinds of annotations
_(leading on to segmentation examples later)_

* [Simplest Annotation][0266]
* [HTML in Annotations][0019]
* [CSS in an Annotation][0045]
* [Simple Annotation - Tagging][0021]
* [Annotation with a Non-Rectangular Polygon][0261]
* [Tagging with an External Resource][0258]
* [Redirecting from one Canvas to another resource (Hotspot linking)][0022]
* [Annotate a specific images or layers][0326]
* [Annotating a specific point of an image][0135]
* [Geographic coordinates][0139]
* [Embedded or Referenced Annotations][0269]
* [Linking external Annotations targeting a Canvas to a Manifest][0306]
* [Using Annotation collections][0309]
* [Image in annotations][0377]
* [Annotating in Multiple Languages][0346]
* [Visible Text Resource on a Canvas][0561]


## Internal structure

* [Table of Contents for Book Chapters][0024]
* [Table of contents for A/V content][0026]
* [Adding Thumbnail Navigation and `no-nav` to a Video Resource][0229]
* [Alternative Page Sequences][0027]


## Higher-level structure

* [Multi-volume Work with Individually-bound Volumes][0030]
* [Multiple Volumes in a Single Bound Volume][0031]


## Segmentation and complex resources

* [Multiple choice of images in a single view][0033]
* [Foldouts, Flaps, and Maps][0035]
* [Composition from Multiple Images][0036]
* [Rendering Resources Sequentially on a Timeline][0560]
* [Rendering Multiple Media Types on a Time-Based Canvas][0489]
* [Annotating part of an image to a Canvas][recipe-segment-image-part]
* [Image Rotation Two Ways][0040]


## Linking

* [Linking to Web Page of an Object (homepage)][0047]
* [Linking to Structured Metadata][0053]


## Sharing IIIF content
Recipes using [Content State API](https://iiif.io/api/content-state/1.0/)

* [Loading a manifest with a viewer using a link][0466]
* [Open a specific region of a canvas in a viewer][0485]
* [Sharing a link for opening two or more Canvases][0540]
* [Drag and drop][0599]


## Technical

* [Making IIIF Presentation API v2 and v3 manifests available at the same URL][0057]


## Real-world complex objects (ideally taken from actual collections)

* [Multiple Choice of Audio Formats in a Single View (Canvas)][0434]
* [Table of Contents for Multiple A/V files on a Single Canvas][0064]
* [Table of Contents for Multiple A/V files on Multiple Canvases][0065]
* [Basic Newspaper][0068]
* [Using Caption and Subtitle Files in Multiple Languages with Video Content][0074]
* [Locating an Item in Place and Time][0318]


{% include acronyms.md %}
{% include links.md %}
