## Use Case

You have audio, such as oral histories or radio broadcasts, served via HTTP Live Streaming (HLS) rather than as a single 
progressive-download file, and you want to reference that stream in a IIIF Manifest so that it can be played in a IIIF 
viewer.

## Implementation Notes

This recipe is the audio counterpart to [Serving HLS Video Files][0257-4]. HLS splits the source media into short 
segments and describes them in a playlist file (`.m3u8`). Rather than downloading one large file, an HLS-capable 
player reads the playlist and then fetches the segments it lists in order. This allows playback to begin quickly and 
to seek within long recordings without downloading everything before that point.

To reference HLS audio in a Manifest, the body of the painting Annotation is the playlist itself. In IIIF 
Presentation API 4, audio is painted onto a Timeline rather than a Canvas: a Timeline has a `duration` but no `height` 
or `width`. The body has the `id` of the `.m3u8` file, a `type` of "Audio", a `format` of 
"application/vnd.apple.mpegurl", and, as with any other audio resource, a `duration`. The Manifest does not need to, 
and should not, expose the individual HLS media segments; the viewer's HLS engine discovers those from the playlist.

The `format` property is especially important for HLS. A browser cannot play an `.m3u8` playlist the way it plays an 
MP3 or MP4, so a viewer needs to know ahead of time that the resource is HLS in order to hand it to an HLS engine 
rather than to a plain `<audio>` element. Viewers should not have to rely on the `.m3u8` file extension or on the 
`Content-Type` header returned by the server, which is often missing or generic (e.g., "text/plain" or 
"application/octet-stream"). Publishers should use "application/vnd.apple.mpegurl", the IANA-registered media type 
for HLS playlists defined in [RFC 8216][rfc8216]. The same `format` is used for video and audio streams; the `type` 
of the body is what tells the viewer this is audio.

RFC 8216 also lists "audio/mpegurl" for compatibility with older software. Despite its name, it is not specific to 
audio streams, and publishers should not use it in new Manifests, though viewers may still find it in existing 
content. The unregistered "application/x-mpegURL" is also widely used by streaming servers and recognized by many 
players, so viewers may encounter it as well.

This recipe uses a single-rendition playlist, so the stream is delivered at one fixed bitrate. HLS also supports 
multivariant playlists that list several renditions of the same content so that a player can switch between them as 
network conditions change. That approach is covered in [Adaptive Bitrate Video][0731].

The playlist, and every media segment it references, must be reachable by the viewer. Because HLS engines in 
browser-based viewers fetch the playlist and segments themselves via JavaScript, cross-origin requests (CORS) must 
be enabled on all of these resources, not only on the playlist. A Manifest that resolves correctly can still fail to 
play if CORS is misconfigured on any segment.

Captions and transcripts for streamed audio do not need to be segmented to match the stream. See 
[Transcripts, Captions, and Subtitles - General Considerations][0231] for approaches to providing them through the 
Manifest.

## Restrictions

Not all browsers support HLS natively. Viewers running in those browsers need a JavaScript-based HLS engine. A viewer 
with no HLS support will be unable to play the audio even though the Manifest itself is valid.

## Example

This example uses a recording of Daphne Marlatt from the University of British Columbia, also used as a progressive 
MP3 in [Scholarly Annotation of a Poetry Reading][0103], here instead served as HLS.

{% include manifest_links.html manifest="v4/manifest.json" version="4" %}

{% include jsonviewer.html src="v4/manifest.json" %}

## Related Recipes

* [Simplest Manifest - Audio][0002-4]
* [Serving HLS Video Files][0257-4]
* [Adaptive Bitrate Video][0731]
* [Transcripts, Captions, and Subtitles - General Considerations][0231]

{% include acronyms.md %}
{% include links.md %}

[rfc8216]: https://www.rfc-editor.org/rfc/rfc8216#section-4 "RFC 8216: HTTP Live Streaming"
