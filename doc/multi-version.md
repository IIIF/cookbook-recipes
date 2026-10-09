---
title: Multi version recipes
layout: page
hero:
  image: "assets/images/heroes/smithsonian_cookbook.webp"
---
# Multi version recipes

The implementation of recipes that support multiple versions like Simplest Manifest - Image [Version 3][0001] and [Verison 4][0001-4] require a certain file layout so that the tabs that show the different versions and Manifest diff function correctly. 


The file structure looks as follows:

```
<recipe>/
    index.md
    recipe.md
    manifest.json
<recipe>/v4
        recipe.md
        manifest.json    
```

## index.md

This is located in the recipe directory and contains all of the front matter and it affects both versions of the recipe. This means that metadata like title, summary and topics are shared between recipe versions and for example you can't have separate titles for different versions. Below is an example of the common frontmatter metadata elements:

```
---
title: Simplest Manifest - Single Image File
id: 1
layout: recipe
tags: [image, presentation]
summary: "The simplest viable manifest for image content. If all you have for an object is one image on the web and a label, this pattern turns it into a IIIF Presentation resource."
topic: 
 - basic
 - image
```

`index.md` also has the viewer support but requires separate properties for each version. In the example below `viewers` is for v3 and `viewers-v4` are for v4 viewers. Code is for v3 and code-v4 is for v4 code implementations.
``` 
viewers:
  - Mirador
  - UV
v4-viewers:  
  - UV
  - Annona
code:
 - iiif-prezi3
```

The front matter also contains the following which sets up the tabs. Assuming you have followed the file naming convention in this guide then you can copy and paste the part below. 
```
{% raw %}
top_tabs:
  - label: Version 3
    content: "{% capture my_include %}{%- include_relative recipe.md version='3' -%}{% endcapture %}{{ my_include | markdownify }}"
  - label: Version 4
    content: "{% capture my_include %}{%- include_relative v4/recipe.md version='4' -%}{% endcapture %}{{ my_include | markdownify }}"
  - label: Manifest Comparison
    content: "{% assign path_parts = page.path | split: '/' %}{% assign recipe_dir = path_parts[1] %}{% capture my_include %}{%- include diff.html recipe=recipe_dir -%}{% endcapture %}{{ my_include | markdownify }}"
---
{% endraw %}
```

Inside the index.md it has the content below. This will setup the HTML for the tabs and default to v3 if `#version-4` is not appended to the URL. This can be copy and pasted and possibly should be moved to a layout so as not to duplicate the code. 

```
{{ theme.block-center-start }}

{% include blocks/tabs.html  tabs=page.top_tabs %}

{{ theme.block-end }}
<script>
  if (!window.location.hash) {
    let el = document.getElementById("version-3-heading");
    el.className += " is-active";
  }  
</script>
```

## recipe.md

In the parent directory the `recipe.md` file is for v3 and in the v4 directory it is for v4. Both files are for the text of the recipe. The file should not contain any frontmatter as this all comes from the `index.md` file. 

## manifest.json

Again in the parent directory this is v3 and in the v4 directory it is v4.  


# Linking to different versions

The convention in the cookbook is to link to recipes as follows:

 * Simplest Manifest - Image ([version 3][0001] / [version 4][0001-4])

Links to the recipes are contained in links.md and in markdown would be linked as follows:

```
[version 3][0001]
[version 4][0001-4]
```

by convention the link name is the recipe id and appended with `-4` for a version 4 recipe. 

{% include acronyms.md %}
{% include links.md %}