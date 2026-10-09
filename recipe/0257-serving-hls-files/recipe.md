## Use Case

You have video served via HTTP Live Streaming (HLS) rather than as a single progressive-download file, and you 
want to reference that stream in a IIIF Manifest while also letting a user switch playback to a specific quality.

## Implementation Notes

Streaming media servers often deliver video and audio using HLS. HLS splits the source 
media into short segments and describes them in playlist files (`.m3u8`). A multivariant playlist can in
turn list several bitrate and resolution renditions of the same content. This allows an HLS-capable viewer to switch between 
them automatically as network conditions change, while the individual rendition playlists can also be served and linked
to on their own.

To reference HLS content in a Manifest, the body of the painting Annotation is a `Choice`, with each item in its `items`
list being one HLS playlist as an `.m3u8` file. Each option has a `type` of "Video" and a `label` identifying the quality 
of the rendition (e.g., "auto", "high", "medium", "low").

The "auto" option points at the multivariant playlist, so a viewer choosing it (or defaulting to it) still gets 
adaptive bitrate switching handled by its own HLS engine. The remaining options each point at a single-rendition 
playlist. Selecting one of these locks playback to that quality rather than letting the viewer renegotiate mid-stream.
The Manifest does not need to, and should not, expose the individual HLS media segments.

Every playlist referenced from a `Choice` option, and every media segment referenced by each of those, must be reachable 
by the viewer. Because HLS engines in browser-based viewers fetch playlists and segments themselves via JavaScript, cross-origin 
requests (CORS) must be enabled on all of these resources, not only on the one initially requested. A Manifest that 
resolves correctly can still fail to play if CORS is misconfigured on any playlist or segment.

Even though the video itself is delivered in segments, an associated caption or subtitle file does not need to be 
segmented to match. It should still be referenced as a single WebVTT resource via a `supplementing` Annotation on the 
Canvas, exactly as in [Using Caption and Subtitle Files with Video Content][0219].

## Restrictions

Not all browsers support HLS natively. Viewers running in those browsers need a JavaScript-based HLS engine. A viewer 
with no HLS support will be unable to play any of the options even though the Manifest itself is valid.

## Example

This example uses the *Lunchroom Manners* excerpt from Indiana University, also used as a progressive MP4 in 
[Simplest Manifest - Video][0003], here instead served as HLS. The `Choice` offers the adaptive multivariant playlist ("auto") 
alongside three fixed-bitrate renditions: high (1,200 kbps), medium (800 kbps), and low (400 kbps). Each is already 
broken into segments on the server.

{% include manifest_links.html version="3" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Multiple Choice of Audio Formats in a Single View (Canvas)][0434]
* [Using Caption Files with Video Content][0219]
* [Transcripts, Captions, and Subtitles - General Considerations][0231]
* [Simplest Manifest - Video][0003]

{% include acronyms.md %}
{% include links.md %}
