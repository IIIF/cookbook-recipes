---
title: Using Transcript Files with Audio or Video Content
id: 253
layout: recipe
tags: [video, audio, transcript, presentation]
summary: "Providing a transcript file to to be rendered alongside an audio or video resource."
v4-viewers:
 - Clover
 - Ramp
 - Aviary
 - Theseus
topic: AV
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



