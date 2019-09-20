---
title: Annotating a Poetry Reading
id: 103
layout: recipe
tags: [audio, presentation, annotation]
summary: "Use annotations to indicate aspects of the performance of a particular poem."
---


## Use Case

While an audio file of a poetry performance may be divided into a track for each poem, scholars may wish to use annotations to indicate aspects of the performance of a particular poem.  

Examples of the kinds of information to be annotated may include the following:
* structural information (introduction, title, stanzas)
* points where the performer takes a breath
* repeated phrases

## Implementation notes

This implementation builds off of the [audio example][0002], but adds Web Annotations.


## Example

A manifest for the poem "Her Kind" read by Anne Sexton in 1974.  The recording is 107 minutes long.

{: .line-numbers data-src="manifest.json" }
```json
```
Annotation examples, both a point annotation (at a particular time) and a range annotation (covering a time range)

{: .line-numbers data-src="annotations.json" }
```json
```

# Related recipes

* [Simple Manifest - Audio][0002]
* [Transformation - WebVTT or OHMS XML to Annotations][0079]


{% include acronyms.md %}
{% include links.md %}

