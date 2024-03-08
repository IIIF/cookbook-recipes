---
title: Multiple Choice of Audio Formats in a Single View (Canvas)
id: 434
layout: recipe
tags: [multiple-files, layers]
summary: "How to model multiple choices of audio files for the same sound - e.g., formats."
viewers:
 - Mirador
 - UV
 - Clover
 - Ramp
topic: 
 - basic
 - AV
---

## Use Case

For an audio resource, you want to provide viewers or other software readers with multiple formats or qualities so the appropriate and/or compatible one can be presented to the listener.

## Implementation Notes

This recipe is structurally very similar to [the image choice recipe][0033], though with a different rationale and different expected outcomes. Where that recipe presented multiple images of the same object, registered against each other, audio choice emerges more frequently from accommodating format compatibility issues in web software. Therefore, there is also a conceptual difference between these two recipes in the notion of choice. In the Image Choice recipe, there is no format difference in the images and therefore no capability difference for the viewer; the choice belongs to the manifest creator and the user. In this recipe, on the other hand, the resources differ in format and therefore can differ for viewer capability; consequently, the choice belongs both to the viewer and to the user.

In the manifest, the central Annotation's `body` is a resource with a type of `choice`. Each resource in the `items` property is instead the media to be presented. This structure is defined in the W3C Web Annotation Data Model:

> "A 'Choice' has an ordered list of resources from which an application should select only one to process or display. The order is given from the most preferable to least preferable, according to the Annotation's creator or publisher." *— from [Choice Between Bodies](https://www.w3.org/TR/annotation-model/#choice-between-bodies)*

Understanding that not all file formats are playable in all viewers or, as relevant, all browsers, the viewer is expected to present for playing the first audio file it is capable of playing.

Developers of viewers or other consuming clients need to understand that the intent is to offer the user a **choice** between 2 or more sound formats, which the user may switch between at will. Publishers can order the audio files by preference, but the file with which a viewer starts cannot be assured.

## Restrictions

No known restrictions.

## Example

This manifest uses a short excerpt from a 14-minute reel-to-reel recording of music from Kabba Division, Kwara State, Nigeria in the 1980s. From the web version in UCLA's digital library, it was transcoded into 6 different containers and codecs of varying commonness. The first option is highly unlikely to play in any web browser, so it is expected that viewers will select the second option by default. Other options are provided for cookbook readers to see how viewers handle further options and other formats. Since the sound content is the same for each file, a computer-voiced format tag has been added to the start of each file for differentiation. This would not be included in a real-world implementation.

In practice, current viewers react with the manifest in a range of ways, with some failing more gracefully than others when they encounter a format they cannot play. Some only try to play the first one or two choices, while others will try to play or offer the visitor to try to play any of the resources in the manifest.

Sound recorded by [Institute of African Studies](https://www.ibadan-ias.org/) of the [University of Ibadan](http://www.ui.edu.ng/), at Kabba Division, Kwara State between 1980 and 1990. The archival version is at the Archive of Sound and Vision at the IAS. For more information, contact [unibadanias60@gmail.com](mailto:unibadanias60@gmail.com).

Soundfile from [UCLA Library Archives of Sound and Vision, Institute of African Studies, University of Ibadan](https://digital.library.ucla.edu/catalog?f%5Bmember_of_collections_ssim%5D%5B%5D=Archive+of+Sound+and+Vision%2C+Institute+of+African+Studies%2C+University+of+Ibadan&sort=title_alpha_numeric_ssort+asc)

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="82-126"' %}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Multiple Choice of Images in a Single View][0033] for more discussion of Choice and an Image context
* [Simplest Manifest - Audio][0002] for use of a single audio resource in a manifest

{% include acronyms.md %}
{% include links.md %}

