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

As a person wanting to annotate a IIIF resource, you would like to open a manifest in a viewer not available in the web interface where you first find the resource.

Alternately, as a viewer developer, you would like to allow your viewer to receive dragged-over items.

## Implementation Notes

Implementing this recipe requires a resource provider and a viewer each to implement their part. 

### For Resource Providers

The resource provider must have a draggable item — such as an image — that makes use of the DataTransfer object. It will have a [`dataTransfer.setData` method](https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer) attached to the item's `dragstart` event.

A script implementing such a method for a Manifest could look like the below.
```
<script>
function drag(ev) {
  ev.dataTransfer.setData("text/plain", JSON.stringify({
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": "https://iiif.io/api/cookbook/recipe/0599-drag-and-drop/dnd-manifest",
    "type": "Annotation",
    "motivation": ["contentState"],
    "target": {
      "id": "https://iiif.io/api/cookbook/recipe/0006-text-language/manifest.json",
      "type": "Manifest"
    }
  }));
}
</script>
```

Note that the script forces the manifest content into a string, which the receiving viewer's handling script is  A script implementing such a method for a single Canvas of a Manifest could look like the below. (Noting that there is no likely practical difference from the above since this manifest contains but one Canvas.)
```
<script>
function drag(ev) {
  ev.dataTransfer.setData("text/plain", JSON.stringify({
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": "https://iiif.io/api/cookbook/recipe/0599-drag-and-drop/dnd-manifest",
    "type": "Annotation",
    "motivation": ["contentState"],
    "target": {
      "id": "https://iiif.io/api/cookbook/recipe/0006-text-language/canvas/p1",
      "type": "Canvas",
      "partOf": [{
      	"id": "https://iiif.io/api/cookbook/recipe/0006-text-language/manifest.json",
      	"type": "Manifest"
      }]
    }
  }));
}
</script>
```

### For Viewer Developers

A supporting viewer must have an interface capable of handling the DataTransfer object's data carried by the draggable item in its `drop` event.

## Restrictions

Because implementation is two-part, you may only have control over one half of the ability to drag and drop. Consequently, and since this action is only in a GUI environment, you will need to consider whether visitors to your IIIF interface would benefit from some kind of support text.

Viewer developers will have a special need to consider security when implementing a droppable interface.

## Example

Below is an image of the IIIF logo, decorated with the appropriate JavaScript event handler attributes, and a visible version of the markup for that image, showing the connection to the page script for the `drag` event. For a supporting viewer, the IIIF logo image below could be dragged onto its viewing area and dropped, which would result in the viewer retrieving the manifest for the IIIF Cookbook recipe titled ["Internationalization and Multi-language Values"][0006].

No viewers currently support this approach to dragging and dropping a manifest.

<img src="logo-sm.png" draggable="true" ondragstart="drag(event)" alt="IIIF logo; drag and drop onto a supporting viewer to see this resource in that viewer">

```
<img src="logo-sm.png" draggable="true" ondragstart="drag(event)" alt="IIIF logo; drag and drop onto a supporting viewer to see this resource in that viewer">
```

<script>
function drag(ev) {
  ev.dataTransfer.setData("text/plain", JSON.stringify({
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": "https://iiif.io/api/cookbook/recipe/0599-drag-and-drop/dnd-manifest",
    "type": "Annotation",
    "motivation": ["contentState"],
    "target": {
      "id": "https://iiif.io/api/cookbook/recipe/0006-text-language/manifest.json",
      "type": "Manifest"
    }
  }));
}
</script>

## Related Recipes

Provide a bulleted list of related recipes and why they are relevant.

{% include acronyms.md %}
{% include links.md %}
