---
title: Missing images in a sequence
id: 283
layout: recipe
tags: [image, presentation]
summary: "Represent a missing image from a paged object in a sequence."
viewers:
 - UV
 - Mirador  
topic:
 - image
---

## Use Case

You have a paged object, such as a printed book or early manuscript, which has an image missing. You want to included a canvas with some content to show the user that there should/could be an image there and also make sure the recto/verso paged functionality isn't thrown due to this missing image.


## Implementation notes



## Example

{% include manifest_links.html viewers="UV, Mirador" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}


# Related recipes

* [Simple Manifest - Book][0009]

{% include acronyms.md %}
{% include links.md %}
