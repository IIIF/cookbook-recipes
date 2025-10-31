---
title: Name of Recipe
id: -1
layout: recipe
tags: [tbc]
summary: "tbc"
viewers:
topic:
 - basic
---

## Use Case

As a person wanting to annotate a IIIF resource, you would like to open a manifest in a viewer not present or available in the web interface where you first find the resource.

## Implementation Notes

What do you need to know to use this pattern?
How do you implement the pattern?

## Restrictions

Implementing this recipe requires a resource provider and a viewer provider each to implement their part. The resource provider must have a draggable item that can have a `dataTransfer.setData` method attached to the item's `dragstart` event and the viewer provider must have an interface capable of handling the data in its `drop` event.

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="" manifest="manifest.json" %}

<img src="https://iiif.io/api/cookbook/assets/images/logos/logo-sm.png" draggable="true" ondragstart="drag(event)" alt="IIIF logo; drag and drop onto a supporting viewer to see this resource in that viewer">

<script>
   function drag(ev) {
            ev.dataTransfer.setData("text/plain", {
                 "@context": "http://iiif.io/api/presentation/3/context.json",
                 "id": "https://example.org/content-states/1",
                 "type": "Annotation",
                 "motivation": ["contentState"],
                 "target": {
                    "id": "https://iiif.io/api/cookbook/recipe/0006-text-language/manifest.json",
                    "type": "Manifest"
                }
      });
   }
</script>

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}
