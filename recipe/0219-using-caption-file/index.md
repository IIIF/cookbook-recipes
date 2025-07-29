---
title: Using Caption Files with Video Content
id: 219
layout: recipe
tags: [video, caption, presentation]
summary: "Providing a caption file to a video resource."
viewers:
 - Clover
 - Ramp
 - Aviary
 - Theseus
v4-viewers:
topic: AV

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