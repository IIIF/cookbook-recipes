## Use Case

You have video served via HTTP Live Streaming (HLS) rather than as a single progressive-download file, and you 
want to reference that stream in a IIIF Manifest while also letting a user switch playback to a specific quality.

## Implementation Notes

Streaming media servers often deliver video and audio using HLS. HLS splits the source 
media into short segments and describes them in playlist files (`.m3u8`). A "master" (or "multivariant") playlist can in
turn list several bitrate/resolution renditions of the same content. This allows an HLS-capable player to switch between 
them automatically as network conditions change, while the individual rendition playlists can also be served and linked
to on their own.

To do this, the body of the painting Annotation is a `Choice`, with each item in its `items` list being one HLS playlist
as an `.m3u8` file. Each option has `type` of `Video` and a `label` identifying the quality of the rendition (e.g. 
"auto", "high", "medium", "low").

The "auto" option points at the master/multivariant playlist, so a player choosing it (or defaulting to it) still gets 
adaptive bitrate switching handled by its own HLS engine. The remaining options each point at a single-rendition 
playlist. Selecting one of these locks playback to that quality rather than letting the player renegotiate mid-stream.

Every playlist referenced from a Choice option, and every media segment referenced by each of those, must be reachable 
by the client. Because browser-based HLS players fetch playlists and segments themselves via JavaScript, cross-origin 
requests (CORS) must be enabled on all of these resources, not only on the one initially requested. A manifest that 
resolves correctly can still fail to play if it is misconfigured.

Even though the video itself is delivered in segments, an associated caption or subtitle file does not need to be 
segmented to match. It should still be referenced as a single WebVTT resource via a `supplementing` Annotation on the 
Canvas, exactly as in [Using Caption and Subtitle Files with Video Content][0219]. The manifest does not need to, and 
should not, expose the individual HLS media segments.

## Restrictions

Native HLS playback is currently limited to Safari; other browsers require a JavaScript-based HLS engine 
(such as hls.js) bundled into the viewer. A viewer with no HLS support will be unable to play any of the options even 
though the manifest itself is valid.

## Example

This example uses the "Lunchroom Manners" excerpt from Indiana University, also used as a progressive MP4 in 
[Simplest Manifest - Video][0003], here instead served as HLS. The Choice offers the adaptive master playlist ("auto") 
alongside three fixed-bitrate renditions (high/1200kbps, medium/800kbps, and low/400kbps), each already broken into 
segments on the server.

{% include manifest_links.html version="3" manifest="manifest.json" %}

{% include jsonviewer.html src="manifest.json" %}

## Related Recipes

* [Multiple Choice of Audio Formats in a Single View (Canvas)][0434] for the general `Choice` pattern, applied there to different container/codec formats rather than quality renditions
* [Using Caption and Subtitle Files with Video Content][0219] for adding captions or subtitles to the Canvas
* [Transcripts, Captions, and Subtitles - General Considerations][0231]
* [Simplest Manifest - Video][0003] for the same content served as a progressive MP4

{% include acronyms.md %}
{% include links.md %}
