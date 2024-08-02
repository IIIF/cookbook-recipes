---
title: Open a specific region of a canvas in a viewer
id: 485
layout: recipe
tags: [annotation]
summary: "Allows users to use content state API to open a specific region of a canvas by means of supported viewers."
viewers:
  - Mirador
  - Clover
topic:
 - content-state
---

## Use Case

I want to share a link to highlight a detail in a specific region of an image. I want to share a portion of a digitized manuscript text allowing the user an easy access to the rest of the manuscript.

Institutions might want to use this recipe for sharing portions of their object through social media allowing a direct link to the viewer for improving the users interaction with the digitized content. A scholar who finds a relevant passage on a manuscript might want to share the precise location with other colleagues, allowing them to check the original source.

## Implementation Notes

To implement this feature we must create a request to an entry point of a viewer instance with the necessary information for the viewer to open the Manifest, retrive the Canvas and set the viewport to the desired region.

[Image API](https://iiif.io/api/image/3.0/#41-region) allows users to share a specific region of an image, however, the context from which the region is extracted is not easily accessible. Instead, sharing a link to a open the specific region with a viewer allows the users to explore other part of the image or related content and metadata present in the Manifest. [link to other recipe]

This request can be implemented in a standardized manner using the [IIIF Content State API](https://iiif.io/api/content-state), providing the data as values of the `iiif-content` query string parameter as explained in the [API section](https://iiif.io/api/content-state/1.0/#initialization-mechanisms-link).

We can use the [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) to encode the information necessary, as shown in [A Region of a Canvas in a Manifest](https://iiif.io/api/content-state/1.0/#51-a-region-of-a-canvas-in-a-manifest) section of the standard.

However, before passing the data as a query parameter we must encode it as explained in the https://iiif.io/api/content-state/1.0/#6-content-state-encoding.


## Example
In this example we want to highlight a portion of an image contained in a book.

We will use the following manifest shown in the Simple Manifest -Book recipe which is available at the following link: [https://iiif.io/api/cookbook/recipe/0009-book-1/manifest.json](https://iiif.io/api/cookbook/recipe/0009-book-1/manifest.json)

We want to open the viewport to a specific region of a canvas using a viewer available at the following page https://example.org/viewer.

First we create an Annotation:

```
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.org/import/1",
  "type": "Annotation",
  "motivation": ["contentState"],
  "target": {
     "id": "https://iiif.io/api/cookbook/recipe/0009-book-1/canvas/p2#xywh=1528,3024,344,408",
     "type": "Canvas",
     "partOf": [{
        "id": "https://iiif.io/api/cookbook/recipe/0009-book-1/manifest.json",
        "type": "Manifest"
     }]
   }
}
```

We can create an Annotation with `motivation` set to `contentState` and a target `type` set to Canvas the `id` of the target will contain a fragment selector with the coordinates of the canvas we want to share, and a `partOf` element containing the `id` of the Manifest containing the Canvas.

We can now use one of the methods listed in the [examples of content state encoding section](https://iiif.io/api/content-state/1.0/#63-examples-of-content-state-encoding) to generate a base64url string (**note: we removed new lines characters and white spaces for brevity before computing the base64url**).

We can pass as the encoded value using the query parameter `iiif-content` of the viewer landing page the Manifest URL:
```html
https://example.org/viewer?iiif-content=JTdCJTIyJTQwY29udGV4dCUyMiUzQSUyMmh0dHAlM0ElMkYlMkZpaWlmLmlvJTJGYXBpJTJGcHJlc2VudGF0aW9uJTJGMyUyRmNvbnRleHQuanNvbiUyMiUyQyUyMmlkJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZleGFtcGxlLm9yZyUyRmltcG9ydCUyRjElMjIlMkMlMjJ0eXBlJTIyJTNBJTIyQW5ub3RhdGlvbiUyMiUyQyUyMm1vdGl2YXRpb24lMjIlM0ElNUIlMjJjb250ZW50U3RhdGUlMjIlNUQlMkMlMjJ0YXJnZXQlMjIlM0ElN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZjYW52YXMlMkZwMiUyM3h5d2glM0QxNTI4JTJDMzAyNCUyQzM0NCUyQzQwOCUyMiUyQyUyMnR5cGUlMjIlM0ElMjJDYW52YXMlMjIlMkMlMjJwYXJ0T2YlMjIlM0ElNUIlN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZtYW5pZmVzdC5qc29uJTIyJTJDJTIydHlwZSUyMiUzQSUyMk1hbmlmZXN0JTIyJTdEJTVEJTdEJTdE
```

Eventually, we can create an anchor tag with the link as the `href` attribute to use in the web page:

```html
<a href="https://example.org/viewer?iiif-content=JTdCJTIyJTQwY29udGV4dCUyMiUzQSUyMmh0dHAlM0ElMkYlMkZpaWlmLmlvJTJGYXBpJTJGcHJlc2VudGF0aW9uJTJGMyUyRmNvbnRleHQuanNvbiUyMiUyQyUyMmlkJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZleGFtcGxlLm9yZyUyRmltcG9ydCUyRjElMjIlMkMlMjJ0eXBlJTIyJTNBJTIyQW5ub3RhdGlvbiUyMiUyQyUyMm1vdGl2YXRpb24lMjIlM0ElNUIlMjJjb250ZW50U3RhdGUlMjIlNUQlMkMlMjJ0YXJnZXQlMjIlM0ElN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZjYW52YXMlMkZwMiUyM3h5d2glM0QxNTI4JTJDMzAyNCUyQzM0NCUyQzQwOCUyMiUyQyUyMnR5cGUlMjIlM0ElMjJDYW52YXMlMjIlMkMlMjJwYXJ0T2YlMjIlM0ElNUIlN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZtYW5pZmVzdC5qc29uJTIyJTJDJTIydHlwZSUyMiUzQSUyMk1hbmlmZXN0JTIyJTdEJTVEJTdEJTdE">Link for visualizing the region of a Canvas using a viewer.</a>
```

**Mirador**:
Link of the viewer: https://projectmirador.org/embed

Complete link: https://projectmirador.org/embed/?iiif-content=JTdCJTIyJTQwY29udGV4dCUyMiUzQSUyMmh0dHAlM0ElMkYlMkZpaWlmLmlvJTJGYXBpJTJGcHJlc2VudGF0aW9uJTJGMyUyRmNvbnRleHQuanNvbiUyMiUyQyUyMmlkJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZleGFtcGxlLm9yZyUyRmltcG9ydCUyRjElMjIlMkMlMjJ0eXBlJTIyJTNBJTIyQW5ub3RhdGlvbiUyMiUyQyUyMm1vdGl2YXRpb24lMjIlM0ElNUIlMjJjb250ZW50U3RhdGUlMjIlNUQlMkMlMjJ0YXJnZXQlMjIlM0ElN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZjYW52YXMlMkZwMiUyM3h5d2glM0QxNTI4JTJDMzAyNCUyQzM0NCUyQzQwOCUyMiUyQyUyMnR5cGUlMjIlM0ElMjJDYW52YXMlMjIlMkMlMjJwYXJ0T2YlMjIlM0ElNUIlN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZtYW5pZmVzdC5qc29uJTIyJTJDJTIydHlwZSUyMiUzQSUyMk1hbmlmZXN0JTIyJTdEJTVEJTdEJTdE

**Clover**:
https://samvera-labs.github.io/clover-iiif/docs/viewer/demo?iiif-content=JTdCJTIyJTQwY29udGV4dCUyMiUzQSUyMmh0dHAlM0ElMkYlMkZpaWlmLmlvJTJGYXBpJTJGcHJlc2VudGF0aW9uJTJGMyUyRmNvbnRleHQuanNvbiUyMiUyQyUyMmlkJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZleGFtcGxlLm9yZyUyRmltcG9ydCUyRjElMjIlMkMlMjJ0eXBlJTIyJTNBJTIyQW5ub3RhdGlvbiUyMiUyQyUyMm1vdGl2YXRpb24lMjIlM0ElNUIlMjJjb250ZW50U3RhdGUlMjIlNUQlMkMlMjJ0YXJnZXQlMjIlM0ElN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZjYW52YXMlMkZwMiUyM3h5d2glM0QxNTI4JTJDMzAyNCUyQzM0NCUyQzQwOCUyMiUyQyUyMnR5cGUlMjIlM0ElMjJDYW52YXMlMjIlMkMlMjJwYXJ0T2YlMjIlM0ElNUIlN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZtYW5pZmVzdC5qc29uJTIyJTJDJTIydHlwZSUyMiUzQSUyMk1hbmlmZXN0JTIyJTdEJTVEJTdEJTdE

**Glycerine**

https://demo.viewer.glycerine.io/viewer?iiif-content=iiif-content=JTdCJTIyJTQwY29udGV4dCUyMiUzQSUyMmh0dHAlM0ElMkYlMkZpaWlmLmlvJTJGYXBpJTJGcHJlc2VudGF0aW9uJTJGMyUyRmNvbnRleHQuanNvbiUyMiUyQyUyMmlkJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZleGFtcGxlLm9yZyUyRmltcG9ydCUyRjElMjIlMkMlMjJ0eXBlJTIyJTNBJTIyQW5ub3RhdGlvbiUyMiUyQyUyMm1vdGl2YXRpb24lMjIlM0ElNUIlMjJjb250ZW50U3RhdGUlMjIlNUQlMkMlMjJ0YXJnZXQlMjIlM0ElN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZjYW52YXMlMkZwMiUyM3h5d2glM0QxNTI4JTJDMzAyNCUyQzM0NCUyQzQwOCUyMiUyQyUyMnR5cGUlMjIlM0ElMjJDYW52YXMlMjIlMkMlMjJwYXJ0T2YlMjIlM0ElNUIlN0IlMjJpZCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGaWlpZi5pbyUyRmFwaSUyRmNvb2tib29rJTJGcmVjaXBlJTJGMDAwOS1ib29rLTElMkZtYW5pZmVzdC5qc29uJTIyJTJDJTIydHlwZSUyMiUzQSUyMk1hbmlmZXN0JTIyJTdEJTVEJTdEJTdE

## Related Recipes

* [Simplest Manifest - Image][0001] shows the basic structure of a IIIF Manifest using presentation API 3.0.
* [A simple book][0009] shows the manifest structure.
* [Link for loading a manifest][0466] another example of content state API.



{% include acronyms.md %}
{% include links.md %}

