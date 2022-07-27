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
topics:
 - basic
 - property
 - structure  
 - image
 - key: AV
   note: Please note there are other IIIF AV viewers that are not listed like the [Europeana Player](https://github.com/europeana/media-player) and the [iiif-react-media-player](https://samvera-labs.github.io/iiif-react-media-player/). These are not included in the matrix due to a lack of public linkable instance rather than them not supporting some of the recipes. 
 - annotation
 - geo-recipes
---

<link rel='stylesheet' href="{{ site.cookbook_url | absolute_url }}/css/style.css"/>

# IIIF 3.0 Viewer Matrix

In the 2021 Working meeting there was a presentation on viewer support for IIIF 3.0 and the community asked if this presentation could be turned into a matrix so the community can see which viewers support which area of the IIIF specifications. This matrix is generated automatically from the recipes and if you notice any thing that is incorrect please report it to the [cookbook GitHub site](https://github.com/IIIF/cookbook-recipes/issues/new).

## Which viewers are included?
Currently only [Mirador](https://projectmirador.org/) and the [Universal Viewer](https://universalviewer.io/) are listed on the cookbook and we welcome the addition of other IIIF viewers but they must support the following features:

 * Support for the [IIIF version 3.0 Presentation API](https://iiif.io/api/presentation/3.0/)
 * Have a public instance available that we can link to, ideally using the `iiif-content` parameter from the [IIIF Content State API](https://iiif.io/api/content-state/)
 * Support at least 1 cookbook recipe 

Currently the cookbook uses Mirador 3 and UV version 3.  

## Viewer Matrix

The possible values for viewer support are YES, NO or Partial. Check the recipe to see the full behaviour of the viewer to check it achieves the required function in the way you expect.
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
                        YES
                    {% else if current.support == "partial" %}
                        Partial
                    {% else %}
                        YES
                    {% endif %}
                {% else %}
                    {% if recipe.viewers contains viewer %} 
                        YES
                    {% else %}    
                        NO
                    {% endif %}
                {% endif %}
            </td>
        {% endfor %}
    </tr>
{% endfor %}
</table>
{% endfor %}


