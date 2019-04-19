---
title: Text in Multiple Languages
id: 6
layout: recipe
tags: [i18n, text, presentation]
summary: "You have more than one label for a IIIF resource, and/or more than one language version of the label."
---


## Use Case

You have more than one label for a IIIF resource, and/or more than one language version of the label. This can be used for the statement that is required to be shown to the user, the summary of the content, and the metadata labels and values.


## Implementation notes

The value `none` indicates that the language value of the string is either unknown, or not applicable.

A client will choose the appropriate value(s) by following the processing rules provided in https://iiif.io/api/presentation/3.0/#43-language-of-property-values


## Example


{: .line-numbers data-src="manifest.json" }
```json
```


# Related recipes

* [Simple Image Manifest][0001]


