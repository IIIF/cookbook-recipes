---
title: Missing Images in a Sequence
id: 283
layout: recipe
tags: [image, presentation]
summary: "Represent a missing image from a paged object in a sequence."
viewers:
 - UV
 - Mirador
 - Glycerine Viewer
topic:
 - image
 - basic
---

## Use Case

You have a paged object, such as a printed book or early manuscript, that has an image missing. You want to include a Canvas in the page flow to acknowledge the missing sequenced image and also to make sure the recto/verso paging functionality isn't thrown off by altogether eschewing a Canvas at the point of the missing image.

## Implementation notes

This recipe attempts to address desires to have a good user experience for people interacting with IIIF resources presented sequentially but lacking one or more images. The recipe also contemplates software consumption of the same. None of the Manifest information described here is required by the [IIIF Presentation API][prezi3], but it may bring benefits to those accessing your work. Nothing in the IIIF Presentation API makes any provision for specifying how or even whether a Canvas replaces what is supposed to appear at that point of the page flow, as the API is agnostic both about your content and its semantics as well as any semantics of your Manifest's structure.

To maintain a sequence presentation of a paged object with missing images, we suggest adding a content-less Canvas with, at a bare minimum, the `id`, `type`, `height`, `width`, and `items` properties. The `items` property would be written as empty specifically to assert there is no image available. In addition, while the spec doesn’t require the presence of `items`, [the IIIF Presentation API Validator](https://presentation-validator.iiif.io/) will fail to validate a Canvas without `items` as it differentiates between Canvas references found in Ranges and Canvas references found not in Ranges by the presence of `items`.

Using an empty Canvas is a very lightweight and authentic way to show missing content. That is, having a content-free Canvas takes modest effort and can represent the lack of content in a real-world object or an error in creating a digital version. However, with only the bare minimum properties neither viewers, nor people interacting with the resources, nor code interacting with it have any indication of why the image is absent. Consequently, as shown in this recipe's Manifest, it's a good idea to make use of the `label` property to contain useful text.

### Additional Information

For a representation of an absent IIIF resource, accessibility to non-visual interactions is particularly important. Using both the minimum suggested properties thoughtfully and additional other properties as the situation demands will be more likely to provide an equitable experience for people with visual disabilities. As an example, note that the `metadata` property can contain as many arbitrary pairs of `label` and `value` as needed to convey accessible information about the missing resource. Note that because viewers are not required to display the metadata in any predictable way or at all, `metadata` content cannot be assumed to be always readable by both visual and non-visual means.

If the best approach is to redirect visitors away from the resource to explain the absence, other Manifest and Canvas properties can be used to provide content pointers to more information about missing image(s). For instance, `homepage` can direct them to a webpage that talks about the object and its physical state.

## Restrictions

No known restrictions.

## Example

For this example, we are using views from a paged Ethiopic manuscript. One verso page has been imagined missing, and represented in the Manifest as discussed above.

{% include manifest_links.html manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="50-77"' %}


# Related recipes

* [Simple Manifest - Book][0009]
* [Linking to Web Page of an Object (`homepage`)][0047]
* [Metadata on Any Resource][0029]


{% include acronyms.md %}
{% include links.md %}
