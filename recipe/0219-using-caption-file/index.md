---
title: Using a Caption File with Video Content
id: 219
layout: recipe
tags: [video, caption, subtitle, presentation]
summary: "tbc"
---


## Use Case

Captions and/or subtitles may be available for your video content and you may want to enable them for your IIIF video resources. 

## Implementation notes

Caption and subtitle file formats are used to mark up the external text track resources in connection with the HTML <track> element of a video file. The markup file formats use time tags that allow for time alignment of the video content and the captions or subtitles. 

Offering the caption file as an Item in the same Annotation `body` that contains the media file itself enables us to express the tight relationship between the two. The file type clarifies the relationship.

The linking property of type `seeAlso` is not appropriate because captions and subtitles do not contain metadata about the resource. Neither are they an alternative representation of the resource, so the linking property of type `rendering` is also not appropriate.

## Restrictions

No restrictions.

## Example

In this example we use a caption file in the WebVTT (Web Video Text Tracks) format, but one could just as well use a subtitle file in the SRT format, or other text-based formats used for the same purpose.

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest.json" config='data-line="31-36"%}

# Related recipes

- [Simplest Manifest - Video][0003]
- [Transformation - WebVTT or OHMS XML to Annotations][0079] - Recipe using Annotations to express the captions of a video.

{% include acronyms.md %}
{% include links.md %}

