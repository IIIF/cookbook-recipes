---
title: Two Uses of Behavior with Ranges
id: 229
layout: recipe
tags: structure
summary: "tbc"
viewers:
 - Annona
 - Theseus
 - Aviary
 - Ramp
topic: 
 - structure
---

## Use Case

In watching a single-file IIIF video resource you will display in a client, visitors could benefit from the ability to navigation within it visually, a bit like having thumbnail scrubbing. You're not able to segment the video, and you prefer visual navigation to a textual table of contents.

## Implementation Notes

The cookbook discusses elsewhere ways to use the `behavior` property for determining paging in a book (9, 11), viewing direction for a visual resource (10), visibility of `tagging` Annotations (21), tables of contents (24, 64, 65), collection structure (30), and how to indicate an alternate view of book contents such as for a foldout (35).

This recipe shows two ways that `behavior` can act in a Range to tell a client how navigation should work. (There isn't going to be a discussion of Ranges per se here; for that, you should read [the spec][prezi3-range].) 

The first way is to use `behavior` with a value of `no-nav` to tell a client explicitly to not include a portion of the resource in navigation, by adding 



## Restrictions

None known.

## Example

The first nine seconds of the video are marked, in the first subsidiary Range, with `no-nav` because they contain no meaningful video and audio. (In an authentic environment, "meaningful" is up for discussion.) Subsequent peer Ranges divide the video into 10 segments, each assigned a `thumbnail` property and a thumbnail image. While in an authentic environment these might be created from moments that are structurally, semantically, pedagogically, or otherwise significant, here they are merely an equal amount of running time except for the final one.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="10-13"'%}

The direct link to the fixture is a useful convenience.

## Related Recipes

{% include links.md %}

