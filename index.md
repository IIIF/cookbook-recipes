---
title: Cookbook of IIIF Recipes
layout: default
tags: [tbc]
summary: "tbc"
---

The [IIIF Presentation API][prezi3] specifies a standardised way to describe complex digital objects. The resource types and properties of the specification are the building blocks of interoperable representations, for rendering by viewers and other software clients. This cookbook gathers together many examples of these representations (usually IIIF Manifests), in order to:

* provide many more examples than the specification alone can do, for reference and learning;
* encourage publishers to adopt common patterns in modelling classes of complex objects;
* enable client software developers to support these patterns, for consistency of user experience (when desirable);
* demonstrate the applicability of IIIF to a broad range of use cases.

The issues of the [Cookbook Recipes repository](https://github.com/IIIF/cookbook-recipes/issues) are used to identify and discuss cookbook recipes, prior to their inclusion in the final cookbook site.

# Contributing

Anyone is welcome to submit a recipe idea or work on implementing a recipe. Advice and support can be received from the IIIF Cookbook channel on the IIIF Slack. For detailed information on how to contribute please see the [Cookbook process](recipe/).

# The Recipes

## Building a manifest in stages, adding more complexity at each stage

_The corresponding 2.1 test fixture(s) is given like this, where appropriate: ..(3,5)_

* [Simplest Manifest - Image][0001] (1) (use static image as content resource, w.h)
* [Simplest Manifest - Audio][0002] (1) (use single audio as content resource, d)
* [Simplest Manifest - Video][0003] (1) (use single video as content resource, w,h,d)
* Image different size to canvas (26)
* Image Service for single image (24,25)
* Multiple values and languages (3,4,6)
* [Embedding HTML in descriptive properties][0007] (64)
* [Rights statement\(s\)][0008] (7)
* thumbnail algorithm / discussion
* Book (simplest, > 1 canvas) (19)
* Book (viewingDirection variations) (11,12,13,14)
* [Book behavior (paging) variations][0011] (15,16,17) 
* [Load a Preview Image Before the Main Content][0013]
* accompanyingCanvas
* start (65)

## Textual and other supplementary content

* Transcription of image-based content - various examples gathered (43,44,45,46,47,48)
* Transcription of audio and video
* Transcription of content into XML, with XPaths to select a segment

## Other kinds of annotations
_(leading on to segmentation examples later)_

* comments - various examples (51,52,54)
* Fragment selectors (61)
* tagging
* hotspot linking
* Annotation in the context of a particular content resource https://github.com/IIIF/iiif-stories/issues/101

## Internal structure

* table of contents (ranges) - book chapters
* table of contents (ranges) - articles in a newspaper
* table of contents (ranges) - acts of an opera
* Alternative Sequence (via `sequence` Range) (20,22,23)
* `sequence` Range with partial canvases
* metadata on any resource (21)

## Higher-level structure

* multi-volume work
* bound multi-volume work
* paged Collections (from #1343)

## Segmentation and complex resources

* Choice (simplest) (28)
* Choice - multispectral flavoured example, with image services (29)
* foldouts, etc (Choice or non-paged interlude (flaps vs maps))?
* [Multiple images (master/detail)][detail-image] (30,31)
* Multiple images and multiple choices (32,33,34)
* [Annotating part of an image to a Canvas][recipe-segment-image-part] (e.g., crop out scanner) (35,36,37,38)
* Image with CSS Rotation (39)
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
* seeAlso scenarios (incl other manifests) (8)

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
* An opera on one Canvas
* An opera on multiple Canvases
* Adaptive bit rate AV examples
* A field recording
* [A newspaper][0068]
* Example with extensions and services
* A manuscript with multiple orderings
* a Sammelband
* Archival collection (hierarchy, paging)
* Thumbnail range for video navigation
* Video with captions in multiple languages
* Mixed Image Service references (a mashup, with img2 and img3 services)
* Glenn Gould - score and performance scenarios (transcribing)

## Access Control
_this might be in a separate auth cookbook_

* probe service for simple resource
* auth for adaptive bit rate media (MPEG-DASH)
* [Anyone can deep zoom, auth reqd for hi-res download](https://digirati-co-uk.github.io/iiif-auth-client/?image=https://iiifauth.digtest.co.uk/img/11_kitty_joyner.jpg/info.json)

{% include acronyms.md %}
{% include links.md %}
