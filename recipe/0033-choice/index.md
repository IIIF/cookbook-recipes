---
title: Choice (simplest)
id: 33
layout: recipe
tags: [tbc]
summary: "tbc"
---


## Use Case

There are multiple images available for a given View (Canvas). For example, a painting has been photographed in 10 different wavelengths of light. The images are _registered_ - that is, they all line up.

(put a picture here!)

Another example would be a  manuscript page with a flap or foldout; there are two registered images of the page available, one with the flap closed and one with it open. The page also has a transcription which is independent of either of these two images, because the annotations target the canvas.

In both cases the images are all of the same thing, they all align, or can be aligned, with the same canvas.

Users should be able to choose which of the multiple images they want to view.
Client implementations should understand that the intent is to offer the user a choice between 2 or more images. Any one image is as valid as another, and the user can switch between them, but the publisher can expect that clients will all start with the same image showing.

Clients anticipating likely uses of this model may wish to provide more sophisticated choice UIs. For example a tool used in the study of artworks may have more sophisticated blending features or other manipluations of the images [Mirador has this]

This pattern is important because it is not uncommon, especially for artworks, for more than one image to be available.


## Implementation notes

The implementation is basically the same as the simplest IIIF use case (link to example 1), except that the body of the annotation isn't an image resource directly, but a resource of type Choice. This is defined in the W3C Web Annotation Data Model:

> Definition of choice

Our multiple images are now values of the choice body.

[Add this bit after doing the multiple images example]
This pattern may be used in conjunction with multiple images (link to other example) - a canvas could have multiple images, multiple Choice resources, or combinations.
[This requires clients to be careful, and be systematic, about handling direct and choice resources]


## Restrictions

Not all IIIF clients will recognise Choice.
Clients need to consider generalised handling of multiple choices and multiple resources.
Clients that don't wish to offer a Choice UI should at least understand the construction and just take the first.

## Example

[JSON-LD](manifest.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}

