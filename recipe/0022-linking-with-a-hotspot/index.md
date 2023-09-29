---
title: Redirecting from one Canvas to another resource (Hotspot linking)
id: 22
layout: recipe
tags: [annotation]
summary: "Link a portion of a Canvas to another resource. "
viewers:
topic: annotation
code:
---

## Use Case

You want to be able to click on a region of an image and being redirected to another resource.
In an image showing multiple objects or parts, you want to see a detailed version of the content of the annotated part. You have digitized a table of contents and you want the user to be able to click on the area of sections and be redirected to page it is pointing at.


## Implementation Notes

The create the annotation, we create an Annotation inside an AnnotationPage
To select the area we want to link to a specific resource we set the target using the link of the Canvas and a fragment as in [Simple Annotation — Tagging][0021], however, in this case, the `motivation` of the annotation is `linking`.

In the case the link is between a region of a Canvas and another Canvas in a Manifest, the `body` contains a SpecificResource with `source` attribute set to the Canvas we want to link.
The `partOf` attribute of the Canvas must point to the Manifest containing the Canvas and have the same `id`.
The `partOf` attribute must be present even when the Canvas is part of the same Manifest, in this way when the manifest is consumed it is always possible to identify where the Canvas is contained.

In the case the link is between a region of a Canvas and and an external resource it is recommended to add the correct type as indicated in the [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/#h-accessibility-of-content), for instance:

```json
{
    "id": "http://example.org/website1",
    "type": "Text"
  }
```

The implementer could consider adding also a Textual Body to the annotation to give more context to the end-user.


## Restrictions

None known.

## Example

In this Manifest, we use a photograph of Göttingen from the 2019 IIIF annual conference the annotation is tagging the fountain. In the same Manifest there is a Canvas with a picture of a close up of the fountain.
We link the Annotation of the fountain with the Canvas containing its close up adding a second body to the Annotation.
The body contains a Specific Resource that has the `id` of the Canvas containing the close up of the fountains as `source` and the id of the Manifest in the `partOf` attribute.


{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="49-75"' %}

## Related Recipes

* [Simple Annotation — Tagging][0021] a simple annotation pointing to a region of an image.

{% include acronyms.md %}
{% include links.md %}

