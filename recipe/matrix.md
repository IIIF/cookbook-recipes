---
title: Viewer Matrix
layout: spec
breadcrumbs:
  - label: IIIF Cookbook
    link: index.html
viewers:
  - Mirador
  - UV
  - Annona
  - Clover
  - Navplace Viewer
  - Ramp
  - Aviary
  - Glycerine Viewer
topics:
  - basic
  - property
  - structure
  - image
  - key: AV
    note: Please note there are other IIIF AV viewers that are not listed like the [Europeana Player](https://github.com/europeana/media-player). These are not included in the matrix due to a lack of public linkable instance rather than them not supporting some of the recipes.
  - annotation
  - key: content-state
    note: These recipes demonstrate use cases for the [content-state](https://iiif.io/api/content-state/) API. 
  - key: geo-recipes
    note: Please note there are many viewers built to view GeoJSON like [Leaflet](https://leafletjs.com/) and [geojson.io](https://geojson.io/), but they are not able to parse objects for a `navPlace` property or look into the `body` property of Annotations for GeoJSON. However, they are easily customizable and can be made to find GeoJSON in these properties. The Navplace Viewer is an [Open Source customization](https://github.com/CenterForDigitalHumanities/navplace-viewer) of Leaflet that intelligently gathers and formats GeoJSON from provided IIIF resources and hands that GeoJSON to a Leaflet viewer for rendering.
---

<link rel='stylesheet' href="{{ site.cookbook_url | absolute_url }}/css/style.css"/>

# IIIF 3.0 Viewer Matrix

In the 2021 Working meeting there was a presentation on viewer support for IIIF Presentation 3.0. The community asked if this presentation could be turned into a matrix so people can see which viewers support which area(s) of the IIIF specifications. This matrix, shown below, is generated automatically from the latest version of cookbook recipes approved by the IIIF TRC. If you notice an error or inaccuracy, please report it as an Issue at the [cookbook GitHub site](https://github.com/IIIF/cookbook-recipes/issues/new).

## Which viewers are included?

Currently [Mirador 3](https://projectmirador.org/), the [Universal Viewer](https://universalviewer.io/) (UV) V3, [Annona](https://ncsu-libraries.github.io/annona/multistoryboard/), [Clover](https://samvera-labs.github.io/clover-iiif/), [Navplace Viewer](https://map.rerum.io/), [Ramp](https://iiif-react-media-player.netlify.app/), [Aviary](https://iiif.aviaryplatform.com/), and [Glycerine](https://demo.viewer.glycerine.io/) are listed on the cookbook and we welcome the addition of other IIIF viewers but they must support the following features:

- Support for the [IIIF version 3.0 Presentation API](https://iiif.io/api/presentation/3.0/)
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

### {{ site.data.topics[topic_key].label }}

{{ topic.note }}
{% assign recipes = site.pages | where_exp: "recipe", "recipe.topic == topic_key or recipe.topic contains topic_key and recipe.id != -1" %}
{% assign sorted = recipes | sort: "id" %}

<table class="viewer">
    <tr>
        <th>Recipe</th>
        {% for viewer in page.viewers %}
            <th>{{ viewer }}</th>
        {% endfor %}
    </tr>    
{% for recipe in sorted %}
    <tr>
        <td><a href="{{ site.cookbook_url | absolute_url }}{{ recipe.url }}">{{recipe.title}}{% if recipe.property%} ({{recipe.property}}){%endif%}</a></td>
        {% for viewer in page.viewers %}
            {% assign current = recipe.viewers | where: "id",viewer | first %}
            <td width="100px">
                {% if current.id == viewer %}
                    {% if current.support == "full" %}
                        <img src="{{ site.cookbook_url | absolute_url }}/assets/images/icons/yes.png" alt="Yes" title="Yes" />
                    {% else if current.support == "partial" %}
                        <img src="{{ site.cookbook_url | absolute_url }}/assets/images/icons/partial.png" alt="Partial" title="Partial" />
                    {% else %}
                        <img src="{{ site.cookbook_url | absolute_url }}/assets/images/icons/yes.png" alt="Yes" title="Yes" />
                    {% endif %}
                {% else %}
                    {% if recipe.viewers contains viewer %} 
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
{% endfor %}

[YES]: {{ site.cookbook_url | absolute_url }}/assets/images/icons/yes.png
[NO]: {{ site.cookbook_url | absolute_url }}/assets/images/icons/no.png
[PARTIAL]: {{ site.cookbook_url | absolute_url }}/assets/images/icons/partial.png