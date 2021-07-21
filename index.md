---
title: IIIF Cookbook
layout: spec
tags: [tbc]
summary: "tbc"
hero:
    image: "https://ids.si.edu/ids/iiif/NMAH-AC0396-0000007/131,1118,1840,1011/1500,/0/default.jpg"
---

The [IIIF Presentation API][prezi3] specifies a standardized way to describe complex digital objects. The resource types and properties of the specification are the building blocks of interoperable representations, for rendering by viewers and other software clients. This cookbook gathers together many examples of these representations (usually IIIF Manifests), in order to:

* provide many more examples than the specification alone can do, for reference and learning;
* encourage publishers to adopt common patterns in modeling classes of complex objects;
* enable client software developers to support these patterns, for consistency of user experience (when desirable);
* demonstrate the applicability of IIIF to a broad range of use cases.

The issues of the [Cookbook Recipes repository][cookbook-issues] are used to identify and discuss cookbook recipes, prior to their inclusion in the final cookbook site.

## Contributing

Anyone is welcome to submit a recipe idea or work on implementing a recipe. Advice and support can be received from the IIIF Cookbook channel on the IIIF Slack. For detailed information on how to contribute please see the [Cookbook process][cookbook-process].

## The Recipes

### Building a manifest in stages, adding more complexity at each stage

#### [Simplest Manifest - Image][0001]
The simplest viable manifest for image content. If all you have for an object is one image on the web and a label, this pattern turns it into a IIIF Presentation resource.

#### [Simplest Manifest - Audio][0002]
The simplest viable manifest for audio content. This pattern presents a single audio file in a IIIF Presentation resource.

#### [Simplest Manifest - Video][0003]
The simplest viable manifest for video content. This pattern presents a single video file in a IIIF Presentation resource.

#### [Image and Canvas with Differing Dimensions][0004]
Demonstrates that image dimensions (pixels) need not be the same as the Canvas dimensions (unit-less).

#### [Support Deep Viewing with Basic Use of a IIIF Image Service][0005]
Paint a Canvas using an image with an associated IIIF Image API service.

#### [Internationalization and Multi-language Values][0006]
An example of a IIIF Resource with labels/descriptions in multiple languages.

#### [Displaying Multiple Values with Language Maps][0118]
The language map pattern requires that all values are supplied as an array, whether a single value string or a string of multiple values.

#### [Embedding HTML in descriptive properties][0007]
You want to have more control of how your metadata is displayed. For example scientific names, and also links out to other sites. Also legacy systems that might include things like italic tags.

#### [Metadata on any Resource][0029]
Provide item metadata for displaying to users.

#### [Rights statement\(s\)][0008]
You want to assert a license or rights statement that applies to the content of the resource, such as the JSON of a Manifest or the pixels of an image.

#### [Simple Manifest - Book][0009]
Represent a book, or any object composed of a set of images, as a simple Manifest.

#### [Book behavior (paging) variations][0011]
The 'behavior' property specifies how Canvases should be displayed in the viewer in relation to one another, such as paged for book-view, continuous for a scroll or accordion book, or as individuals for a book imaged as full page spreads.

#### [Viewing direction and its effect on navigation][0010]
Informing a client how the Canvases should be displayed to the viewer in order to read the contents authentically in accordance with the script used, object layout, or reading practice.

#### [Manifest Thumbnail][0117]
Display a thumbnail image for a resource other than a Canvas, such that it can be used by clients to represent the object.

#### thumbnail algorithm / discussion

#### [Load a Preview Image Before the Main Content][0013]
Provide the user with something to look at before they choose to start interacting with the main content, and/or while they wait for it to load/buffer.

#### [Audio Presentation with Accompanying Image][0014]
Provide the user with something to look at before they choose to start interacting with the main content, and/or while they wait for it to load/buffer, and/or while interacting with the main content.

#### [Load Manifest Beginning with a Specific Canvas][0202]
This manifest uses the 'start' property to specify which Canvas the client should display on initialization of the resource.

#### [Begin playback at a specific point - Time-based media][0015]
This manifest uses the 'start' property to specify a point in an audio or video object where a client application should begin playback.

#### [Navigation by Chronology][0230]
You have one or more IIIF resources that have dates associated with them, and would like to communicate their dates to a consuming client for putting in a date-based interface. 

