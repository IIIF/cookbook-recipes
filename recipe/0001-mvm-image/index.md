---
title: Simplest Manifest - Single Image File
id: 1
layout: recipe
tags: [image, presentation]
summary: "The simplest viable manifest for image content. If all you have for an object is one image on the web and a label, this pattern turns it into a IIIF Presentation resource."
viewers:
  - Mirador
  - UV
  - Annona
  - Clover
  - Glycerine Viewer
  - Theseus
  - Curation
v4-viewers:  
  - Mirador
topic: 
 - basic
 - image
code:
 - iiif-prezi3
top_tabs:
  - label: Version 3
    content: "{% capture my_include %}{%- include_relative recipe.md version='3' -%}{% endcapture %}{{ my_include | markdownify }}"
  - label: Version 4
    content: "{% capture my_include %}{%- include_relative v4/recipe.md version='4' -%}{% endcapture %}{{ my_include | markdownify }}"
---

{{ theme.block-center-start }}

{% include blocks/tabs.html  tabs=page.top_tabs %}

{{ theme.block-end }}
<script>
  if (!window.location.hash) {
    let el = document.getElementById("version-3-heading");
    el.className += " is-active";
  }  
</script>