---
title: An opera on multiple Canvases
id: 65
layout: recipe
tags: [video, presentation, opera]
summary: "A real world example of an audio recording of an opera spread across multiple canvases."
---


## Use Case

An opera performance can be long and split across multiple physical tapes, reels, or cassettes.  These may be digitized as one file per physical medium then mapped to one canvas per file.  This real world example shows how this can be modeled using multiple canvases.

## Implementation Notes

Implementation is identical to the [opera on one canvas recipe][0064] except that the two files, one for each act, each have their own canvas and are referenced as such in the structures.  With two canvases the viewer will show the duration of only the currently playing file and the time will start at zero again when switching between files.  This may be helpful when you have time references within files instead of the opera as a whole.

## Example

[JSON-LD](manifest.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```

## Related Recipes

* [Table of Contents - Opera][0026] - Another example of using nested ranges to represent an opera's table of contents.
* [Opera One Canvas][0064] - The same opera from this example but in video format on one canvas.

{% include acronyms.md %}
{% include links.md %}