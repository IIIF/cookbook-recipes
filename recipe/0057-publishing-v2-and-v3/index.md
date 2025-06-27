---
title: Making IIIF Presentation API v2 and v3 manifests available at the same URL
id: 57
layout: recipe
tags: [implementation_note]
summary: "tbc"
viewers:
topic: note
---


## Use Case
As a manifest creator or host, or as a viewer or client developer, you may want to allow access to multiple versions of a manifest, each conforming to a different IIIF Presentation API major version. For the manifest creator or host, you may want to allow a wider range of clients the ability to view the resources in the manifests. For a client developer, you may want your client software to privilege one version of the API while allowing users to view manifests from a wide range of hosts with unpredictable and possibly uneven API conformance.

## Implementation notes

This recipe describes publishing IIIF v2 and v3 resources (both Presentation and Image API) at the same URL by using HTTP Content Negotiation. It is presented as an alternative approach both to publishing version-specific URLs and either requiring direct requests for retrieving the desired resource version or redirecting manifest requests from an neutral URL to a version-specific one.

Using Content Negotiation is useful in cases where changing the location of these resources would cause annotations targeting those resources, particularly those created and stored by third-party users, to no longer work. For example, an annotation targeting a region of a canvas that relies on resolving that canvas and any media (image, video, or audio) to show to end users. Using multiple URLs risks losing any work your users have done to annotate these canvases. Content Negotiation also provides a stable URL to reference a IIIF Manifest that will work, even as providers transition through 
supported IIIF versions.

[Content Negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation) is an established method of requesting varying responses from a server. In this case, the server will be asked to vary its response for either a version 2 or version 3 of a IIIF resource formatted in JSON-LD. This can be accomplished by using the `Accept` HTTP header. The value of this header contains a `profile` section that varies according to the IIIF version that is desired. Servers that implement this method should also provide a default response if the request does not contain these values. The examples below illustrate this process.

The [IIIF API specification](https://iiif.io/api/presentation/3.0/#63-responses) gives the values for the header. It follows a straightforward format:

`application/ld+json;profile="http://iiif.io/api/presentation/{VERSION}/context.json"`

If successful, the server should respond with a value in the `Content-Type` header that mirrors the requested value. 

If the server is unable to respond as requested &#8212; for example, it does not support the version requested &#8212; then it may either choose to return its default response (a manifest for a different IIIF Presentation version), or it may choose to return a `406 Not Acceptable` status code. Returning such an error implies support for Content Negotiation.

Where possible, servers are encouraged to return by default the latest IIIF Presentation API version. Since the server may substitute a different version than the one requested if the requested one is not available, clients will need to check the version information in the returned manifest. Simultaneously, client software must account for the response indicating the server does not support Content Negotiation and is responding with the manifest available at the requested URL. Put another way, clients must consider multiple possibilities and inconsistent affordances when requesting IIIF manifests from a server.

## Restrictions

There are several restrictions to using this pattern. Perhaps the most notable is that web browsers do not allow clients to vary their `Accept` headers, so viewing IIIF resources in a browser is restricted to viewing the server's default response. To view varying responses, the user must have the ability to control the HTTP request headers. This is available in tools such as [Postman](https://www.postman.com/).

This is an active area of work in web specifications, and may change as methodologies develop. The W3C has a current working group looking at [Content Negotiation by Profile](https://www.w3.org/TR/dx-prof-conneg/.). This specification offers dedicated `Accept-Profile` and `Content-Profile` headers, however these recommendations are
still in draft form.

## Example

These examples will use the `cURL` command-line HTTP client to control the request and view the response from the server. The `-H` flag controls the value of the request header. The `-v` flag makes the process "verbose" so that the response headers can be inspected. The leading `$` is used to illustrate a prompt and is not part of the command.

The first example shows a basic request to an HTTP service, but with an explicitly-set `Accept` header:

    $ curl -v -H "Accept: application/ld+json;profile=http://iiif.io/api/presentation/2/context.json" "https://iiif.io/api/cookbook/recipe/0057-publishing-v2-and-v3/manifest.json"

This provides a default response of a IIIF v2 manifest. Looking at some of the request (`>`) and response (`<`) values from cURL:

    > GET /api/cookbook/recipe/0057-publishing-v2-and-v3/manifest.json HTTP/2
    > Host: iiif.io
    > User-Agent: curl/8.7.1
    > Accept: application/ld+json;profile=http://iiif.io/api/presentation/2/context.json

    < HTTP/2 200
    < server: nginx
	< date: Fri, 07 Mar 2025 15:49:39 GMT
    < content-type: application/json

The response content should be a v2 manifest:

{% include manifest_links.html viewers="UV, Mirador, Annona, Glycerine Viewer, Theseus, Curation" manifest="manifest.json" %}
{% include jsonviewer.html src="manifest-v2.json" %}

To request a IIIF v3 manifest at the same URL the `Accept` header value can be adjusted:

    $ curl -v -H "Accept: application/ld+json;profile=http://iiif.io/api/presentation/3/context.json" "https://iiif.io/api/cookbook/recipe/0057-publishing-v2-and-v3/manifest.json"

Looking at the same request (`>`) and response (`<`) values from cURL as for the previous example, we see the difference in the request's `Accept` header:

    > GET /api/cookbook/recipe/0057-publishing-v2-and-v3/manifest.json HTTP/2
    > Host: iiif.io
    > User-Agent: curl/8.7.1
    > Accept: application/ld+json;profile=http://iiif.io/api/presentation/3/context.json

    < HTTP/2 200
    < server: nginx
	< date: Fri, 07 Mar 2025 15:54:11 GMT
	< content-type: application/json

The response now should be a v3 manifest. Note that the value of the manifest's `id` field is the same as in the v2 manifest.

{% include jsonviewer.html src="manifest-v3.json" %}

{% include acronyms.md %}
{% include links.md %}

