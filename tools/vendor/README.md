# tools/vendor

`diagram-render.html` is the offline Mermaid renderer `tools/build_pack.py` uses (AD-5,
AD-6 step 2). It is a single self-contained page: Mermaid 11.16.1 plus the excalidraw
export code, with no network access needed.

- **Copied from:** `~/.claude/skills/gstack/lib/diagram-render/dist/diagram-render.html`,
  gstack 1.81.0.0 @ 0530392 (the bundle `make-pdf` uses). Copied from disk on 2 Nov 2026;
  nothing was downloaded.
- **sha256:** `46ed274ca8b6bc763308c87fea05fa9ad940d7f6bcfbd1bc0abbf56c6c0c705d`
  (matches gstack's `BUILD_INFO.json`).
- **Pinned contents:** mermaid 11.16.1, @excalidraw/excalidraw 0.18.1,
  @excalidraw/mermaid-to-excalidraw 2.2.2, react 18.3.1, react-dom 18.3.1. All MIT;
  excalidraw's bundled fonts are SIL OFL 1.1.
- **The builder uses** only `window.__renderMermaid(id, text)`, waits for it in headless
  Chrome (`--dump-dom`), and inlines the returned SVG, so chart labels stay as text.

Don't edit the file. To update it, copy a newer gstack build over it and update the
version and sha256 above.
