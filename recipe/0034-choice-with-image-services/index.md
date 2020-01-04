---
title: Choice - multispectral flavoured example, with image services
id: 34
layout: recipe
tags: [multiple-images]
summary: "How to model multiple choices of images for the same view - e.g., layers, multispectral images - with image services."
---


## Use Case

This recipe is identical to the previous recipe, [Choice](../0033-choice/), except that the provided example includes IIIF Image API Services for the image choices. 

## Implementation notes

Please refer to [Choice](../0033-choice/) for the full discussion. Note that in the IIIF Manifest below, the linked image services implement version 2.1 of the Image API, therefore they use `@id` and `@type`. See the description for `service` in the [Presentation 3 API][prezi3].

## Example

[JSON-LD](manifest.json)

{: .line-numbers data-download-link data-download-link-label="Download me" data-src="manifest.json" }
```json
```

# Related recipes

* [Choice](../0033-choice/). This is the same as this example, but without the image service (only static images are used).
* [Foldouts](../0035-foldouts/). In the example above, `Choice` is appropriate because the two images are the same view and are aligned. For, say, a map in a book that folds out to a much bigger view, the unfolded version would be a different `Canvas`, because it does not represent the same spatial view. This is one reason to offer two separate views rather than a choice of resources within one view.
* [Composition of one view from multiple image sources](../0036-composition-from-multiple-images/). Care should be taken not to confuse _composition_ with the current recipe. Both involve multiple images, but composition is for building a scene from multiple images (and possibly other resources), where there is no requirement to offer the user choices _between_ those images.

{% include acronyms.md %}
{% include links.md %}

