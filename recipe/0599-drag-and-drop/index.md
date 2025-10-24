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

Describe the use case that the pattern is intended to solve.
Why is this pattern important?

## Implementation Notes

What do you need to know to use this pattern?
How do you implement the pattern?

## Restrictions

When is this pattern is usable / not usable? Is it deprecated? If it uses multiple specifications, which versions are needed, etc.?

Delete this section if it is not needed.
If you don't know what the restrictions might be initially, just leave the following line:
**Unknown - Help Needed**

## Example

Describe the solution in prose and provide an example.
The example json document must be an external document, and imported with the following:

{% include manifest_links.html viewers="" manifest="manifest.json" %}

<img src="https://collections.library.yale.edu/assets/iiif-ca042537b7cca44f9a22d3960ae9e3a8d990bc6e442b1376b928d7c79ab353c9.png" draggable="true" ondragstart="drag(event)" alt="IIIF logo; drag and drop onto a supporting viewer to see this resource in that viewer">

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
