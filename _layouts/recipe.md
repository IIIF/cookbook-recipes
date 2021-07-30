---
layout: page
hero:
    image: "https://ids.si.edu/ids/iiif/NMAH-AC0396-0000007/131,1118,1840,1011/1500,/0/default.jpg"
breadcrumbs:
 - label: IIIF Cookbook
   link: index.html

---
<link rel='stylesheet' href="{{ site.cookbook_url | absolute_url }}/css/style.css"/>
<link rel='stylesheet' href="{{ site.cookbook_url | absolute_url }}/css/prism.css"/>

{{ content }}

<script src='{{ site.cookbook_url | absolute_url }}/js/prism.js'></script>
<script>
    Prism.plugins.customClass.map({
        number: 'prism-number'
    });
</script>
