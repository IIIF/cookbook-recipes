---
title: Viewer Matrix
layout: recipe
viewers:
 - Mirador
 - UV
topics:
 - key: basic
   label: Basic Recipes
 - key: AV
   label: Audio/Visual Recipes
---

# IIIF 3.0 Viewer Matrix

In the 2021 Working meeting there was a presentation on viewer support for IIIF 3.0 and the community asked if this presentation could be turned into a matrix so the community can see which viewers support which area of the IIIF specifications. This matrix is generated automatically from the recipes and if you notice any thing that is incorrect please report it to the [cookbook GitHub site](https://github.com/IIIF/cookbook-recipes/issues/new).

## Which viewers are included?
Currently only [Mirador](https://projectmirador.org/) and the [Universal Viewer](https://universalviewer.io/) are listed on the cookbook and we welcome the addition of other IIIF viewers but the must support the following features:

 * Support IIIF version 3.0 
 * Have a public instance available that we can link to, ideally using the `iiif-content` parameter from the [IIIF Content State API](https://iiif.io/api/content-state/)
 * Support at least 1 cookbook recipe 

## Viewer Matrix

{% for topic in page.topics  %}
### {{ topic.label }}
{% assign recipes = site.pages | where_exp: "recipe", "recipe.topic == topic.key" %}
{% assign sorted = recipes | sort: "id" %}
<table>
    <tr>
        <th>Recipe</th>
        {% for viewer in page.viewers %}
            <th>{{ viewer }}</th>
        {% endfor %}
    </tr>    
{% for recipe in sorted %}
    <tr>
        <td><a href="{{ site.cookbook_url | absolute_url }}{{ recipe.url }}">{{recipe.title}}</a></td>
        {% for viewer in page.viewers %}
            <td>
                {% if recipe.viewers contains viewer %}
                    YES
                {% else %}
                    NO
                {% endif %}
            </td>
        {% endfor %}
    </tr>
{% endfor %}
</table>
{% endfor %}


