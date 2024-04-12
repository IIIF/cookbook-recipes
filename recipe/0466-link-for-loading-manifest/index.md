---
title: Loading a manifest with a viewer using a link
id: 466
layout: recipe
tags: [annotation]
summary: "Allows users to use links that can be clicked to open a viewer with a selected manifest."
viewers:
  - Mirador
  - Clover
topic:
 - content-state
---

## Use Case

You want to generate a link that you can use to open a Manifest using a specific Viewer. For instance, in your web page, you want to allow the user to click on a link that opens Mirador and a Manifest of a book relevant to the page.

## Implementation Notes

This request can be implemented in a standardized manner using the [IIIF Content State API](https://iiif.io/api/content-state) in particular following the [HTTP GET (Query String) Parameter section](https://iiif.io/api/content-state/1.0/#initialization-mechanisms-link).


The link of the Manifest to be opened with the viewer should be provided as the value of `iiif-content` parameter of the viewer URL.

## Example

We want to create an hyperlink to open the Manifest available at the following link https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json using a viewer available at  the following page https://example.org/viewer. We can pass as the value of the query parameter `iiif-content` of the viewer landing page the Manifest URL:
```html
https://example.org/viewer?iiif-content=https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json
```

Eventually, we can create an anchor tag with the link as the `href` attribute to use in the web page:

```html
<a href="https://example.org/viewer?iiif-content=https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json">Link for visualizing the manifest using a viewer.</a>
```

**Mirador**:
[https://projectmirador.org/embed/?iiif-content=https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json](https://projectmirador.org/embed/?iiif-content=https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json)

**Clover**:
[https://samvera-labs.github.io/clover-iiif/docs/viewer/demo?iiif-content=https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json](https://samvera-labs.github.io/clover-iiif/docs/viewer/demo?iiif-content=https://iiif.io/api/cookbook/recipe/0001-mvm-image/manifest.json)

## Related Recipes

* [Simplest Manifest - Image][0001] shows the basic structure of a IIIF Manifest using presentation API 3.0.

{% include acronyms.md %}
{% include links.md %}

