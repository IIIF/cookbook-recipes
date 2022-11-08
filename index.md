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

# Contributing

Anyone is welcome to submit a recipe idea or work on implementing a recipe. Advice and support can be received from the IIIF Cookbook channel on the IIIF Slack. For detailed information on how to contribute please see the [Cookbook process][cookbook-process].

# The Recipes

## Building a manifest in stages, adding more complexity at each stage

_The corresponding 2.1 test fixture(s) is given like this, where appropriate: ..(3,5)_

* [Simplest Manifest - Image][0001] (1) (use static image as content resource, w.h)
* [Simplest Manifest - Audio][0002] (1) (use single audio as content resource, d)
* [Simplest Manifest - Video][0003] (1) (use single video as content resource, w,h,d)
* [Image and Canvas with Differing Dimensions][0004] (26)
* [Support Deep Viewing with Basic Use of a IIIF Image Service][0005] (24,25)
* [Internationalization and Multi-language Values][0006] (3,4,6)
* [Displaying Multiple Values with Language Maps][0118]
* [Embedding HTML in descriptive properties][0007] (64)
* [Metadata on any Resource][0029] (21)
* [Rights statement\(s\)][0008] (7)
* [Simple Manifest - Book][0009] (19)
* [Book behavior (paging) variations][0011] (15,16,17)
* [Addressing a region][0299]
* [Viewing direction and its effect on navigation][0010] (11,12,13,14)
* [Manifest Thumbnail][0117]
* [Implementation discussion: Thumbnails on Canvases][0232]
* [Load a Preview Image Before the Main Content][0013]
* [Audio Presentation with Accompanying Image][0014]
* [Load Manifest Beginning with a Specific Canvas][0202]
* [Begin playback at a specific point - Time-based media][0015] (65)
* [Navigation by Chronology][0230]
* [Locate a Manifest on a Web Map][0154]
* [Locate Multiple Canvases on a Web Map][0240]
* [Acknowledge Content Contributors][0234]

## Textual and other supplementary content

* [Transcription of image-based content][016]
* [Using Transcripts with A/V Content][0017]
* [Using Captions and Subtitles with Video Content][0219]
* Transcription of content into XML, with XPaths to select a segment
* [Providing Alternative Representations][0046]
* [Transcripts, Captions, and Subtitles - General Considerations][0231]
    * [Providing Access to Transcript Files of A/V Content][0017]
    * [Using Annotations for Timed Text][0079]
    * [Using Caption and Subtitle Files with Video Content][0219]
    * [A Side-by-side Transcript of a Video Recording][0253]
* Transcription of content into XML, with XPaths to select a segment

## Other kinds of annotations
_(leading on to segmentation examples later)_

* comments - various examples (51,52,54)
* [Simplest Annotation][0266]
* [HTML in Annotations][0019]
* Fragment selectors (61)
* [Simple Annotation - Tagging][0021]
* [Annotation with a Non-Rectangular Polygon][0261]
* [Tagging with an External Resource][0258]
* hotspot linking
* Annotation in the context of a particular content resource https://github.com/IIIF/iiif-stories/issues/101
* [Geographic coordinates][0139]
* [Embedded or Referenced Annotations][0269]

## Internal structure

* [Table of Contents for Book Chapters][0024]
* table of contents (ranges) - articles in a newspaper
* [Table of contents for A/V content][0026] (26)
* Alternative Sequence (via `sequence` Range) (20,22,23)
* `sequence` Range with partial canvases

## Higher-level structure

* [Multi-volume Work with Individually-bound Volumes][0030]
* [Multiple Volumes in a Single Bound Volume][0031]
* paged Collections (from #1343)

## Segmentation and complex resources

* [Multiple choice of images in a single view][0033] (29)
* [Foldouts, Flaps, and Maps][0035]
* [Composition from Multiple Images][0036] (30,31)
* Multiple images and multiple choices (32,33,34)
* [Annotating part of an image to a Canvas][recipe-segment-image-part] (e.g., crop out scanner) (35,36,37,38)
* [Image Rotation Two Ways][0040]
* Reusing an image service (ImageApiSelector) (41)
* non-rectangular segmentation
* temporal segmentation
* Audio only from video (and other xxxContentSelector scenarios)
* canvas on canvas (#1191)
* CSS styling

## Linking

* alternative representations (rendering (?))
* Homepage
* Linking from Image API to Presentation API (via partOf as per #600, #1507)
* Linking from Image API to external metadata
* Linking from external metadata to Image API
* Linking from external metadata to Presentation API
* Linking between Presentation API representations
* [Linking to Structured Metadata][0053] (8)

## Technical

* extensions (18)
* services (9,10)
* Mixed version scenarios (Prezi 3+Image 2)
* Publishing v2 and v3 versions

## Real-world complex objects (ideally taken from actual collections)

* An Image gallery
* museum object (fwd ref to renderings)
* A complex printed work with foldouts and choice
* A music album's audio resources
* ...and its image resoures
* ...combined to demonstrate _together_
* [Table of Contents for Multiple A/V files on a Single Canvas][0064] (64)
* [Table of Contents for Multiple A/V files on Multiple Canvases][0065] (65)
* Adaptive bit rate AV examples
* A field recording
* [A newspaper][0068]
* Example with extensions and services
* A manuscript with multiple orderings
* a Sammelband
* Archival collection (hierarchy, paging)
* Thumbnail range for video navigation
* [Using Caption and Subtitle Files in Multiple Languages with Video Content][0074]
* Mixed Image Service references (a mashup, with img2 and img3 services)
* Glenn Gould - score and performance scenarios (transcribing)
* A Map

## Access Control
_this might be in a separate auth cookbook_

* probe service for simple resource
* auth for adaptive bit rate media (MPEG-DASH)
* [Anyone can deep zoom, auth reqd for hi-res download](https://digirati-co-uk.github.io/iiif-auth-client/?image=https://iiifauth.digtest.co.uk/img/11_kitty_joyner.jpg/info.json)

{% include acronyms.md %}
{% include links.md %}
