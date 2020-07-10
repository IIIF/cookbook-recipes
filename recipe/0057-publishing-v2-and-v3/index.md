---
title: Publishing v2 and v3 versions
id: 57
layout: recipe
tags: [implementation_note]
summary: "tbc"
---


## Use Case

This recipe describes publishing IIIF v2 and v3 resources (both Presentation and Image API) at the same URL by using
Content Negotiation. It is presented as an alternative approach to publishing version-specific URLs for retrieving 
these resources.

Using Content Negotiation is useful in cases where changing the location of these resources would cause annotations 
targeting those resources, particularly those created and stored by third-party users, to no longer work. For example, 
an annotation targeting a region of a canvas that relies on resolving that canvas and any media (image, video, or audio)
to show to end users. Using multiple URLs risks losing any work your users have done to annotate these canvases. Content
negotiation also provides a stable URL to reference a IIIF Manifest that will work, even as providers transition through 
supported IIIF versions.

## Implementation notes

[Content Negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation) is an established method of requesting varying responses from a server. In this case, the server will
be asked to vary its response for either a version 2 or version 3 formatted JSON-LD. This can be accomplished by using
the `Accept` HTTP header. The value of this header contains a `profile` section that varies according to the IIIF 
version that is desired. Servers that implement this method should also provide a default response 
if the request does not contain these values. The examples below illustrate this process.

The IIIF API specifications give the values for the header. It follows a straightforward format:

`application/ld+json;profile="http://iiif.io/api/presentation/{VERSION}/context.json"`

If successful, the server should respond with a value in the `Content-Type` header that mirrors
the requested value. If the server is unable to respond as requested--for example, it does not support v3
manifests--then it may either choose to return its default response (a v2 manifest), or it may choose to return a
`406 Not Acceptable` status code. 

## Restrictions

There are several restrictions to using this pattern. Perhaps the most notable is that web browsers do
not allow clients to vary their `Accept` headers, so viewing IIIF resources in a browser is restricted to viewing 
the server's default response. To view varying responses, the user must have the ability to control the HTTP request 
headers. This is available in tools such as [Postman](https://www.postman.com/).

This is an active area of work in web specifications, and may change as methodologies develop. The W3C has a current 
working group looking at [Content Negotiation by Profile](https://www.w3.org/TR/2019/WD-dx-prof-conneg-20191126/). 
This specification offers dedicated `Accept-Profile` and `Content-Profile` headers, however these recommendations are
still in draft form.

## Example

These examples will use the `cURL` command-line HTTP client to control the request and view the response from
the server. The `-H` flag controls the value of the request header. The `-v` flag makes the process "verbose" so
that the response headers can be inspected. The leading `$` is used to illustrate a prompt and is not part of the command.

The first example shows a basic request to an HTTP service, but with an explicitly-set `Accept` header:

    $ curl -v -H "Accept: application/ld+json" "https://example.iiif.io/0057-publishing-v2-and-v3/manifest.json"

This provides a default response of a IIIF v2 manifest. Looking at the request (`>`) and response (`<`) (truncated for 
clarity):

    > GET /0057-publishing-v2-and-v3/manifest.json HTTP/2
    > Host: example.iiif.io
    > User-Agent: curl/7.64.1
    > Accept: application/ld+json
    >

    < HTTP/2 200
    < server: nginx/1.18.0
    < date: Wed, 24 Jun 2020 06:21:42 GMT
    < content-type: application/json; charset=utf-8    

The response content should be a v2 manifest:

{% include jsonviewer.html src="manifest-v2.json" %}

To request a IIIF v3 manifest at the same URL the `Accept` header value can be adjusted:

    $ curl -v -H "Accept: application/ld+json;profile="http://iiif.io/api/presentation/3/context.json"" "https://example.iiif.io/0057-publishing-v2-and-v3/manifest.json"

The response has varied accordingly:

    > GET /0057-publishing-v2-and-v3/manifest.json HTTP/2
    > Host: example.iiif.io
    > User-Agent: curl/7.64.1
    > Accept: application/ld+json;profile=http://iiif.io/api/presentation/3/context.json
    >

    < HTTP/2 200
    < server: nginx/1.18.0
    < date: Wed, 24 Jun 2020 06:29:39 GMT
    < content-type: application/ld+json;profile="http://iiif.io/api/presentation/3/context.json"

The response should be a v3 manifest:

{% include jsonviewer.html src="manifest-v3.json" %}

To illustrate the case where a server is unable to fulfil a request, a "sequence" resource is requested with
a version 3 Accept header. This resource type is available in version 2 manifests, but was removed in version 3.

    $ curl -v -H "Accept: application/ld+json;profile="http://iiif.io/api/presentation/3/context.json"" "https://iiif.bodleian.ox.ac.uk/iiif/sequence/7c99ac4d-c4db-43d3-97e4-40fee56fedf4_default.json"

    > GET /iiif/sequence/7c99ac4d-c4db-43d3-97e4-40fee56fedf4_default.json HTTP/2
    > Host: iiif.bodleian.ox.ac.uk
    > User-Agent: curl/7.64.1
    > Accept: application/ld+json;profile=http://iiif.io/api/presentation/3/context.json
    >
    < HTTP/2 406
    < server: nginx/1.18.0
    < date: Wed, 24 Jun 2020 06:34:54 GMT
    < content-type: text/plain; charset=utf-8
    < content-length: 61

    The requested resource is not available as a IIIFv3 response.

# Related recipes

Provide a bulleted list of related recipes and why they are relevant.


{% include acronyms.md %}
{% include links.md %}

