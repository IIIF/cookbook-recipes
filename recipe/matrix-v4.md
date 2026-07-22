---
title: Viewer Matrix V4
layout: spec
breadcrumbs:
  - label: IIIF Cookbook
    link: index.html
viewers:
  - Mirador
  - UV
  - Annona
  - Clover
  - Aviary
  - Theseus
  - TIFY
  - Triiiceratops
  - Voyager
  - Kompakkt
topics:
  - basic
  - property
  - structure
  - image
  - key: AV
    note: Please note there are other IIIF AV viewers that are not listed like the [Europeana Player](https://github.com/europeana/media-player). These are not included in the matrix due to a lack of public linkable instance rather than them not supporting some of the recipes.
  - 3d
  - annotation
  - key: content-state
    note: These recipes demonstrate use cases for the [content-state](https://iiif.io/api/content-state/) API. 
  - key: geo-recipes
    note: Please note there are many viewers built to view GeoJSON like [Leaflet](https://leafletjs.com/) and [geojson.io](https://geojson.io/), but they are not able to parse objects for a `navPlace` property or look into the `body` property of Annotations for GeoJSON. However, they are easily customizable and can be made to find GeoJSON in these properties. The Navplace Viewer is an [Open Source customization](https://github.com/CenterForDigitalHumanities/navplace-viewer) of Leaflet that intelligently gathers and formats GeoJSON from provided IIIF resources and hands that GeoJSON to a Leaflet viewer for rendering.
---

<link rel='stylesheet' href="{{ site.cookbook_url | absolute_url }}/css/style.css"/>

# IIIF 4.0 Viewer Matrix

In the 2021 Working meeting there was a presentation on viewer support for IIIF Presentation 3.0. The community asked if this presentation could be turned into a matrix so people can see which viewers support which area(s) of the IIIF specifications. This matrix, shown below, is generated automatically from the latest version of cookbook recipes approved by the IIIF TRC. If you notice an error or inaccuracy, please report it as an Issue at the [cookbook GitHub site](https://github.com/IIIF/cookbook-recipes/issues/new).

## Which viewers are included?

Currently [Mirador](https://projectmirador.org/), the [Universal Viewer](https://universalviewer.io/) (UV) V3, [Clover](https://samvera-labs.github.io/clover-iiif/),  [Aviary](https://iiif.aviaryplatform.com/), [Theseus](https://theseusviewer.org/), [TIFY](https://tify.rocks/) and [Triiiceratops](https://d-flood.github.io/triiiceratops/) are listed on the cookbook. We welcome the addition of other IIIF viewers, but they must support the following features:

- Support for the [IIIF version 4.0 Presentation API](https://iiif.io/api/presentation/4.0/)
- A public, linkable instance, ideally using the `iiif-content` parameter from the [IIIF Content State API](https://iiif.io/api/content-state/)
- Support at least 1 cookbook recipe

## Viewer Matrix

The possible values for viewer support are Yes - ![Yes][YES]{:title="Yes"}, No - ![No][NO]{:title="No"} or Partial - ![Partial][PARTIAL]{:title="Partial"}. Click on the recipe name to see links to supporting viewers' behaviour with the recipe manifest. This will allow you to see whether it achieves the required function in the way you expect.
{% for topic in page.topics  %}
{% if topic.key %}
{% assign topic_key = topic.key %}
{% else %}
{% assign topic_key = topic %}
{% endif %}

{% assign topic_matches = site.pages | where_exp: "recipe", "recipe.topic == topic_key or recipe.topic contains topic_key" %}
{% assign recipes = topic_matches | where_exp: "recipe", "recipe.id != -1 and recipe['v4-viewers']" %}
{% assign sorted = recipes | sort: "id" %}

{% if sorted.size > 0 %}

### {{ site.data.topics[topic_key].label }}

{{ topic.note }}

<table class="viewer">
    <tr>
        <th class="scrolling-header">Recipe</th>
        {% for viewer in page.viewers %}
            <th class="scrolling-header">{{ viewer }}</th>
        {% endfor %}
    </tr>
{% for recipe in sorted %}
    <tr>
        <td><a href="{{ site.cookbook_url | absolute_url }}{{ recipe.url }}#version-4">{{recipe.title}}{% if recipe.property%} ({{recipe.property}}){%endif%}</a></td>
        {% for viewer in page.viewers %}
            {% assign current = recipe['v4-viewers'] | where: "id",viewer | first %}
            <td width="100px">
                {% if current.id == viewer %}
                    {% if current.support == "full" %}
                        <img src="{{ site.cookbook_url | absolute_url }}/assets/images/icons/yes.png" alt="Yes" title="Yes" />
                    {% else if current.support == "partial" %}
                        <img src="{{ site.cookbook_url | absolute_url }}/assets/images/icons/partial.png" alt="Partial" title="Partial" />b
                    {% else %}
                        <img src="{{ site.cookbook_url | absolute_url }}/assets/images/icons/yes.png" alt="Yes" title="Yes" />
                    {% endif %}
                {% else %}
                    {% if recipe['v4-viewers'] contains viewer %} 
                        <img src="{{ site.cookbook_url | absolute_url }}/assets/images/icons/yes.png" alt="Yes" title="Yes" />
                    {% else %}    
                        <img src="{{ site.cookbook_url | absolute_url }}/assets/images/icons/no.png" alt="No" title="No" />
                    {% endif %}
                {% endif %}
            </td>
        {% endfor %}
    </tr>
{% endfor %}
</table>
{% endif %}
{% endfor %}

[YES]: {{ site.cookbook_url | absolute_url }}/assets/images/icons/yes.png
[NO]: {{ site.cookbook_url | absolute_url }}/assets/images/icons/no.png
[PARTIAL]: {{ site.cookbook_url | absolute_url }}/assets/images/icons/partial.png
