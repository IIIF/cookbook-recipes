---
title: Annotating a Poetry Reading
id: 103
layout: recipe
tags: [audio, presentation, annotation]
summary: "Use annotations to indicate aspects of the performance of a particular poem."
---


## Use Case

While an audio file of a poetry performance may be divided into a track for each poem, scholars may wish to use annotations to indicate aspects of the performance of a particular poem.  

A researcher might want to annotate the following types of information:
* structural information (introduction, title, stanzas)
* points where the performer takes a breath
* repeated phrases

Since annotations could be available at the same time the manifest is generated, or might be a separate process that references the item manifest, both scenarios are shown.

There is a third use case where manifests are unaware of annotations on them, but the systems that display the item are aware of the annotations and pull them in, using the target block in the annotation.

## Implementation notes

This implementation builds off of the [audio example][0002], but adds Web Annotations.

This recipe shows two variations of referencing annotations from within a manifest.  The first has the annotations embedded within the manifest file.  The second has a reference to annotations in a separate file.


## Example

A manifest for the poem "Her Kind" read by Anne Sexton in 1974.  The recording is 107 minutes long.  Annotations are included in the manifest and show both a point annotation (at a particular time) and a range annotation (covering a time range).  (For more on these annotations, see the [annotation.json file description.](#annotations))

{: .line-numbers data-src="manifest1.json" }
```json
```

The same manifest, but with a reference to annotations in a separate file.  The annotation file is included below the manifest. 

{: .line-numbers data-src="manifest2.json" }
```json
```

<a name="annotations"></a>Annotation examples, both a point annotation (at a particular time) and a range annotation (covering a time range).  We use the "supplementing" motivation because these annotations are derived from the audio file on the canvas and the "commenting" motivation because the annotations are a comment about the canvas.  Annotations must have "supplementing" as a motivation for any annotations derived from the items on the canvas.

{: .line-numbers data-src="annotations.json" }
```json
```

# Related recipes

* [Simple Manifest - Audio][0002]
* [Transformation - WebVTT or OHMS XML to Annotations][0079]


{% include acronyms.md %}
{% include links.md %}

