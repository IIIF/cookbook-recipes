
This is a recipe from the [Presentation API Cookbook][annex-cookbook].

# Text in Multiple Languages 

## Use Case

You have more than one label for a IIIF resource, and/or more than one language version of the label. This can be used for the statement that is required to be shown to the user, the summary of the content, and the metadata labels and values.


## Implementation notes

The value `none` indicates that the language value of the string is either unknown, or not applicable.

A client will choose the appropriate value(s) by following the processing rules provided in https://iiif.io/api/presentation/3.0/#43-language-of-property-values


## Example


```jsonld
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.org/iiif/text-language/manifest",
  "type": "Manifest",
  "label": {
    "en": [
      "Whistler's Mother",
      "Arrangement in Grey and Black No. 1: The Artist's Mother"
    ],
    "fr": [
      "Arrangement en gris et noir no 1",
      "Portrait de la mère de l'artiste",
      "La Mère de Whistler"
    ],
    "none": [ "Whistler (1871)" ]
  },
  "metadata": [
    {
      "label": {
        "en": ["Creator"],
        "fr": ["Auteur"]  
      },
      "value": {
        "none": ["Whistler, James Abbott McNeill"]
      }
    }  
  ],
  "summary": {
    "en": ["A painting in oil on canvas created by the American-born painter James McNeill Whistler, in 1871."]
  },
  "requiredStatement": {
    "label": {
      "en": [ "Held By" ],
      "fr": [ "Détenu par" ]
    },
    "value": {
      "none": [ "Musée d'Orsay, Paris, France" ]
    }
  },

  "items": [
    {
      "id": "https://example.org/iiif/text-language/canvas1",
      "type": "Canvas",
      "width": 1114,
      "height": 991,
      "items": [
        {
          "id": "https://example.org/iiif/text-language/canvas1/page1",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://example.org/iiif/text-language/canvas1/page1/annotation1",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Whistlers_Mother_high_res.jpg/1114px-Whistlers_Mother_high_res.jpg",
                "type": "Image",
                "format": "image/jpg"
              },
              "target": "https://example.org/iiif/text-language/canvas1"
            }           
          ]
        }
      ]
    }    
  ]
}
```


# Related recipes

* [Simple Image Manifest][link]


