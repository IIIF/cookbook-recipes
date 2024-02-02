---
title: Multiple Choice of Audio Formats in a Single View (Canvas)
id: 434
layout: recipe
tags: [multiple-files, layers]
summary: "How to model multiple choices of audio files for the same sound - e.g., formats."
viewers:
 - Ramp
 - UV
 - Clover
 - Mirador
topic: 
 - basic
 - AV
---

## Use Case

For an audio resource, you want to provide viewers or other software readers with multiple formats or qualities so the appropriate and/or compatible one can be presented to the listener.

## Implementation Notes

This recipe is structurally very similar to the image choice recipe, though with a different rationale and different expected outcomes. Where that recipe presented multiple images of the same object, registered against each other, audio choice emerges more frequently from uneven format compatibility in web software.

In the manifest, the central Annotation's `body` is a resource with a type of `choice`. Each resource in the `items` property is instead the media to be presented. This structure is defined in the W3C Web Annotation Data Model:

> "A 'Choice' has an ordered list of resources from which an application should select only one to process or display. The order is given from the most preferable to least preferable, according to the Annotation's creator or publisher." *— from [Choice Between Bodies](https://www.w3.org/TR/annotation-model/#choice-between-bodies)*

Current viewers react with the manifest in a range of ways. Some fail more gracefully than others when they encounter a format they cannot play. Some only try to play the first one or two choices, while others will try to play or offer the visitor to try to play any of the resources in the manifest.

## Restrictions

No known restrictions, but not all viewers will recognize Choice.

## Example

This manifest uses a short excerpt from a 14-minute reel-to-reel recording of music from Kabba Division, Kwara State, Nigeria in the 1980s. From the web version in UCLA's digital library, it was transcoded into 6 different containers and codecs of varying commonness. The first option is highly unlikely to play in any web browser, so it is expected that viewers will select the second option by default. Other options are provided for cookbook readers to see how viewers handle further options and other formats.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

The direct link to the fixture is a useful convenience.

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}

