---
title: Simplest Manifest - Single 3D Model
id: 1
layout: recipe
tags: [presentation]
summary: "The simplest viable manifest for 3D content. If all you have for an object is one model on the web and a label, this pattern turns it into a IIIF Presentation resource."
v4-viewers:  
  - Mirador
  - UV
  - Annona
  - Clover
  - Theseus
topic: 
 - basic
 - image
code:
 - iiif-prezi3
top_tabs:
  - label: Version 4
    content: "{% capture my_include %}{%- include_relative v4/recipe.md version='4' -%}{% endcapture %}{{ my_include | markdownify }}"
---

{{ theme.block-center-start }}

{% include blocks/tabs.html  tabs=page.top_tabs %}

{{ theme.block-end }}
<script>
  if (!window.location.hash) {
    let el = document.getElementById("version-4-heading");
    el.className += " is-active";
  }  
</script>