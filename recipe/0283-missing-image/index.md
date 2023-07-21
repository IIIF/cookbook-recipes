---
title: Missing Images in a Sequence
id: 283
layout: recipe
tags: [image, presentation]
summary: "Represent a missing image from a paged object in a sequence."
viewers:
 - UV
 - Mirador
 - Annona
 - Clover
topic:
 - image
 - basic
---

## Use Case

You have a paged object, such as a printed book or early manuscript, that has an image missing. You want to include a Canvas with some content to alert the user to the missing image and also to make sure the recto/verso paging functionality isn't thrown off by eschewing an image altogether.


## Implementation notes



## Example

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="50-81"' %}


# Related recipes

* [Simple Manifest - Book][0009]

{% include acronyms.md %}
{% include links.md %}
