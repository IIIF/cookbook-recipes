---
title: Embedding HTML in descriptive properties
id: 7
layout: recipe
tags: [text, presentation]
summary: "You want to have more control on how your metadata is displayed. For example scientific names, and also links out to other sites. Also legacy systems that might include things like italic tags."
---

## Use Case

You want to have more control on how your metadata is displayed by adding links or simple formatting instructions to selected text blocks. For example, scientific names might need special formatting and links out to other sites benefit from being activatable. Legacy systems may also include rudimentary formatting in their output.

## Implementation notes

You may include minimal HTML markup only in the `summary` property and the `value` property in the `metadata` and `requiredStatement` objects. HTML is not permitted in `label` or other properties. Your HTML must be [well-formed XML](https://validator.w3.org/) and therefore must be wrapped in an element such as `p` or `span`.

To alert a consuming application that your content is HTML, the first character in your string must be ‘<’ and the last character must be ‘>’. If your content is plain text but happens to start and end with angle brackets as described above, add an additional whitespace character to the end of the value.

For security reasons, clients allow only `a`, `b`, `br`, `i`, `img`, `p`, `small`, `span`, `sub`, and `sup` tags, and may remove any or all of those. For more details of permitted and prohibited markup, see [the specification](https://iiif.io/api/presentation/3.0/#45-html-markup-in-property-values).

## Restrictions

None known.

## Example

[JSON-LD](manifest.json) | View in X | View in Y 

{: .line-numbers data-download-link data-download-link-label="Download me" data-line="7" data-src="manifest.json" }
```json
```

# Related recipes

* [Simplest Manifest - Single Image File][0001]

{% include acronyms.md %}
{% include links.md %}