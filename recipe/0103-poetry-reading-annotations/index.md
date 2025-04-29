---
title: Scholarly Annotation of a Poetry Reading
id: 103
layout: recipe
tags: [audio, presentation, annotation]
summary: "Use annotations to indicate aspects of the performance of a particular poem."
viewers:
  - Mirador
  - Aviary Viewer
  - Ramp
  - UV
topic:
  - AV
code:
  - iiif-prezi3
---


## Use Case

While an audio file of a poetry performance may be divided into a track for each poem, scholars may wish to use annotations to indicate aspects of the performance of a particular poem.  

For a performance of a published text, transcribing the performance is of little use to the researcher annotating the performance.  Rather, the annotations serve as commentary on the performance itself.

A researcher might want to annotate the following types of information:
* structural information (introduction, title, stanzas)
* points where the performer takes a breath
* repeated or emphasized phrases

## Implementation notes

This implementation builds off of the [audio example][0002], but adds Web Annotations. We show both annotation targeting using a FragmentSelector and a simplified Media Fragment appended to the canvas URL.

FragmentSelector using a SpecificResource:

```
"target":{
  "type":"SpecificResource",
  "source":{
     "id":"{{ id.path }}/canvas/1",
     "type":"Canvas",
     "partOf":[
        {
           "id":"{{ id.url }}",
           "type":"Manifest"
        }
     ]
  },
  "selector":{
     "type":"FragmentSelector",
     "conformsTo":"http://www.w3.org/TR/media-frags/",
     "value":"t=705.0,707.0"
  }
}

```

Media Fragment using "#t=702.0,705.0" appended to the canvas URL. Instead of "source" you'd condense it into the "target" field:

```
"target":"{{ id.path }}/canvas/1#t=702.0,705.0"
```

If you are targeting a single point, you should use a point selector.  The [Begin playback at a specific point - Time-based media][0015] recipe demonstrates that approach.

Because the annotations are pointing out features of the audio, rather than transcriptions, the "motivation" for each annotation is "commenting" not "supplementing".  (If the annotations were transcriptions, their motivation would be "supplementing".)


## Example

A manifest for a poetry reading by Canadian poet Daphne Marlatt in 2018.  The recording is 707 seconds long.
{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest2.json" %}


# Related recipes

* [Simple Manifest - Audio][0002]
* [Transformation - WebVTT or OHMS XML to Annotations][0079]
* [Begin playback at a specific point - Time-based media][0015]
* [Embedded or Referenced Annotations][0269]

{% include acronyms.md %}
{% include links.md %}

