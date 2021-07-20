---
layout: default
hero:
    image: "https://ids.si.edu/ids/iiif/NMAH-AC0396-0000007/131,1118,1840,1011/1500,/0/default.jpg"
breadcrumbs:
 - label: IIIF Cookbook
   link: index.html

---
<div class="content">
    <a href='{{ site.cookbook_url | absolute_url }}/'>Recipe home</a> | <a href='{{ site.cookbook_url | absolute_url }}/recipe/all/'>Recipe List</a>
    {{ content }}
</div>  

<link rel='stylesheet' href="{{ site.cookbook_url | absolute_url }}/css/prism.css"/>
<script src='{{ site.cookbook_url | absolute_url }}/js/prism.js'></script>
