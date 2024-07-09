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

You want to be able to click on a region of an image and be redirected to another resource.
For example, in an image showing multiple objects or parts, you want to see a detailed version of the content of the annotated part. As another possibility, you have digitized a table of contents and you want the user to be able to click on a chapter entry and be redirected to the correct place.


## Implementation Notes

To create the annotation, we use an Annotation inside an AnnotationPage.
To select the area we want to link to a specific resource we set the `target` using the Canvas `id` and a fragment, as in [Simple Annotation — Tagging][0021]. However, in this case, the `motivation` of the annotation is `linking`.

When the link is between a region of a Canvas and another Canvas in a Manifest, the `body` contains a SpecificResource with `source` property set to the Canvas we want to link.
The `partOf` property of the Canvas must point to the Manifest containing the Canvas and have the same `id`.
The `partOf` property must be present even when the Canvas is part of the same Manifest, in this way, when the manifest is consumed, it is always possible to identify where the Canvas is contained.

When the link is between a region of a Canvas and an external resource it is recommended to add the correct type as indicated in the [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/#classes), for instance:

```json
{
  "id": "https://example.com/annotation/p0002-link",
  "type": "Annotation",
  "motivation": "linking",
  "body": [
    {
    "id": "https://example.com/website1",
    "type": "Text"
    }
  ],
  "target": "https://example.com/canvas/p1#xywh=265,661,1260,1239"
}
```

The implementer could also consider adding a TextualBody to the annotation to give more context to the end-user.
The `value` of the Textual Body should describe the `target` (not the `body` of the Annotation) so that the user can understand what resource will be opened when clicking on the Annotation area.


## Restrictions

None known.

## Example

In this Manifest, we use a photograph of Göttingen from the 2019 IIIF annual conference, where the annotation tags the fountain. In the same Manifest there is a Canvas with a picture of a close-up of the fountain.
We link the Annotation of the fountain to the Canvas containing its close-up by adding a second body to the Annotation.
The body contains a Specific Resource with the `id` of the Canvas containing the close-up of the fountain as `source` and the `id` of the Manifest in the `partOf` property.


{% include manifest_links.html viewers="Theseus" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="49-75"' %}

## Related Recipes

* [Simple Annotation — Tagging][0021] a simple annotation pointing to a region of an image.

{% include acronyms.md %}
{% include links.md %}
