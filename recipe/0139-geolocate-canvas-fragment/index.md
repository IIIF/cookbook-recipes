---
title: Represent Canvas Fragment as a Geographic Point on a Web Map
id: 139
layout: recipe
tags: [maps, annotation]
summary: "Make Web Annotation to provide geocoordinates for a fragment of a IIIF Presentation API 3.0 Canvas."
---

### Use Case 
A Canvas has a region of interest that contains the place name "Paris". You would like to associate this instance of "Paris" with the geocoordinates for a central point in Paris, France that clients can use for representing the targeted fragment in world map based user interfaces, such as [Leaflet](https://leafletjs.com/examples/geojson/) or [Google Maps](https://developers.google.com/maps/documentation/javascript/importing_data). This could mean simply showing a non-interactive point on a web map, but often more data from the resource is displayed in connection with the point as a result of available functionality within the MapUI, such as a pop-up that appears showing metadata from the resource upon clicking the point.

A multitude of real world resources benefit from geographic data, many of which are already represented in IIIF digital collections. New and old maps, travel journals, newspapers, manuscripts, poems and diaries are just a subset of cultural heritage artifacts that have geographic mentions. These mentions bring human context to the material and offer a recognizable, comfortable setting for discovering connections between disparate resources.

<img onclick="showBigImage()" style="max-height: 125px" src="./images/leaflet_example.png" />

### Implementation Notes
The third party [GeoJSON-LD](https://geojson.org/geojson-ld/) context is included in addition to the IIIF Presentation API 3.0 context. The GeoJSON-LD context supplies the vocabulary terms for the Annotation bodies since the IIIF Presentation API 3.0 context does not describe those terms. When the field `@context` is used as an array with multiple contexts, the IIIF Presentation API 3.0 context must be the last item in the array.

The GeoJSON `properties` field is generic and [can be nearly anything](https://tools.ietf.org/html/rfc7946#section-3.2). It is used to pass metadata along with the geocoordinates. This has implications on clients and parsers that must discern what data to use. For example, if the targeted resource has a `label` and the `properties` field has a `label`, the consuming interface must make a choice on which to prioritize for presentation purposes. In the image from the Use Case section, the "Label" uses the GeoJSON `properties` `label` (lines 80-83) instead of the `label` property from the Annotation or Canvas.

Note that [`geometry` can be more than just a `Point`.](https://tools.ietf.org/html/rfc7946#section-3.1)

### Restrictions
Applications that strictly follow Linked Data practices will find that nested GeoJSON coordinate arrays are incompatible with the processing model of JSON-LD 1.0. The JSON-LD 1.1 processing model does not have this restriction. Be aware if you plan to serialize JSON-LD into [other semantic data formats or markup languages](https://www.w3.org/TR/json-ld11/#relationship-to-other-linked-data-formats) such as RDF.  

### Example
The Manifest has one Canvas with one Image, and the Canvas has the same size dimensions as the Image. The Canvas has one Annotation Page with one Annotation targeting the region of interest where "Paris" appears using the [#xywh Fragment Selector syntax](https://www.w3.org/TR/annotation-model/#fragment-selector). The Annotation body is GeoJSON-LD, which is supported by a number of open source mapping systems. A client can parse the Annotation from the Canvas and pass the Annotation body into MapUI systems resulting in rendered geometric shapes on a world map. Often, data from the resource such as an image URL, label or description is connected with those shapes via [`properties`](https://tools.ietf.org/html/rfc7946#section-3.2) in GeoJSON. Since the image used is a IIIF Fixture following [IIIF Image API 3.0](https://iiif.io/api/image/3.0/), you can see the targeted fragment by supplying [the values used in the #xywh selector to the image URL](https://iiif.io/api/image/3.0/example/reference/59d09e6773341f28ea166e9f3c1e674f-gallica_ark_12148_bpt6k1526005v_f20/1300,3370,250,100/max/0/default.jpg).  

{% include manifest_links.html viewers="" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" config='data-line="2-5, 67-95"' %}

## Related Recipes
* [Represent Canvas Fragment as Multiple Geographic Points on a Web Map][TBD]
* [Represent Manifest as a Geographic Point on a Web Map][TBD]
* [Represent Manifest as a Geographic Polygon on a Web Map][TBD]
* [Fragment Selectors][0020]
* [Tagging Annotation][0021]

{% include acronyms.md %}
{% include links.md %}

<div id="bigImage">
	<h4 style="color:white;"> Click Image to Close </h4>
	<img onclick="hideBigImage()" style="max-height: 100%; max-width: 100%;" src="./images/leaflet_example.png" />
</div>

<style>
	#bigImage{
		position: fixed;
		top: 0;
		left : 0;
		height : 100em;
		width: 100%;
		background-color: rgba(0,0,0,.8);
		display:none;
		text-align: center;
		padding-top: 4em;
	}
	img{
		cursor: pointer;
	}
</style>

<script type="text/javascript">
	function showBigImage(){
		document.getElementById("bigImage").style.display = "block"
	}
	function hideBigImage(){
		document.getElementById("bigImage").style.display = "none"
	}
</script>
