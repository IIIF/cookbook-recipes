---
title: Full recipe list
layout: page
breadcrumbs:
 - label: Cookbook Home
   link: index.html
---
<!-- TODO MAKE LINK USE {{ site.cookbook_url | absolute_url }}-->
<ul>
  {% assign recipes = site.pages | where_exp:"recipe","recipe.id > 0" %}
  {% assign sorted = recipes | sort:"id" %}
  {% for recipe in sorted %}
    <li>
      <h3>{{ recipe.id }}: <a href="{{ site.cookbook_url | absolute_url }}{{ recipe.url }}">{{ recipe.title }}</a></h3>
      <p>Tagged: 
      {% for tag in recipe.tags %}
        <a href="">{{ tag }}</a>
        {% if forloop.last == false %} | {% endif %} 
      {% endfor %}
      </p>
      <p>{{ recipe.summary }}</p>
    </li>
  {% endfor %}
</ul>
