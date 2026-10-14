## Use Case

You have video served via HTTP Live Streaming (HLS) rather than as a single progressive-download file, and you 
want to reference that stream in a IIIF Manifest so that it can be played in a IIIF viewer.

## Implementation Notes

Streaming media servers often deliver video and audio using HLS. HLS splits the source media into short segments and 
describes them in a playlist file (`.m3u8`). Rather than downloading one large file, an HLS-capable player reads the 
playlist and then fetches the segments it lists in order. This allows playback to begin quickly and to seek within long 
media without downloading everything before that point.

To reference HLS content in a Manifest, the body of the painting Annotation is the playlist itself. The body has the 
`id` of the `.m3u8` file, a `type` of "Video", and a `format` of "application/vnd.apple.mpegurl". As with any other video, 
it should also carry `height`, `width`, and `duration`. The Manifest does not need to, and should not, expose the 
individual HLS media segments; the viewer's HLS engine discovers those from the playlist.

The `format` property is especially important for HLS. A browser cannot play an `.m3u8` playlist the way it plays an MP4, 
so a viewer needs to know ahead of time that the resource is HLS in order to hand it to an HLS engine rather than to a 
plain `<video>` element. Viewers should not have to rely on the `.m3u8` file extension or on the `Content-Type` 
header returned by the server, which is often missing or generic (e.g., "text/plain" or "application/octet-stream"). 
Publishers should use "application/vnd.apple.mpegurl" as the `format` value. It is the IANA-registered media type for 
HLS playlists defined in [RFC 8216][rfc8216], and it is the value used in this recipe. The same `format` applies 
whether the stream is video or audio only; the `type` of the body should be "Video" or "Sound" to distinguish the two.

RFC 8216 also lists "audio/mpegurl" for compatibility with older software. Publishers should not use it in new 
Manifests, but viewers may still find it in existing content. The unregistered "application/x-mpegURL" is also 
widely used by streaming servers and recognized by many players, so viewers may encounter it as well.

This recipe uses a single-rendition playlist, so the stream is delivered at one fixed bitrate and resolution. HLS also 
supports multivariant playlists that list several renditions of the same content so that a player can switch between 
them as network conditions change. That approach is covered in [Adaptive Bitrate Video][0731].

The playlist, and every media segment it references, must be reachable by the viewer. Because HLS engines in 
browser-based viewers fetch the playlist and segments themselves via JavaScript, cross-origin requests (CORS) must be 
enabled on all of these resources, not only on the playlist. A Manifest that resolves correctly can still fail to play 
if CORS is misconfigured on any segment.

Even though the video itself is delivered in segments, an associated caption or subtitle file does not need to be 
segmented to match. It should still be referenced as a single WebVTT resource via a `supplementing` Annotation on the 
Canvas, as in [Using Caption and Subtitle Files with Video Content][0219]. In IIIF Presentation API 4, that Annotation should also 
carry a `provides` property (for example `["subtitles"]` or `["closedCaptions"]`) indicating the accessibility feature the 
WebVTT file supplies.

## Restrictions

Not all browsers support HLS natively. Viewers running in those browsers need a JavaScript-based HLS engine. A viewer 
with no HLS support will be unable to play the video even though the Manifest itself is valid.

## Example

This example uses the *Lunchroom Manners* excerpt from Indiana University, also used as a progressive MP4 in 
[Simplest Manifest - Video][0003], here instead served as HLS.

{% include manifest_links.html manifest="v4/manifest.json" version="4" %}

{% include jsonviewer.html src="v4/manifest.json" %}

## Related Recipes

* [Adaptive Bitrate Video][0731]
* [Using Caption Files with Video Content][0219]

{% include acronyms.md %}
{% include links.md %}

[rfc8216]: https://www.rfc-editor.org/rfc/rfc8216#section-4 "RFC 8216: HTTP Live Streaming"
