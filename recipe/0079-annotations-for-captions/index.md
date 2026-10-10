---
title: Using Annotations for Timed Text
id: 79
layout: recipe
tags: [video, caption, subtitle, presentation]
summary: "Providing captions, represented as annotations, to a video resource."
viewers:
 - Ramp
 - Theseus
v4-viewers:  
 - Mirador
topic: 
 - AV
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
    let el = document.getElementById("version-3-heading");
    el.className += " is-active";
  }  
</script>