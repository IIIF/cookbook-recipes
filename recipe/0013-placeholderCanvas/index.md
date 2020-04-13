---
title: "Posters: placeholderCanvas"
id: 13
layout: recipe
tags: video, audio, image, av
summary: "I wish to provide the user with something to look at before they choose to start interacting with the object, and/or while they wait for it to load/buffer."
---

## Use Case

I wish to provide the user with something to look at before they choose to start interacting with the object, and/or while they wait for it to load/buffer.

## Implementation notes

For this value, it's particularly important to note the latitude given conforming clients. The spec only says that clients _may_ render the `placeholderCanvas` property, not _must_.

Note also the differences between this property and the `accompanyingCanvas` property. This property provides content to render before the main content is rendered 

How does one implement the pattern?

See also [https://github.com/IIIF/trc/issues/8](https://github.com/IIIF/trc/issues/8), [https://github.com/IIIF/api/issues/1605](https://github.com/IIIF/api/issues/1605)


## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.? (Not present if not needed.)

## Example

Describe in prose and provide examples, e.g.: 

[JSON-LD](manifest.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}