#### [Acknowledge Content Contributors][0234]
Include a rich set of information for each content contributor so clients can make this information visible.

### Textual and other supplementary content

#### Transcription of image-based content - various examples gathered

#### Transcription of audio and video

#### [Using Caption and Subtitles with Video Content][0219]
Representing the tight relationship between a video file and its caption or subtitle file.

#### Transcription of content into XML, with XPaths to select a segment

#### [Providing Alternative Representations][0046]
Linking to non-IIIF representations of the object, such as a PDF.

### Other kinds of annotations
_(leading on to segmentation examples later)_

#### comments - various examples

#### Fragment selectors

#### tagging

#### hotspot linking

#### Annotation in the context of a particular content resource 
https://github.com/IIIF/iiif-stories/issues/101

#### [Geographic coordinates][0139]
Use Web Annotation to provide geocoordinates for a fragment of an IIIF Presentation API 3.0 Canvas.

### Internal structure

#### [Table of Contents for Book Chapters][0024]
Using Ranges to create a table of contents for a book.

#### table of contents (ranges) - articles in a newspaper

#### [Table of contents for A/V content][0026]
Complex nested table of contents, e.g. for an opera.

#### Alternative Sequence (via `sequence` Range)

#### `sequence` Range with partial canvases

### Higher-level structure

#### [Multi-volume Work with Individually-bound Volumes][0030]
With multi-volume works, it is often desirable to group the volumes together as a single work while maintaining the user experience of separate volumes.

#### bound multi-volume work

#### paged Collections (from #1343)

### Segmentation and complex resources

#### Choice (simplest)

#### Choice - multispectral flavored example, with image services

#### foldouts, etc (Choice or non-paged interlude (flaps vs maps))?

#### Multiple images (master/detail)

#### Multiple images and multiple choices

#### Annotating part of an image to a Canvas (e.g., crop out scanner)

#### Image with CSS Rotation

#### Reusing an image service (ImageApiSelector)

#### non-rectangular segmentation

#### temporal segmentation

#### Audio only from video (and other xxxContentSelector scenarios)

#### canvas on canvas (#1191)

#### CSS styling

### Linking

#### alternative representations (rendering (?))

#### Homepage

#### Linking from Image API to Presentation API (via partOf as per #600, #1507)

#### Linking from Image API to external metadata

#### Linking from external metadata to Image API

#### Linking from external metadata to Presentation API

#### Linking between Presentation API representations

#### [Linking to Structured Metadata][0053]
You have a IIIF manifest resource along with additional machine-readable metadata usable by aggregators and others that can process or index it via the [`seeAlso`](https://iiif.io/api/presentation/3.0/#seealso) property.

### Technical

#### extensions

#### services

#### Mixed version scenarios (Prezi 3+Image 2)

#### Publishing v2 and v3 versions

### Real-world complex objects (ideally taken from actual collections)

#### An Image gallery

#### museum object (fwd ref to renderings)

#### A complex printed work with foldouts and choice

#### A music album's audio resources

#### ...and its image resoures

#### ...combined to demonstrate _together_

#### [Table of Contents for Multiple A/V files on a Single Canvas][0064]
A video recording of an opera on one Canvas.

#### [Table of Contents for Multiple A/V files on Multiple Canvases][0065]
A real world example of an audio recording of an opera spread across multiple Canvases.

#### Adaptive bit rate AV examples

#### A field recording

#### [A newspaper][0068]
An outline of common mapping solutions for Newspapers. 

#### Example with extensions and services

#### A manuscript with multiple orderings

#### a Sammelband

#### Archival collection (hierarchy, paging)

#### Thumbnail range for video navigation

#### Video with captions in multiple languages

#### Mixed Image Service references (a mashup, with img2 and img3 services)

#### Glenn Gould - score and performance scenarios (transcribing)

#### A Map


### Access Control
_this might be in a separate auth cookbook_

#### probe service for simple resource

#### auth for adaptive bit rate media (MPEG-DASH)

#### [Anyone can deep zoom, auth reqd for hi-res download](https://digirati-co-uk.github.io/iiif-auth-client/?image=https://iiifauth.digtest.co.uk/img/11_kitty_joyner.jpg/info.json)

{% include acronyms.md %}
{% include links.md %}
