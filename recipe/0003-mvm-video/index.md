---
title: Simplest Manifest - Video
id: 3
layout: recipe
tags: [video, presentation]
summary: "The simplest viable manifest for video content. This pattern presents a single video file in a IIIF Presentation resource."
viewers:
 - Mirador
 - UV
 - Clover
 - Ramp
 - Aviary
 - Theseus
 - Glycerine Viewer
v4-viewers:
 - Mirador
 - UV
 - Aviary
topic:
 - basic
 - AV
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