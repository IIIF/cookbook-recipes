---
title: Code Samples
layout: spec
breadcrumbs:
  - label: IIIF Cookbook
    link: index.html
code:
  - iiif-prezi3
topics:
  - basic
  - property
  - structure
  - image
  - AV
  - annotation
  - geo-recipes
---

<link rel='stylesheet' href="{{ site.cookbook_url | absolute_url }}/css/style.css"/>

# Code samples

In addition to the [viewer matrix](../matrix/) we now link to code samples and component libraries that supported cookbook recipes. The aim is to give readers of the cookbook code which they can use to re-create the recipe that they are reading. For components it is useful for readers to be able to see how the recipe is supported before deciding whether to integrate the component into their software.  

## Which libraries are included?

Currently only [iiif-prezi](https://iiif-prezi.github.io/iiif-prezi3/) is supported but we welcome additions of both code samples and components that support at least one recipe. If you would like to add a project to the list on this page please provide a pull request to the Cookbook repository. Note submissions should meet the following requirements:

 - Support for the [IIIF version 3.0 Presentation API](https://iiif.io/api/presentation/3.0/)
 - Have a public instance available that we can link to.
 - Support at least 1 cookbook recipe
 - Components should demonstrate how to initiate the component with the supplied Manifest in a [Code Sandbox](https://codesandbox.io) or other tool. 

## Code samples matrix

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
        {% for sample in page.code %}
            <th>{{ sample }}</th>
        {% endfor %}
    </tr>    
{% for recipe in sorted %}
    <tr>
        <td><a href="{{ site.cookbook_url | absolute_url }}{{ recipe.url }}">{{recipe.title}}{% if recipe.property%} ({{recipe.property}}){%endif%}</a></td>
        {% for sample in page.code %}
            {% assign current = recipe.code | where: "id",sample | first %}
            <td width="100px">
                {% if current.id == sample %}
                    {% if current.support == "full" %}
                        YES
                    {% else if current.support == "partial" %}
                        Partial
                    {% else %}
                        YES
                    {% endif %}
                {% else %}
                    {% if recipe.code contains sample %} 
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
