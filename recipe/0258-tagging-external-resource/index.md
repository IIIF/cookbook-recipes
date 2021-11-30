---
title: Tagging with an External Resource
id: 258
layout: recipe
tags: annotation
summary: "Connect a tagging annotation to an external resource"
---

## Use Case

When you annotate a resource with a tag, you'd like to connect that tag to an external source, whether an authority file, a linked data node, or something else that represents unambiguously some data you want to associate with the annotated resource.

## Implementation Notes
The [IIIF Presentation 3.0 API][prezi3] does not itself discuss linking to external web resources in annotations, incorporating them from the [W3C Web Annotation Data Model](http://w3.org/TR/annotation-model/) by reference. For a full description of this and other portions of the data model used in IIIF annotations, we recommend you read that document.

In order to make possible a link between the IIIF resource and an external web resource, the pertinent Annotation must have at least a `body` that is a Specific Resource whose `source` property contains the appropriate URI as its value. That `source` value must resolve, that is, it must be a real URI at the time of the creation of the Annoation.

Finally, be sure you are writing valid value forms in your Annotation. In the Web Annotation data model, there are different patterns for the `value` property, when used within an Annotation. The `value` of a `TextualBody` or a `FragmentSelector`, for example, are strings rather than JSON objects. See also [the Presentation API v3.0](https://iiif.io/api/presentation/3.0/#56-annotation).

## Restrictions

None known.

## Example

In this example, we continue our use of this photograph of a square in Göttingen, Germany, which includes a fountain topped by a sculpture of a girl and 2 accompanying geese. In addition to tagging the fountain with text giving its name, we are adding for this recipe an additional Annotation `body` that points to the Wikidata entry for the fountain.

Using multiple `body` properties, as shown here, does not have any predictable consequences for a viewer's handling of the data. With this in mind, each `body` in this Manifest could stand alone.

Because each `body` is used for tagging, we have put that as the value of the `motivation` property on the Annotation rather than making use of the Specific Resource's `purpose` property.

No viewers currently implement this tagging approach.

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config="data-line='44–68'"%}

The direct link to the fixture is a useful convenience.

## Related Recipes

* [Simplest Annotation][0266]
* [Simple Annotation — Tagging][0021]

{% include links.md %}

