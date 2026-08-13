# csscompress

A fast and safe **CSS minifier** for Python — the community-maintained fork of
[`csscompressor`](https://pypi.org/project/csscompressor/) (itself a Python
port of YUI Compressor's CSS minifier).

## What's fixed vs upstream

Upstream `csscompressor` is dormant (last release 0.9.5, November 2017). `csscompress`
continues it with:

- **Data-URI whitespace fix**: `url("data:...")` values containing SVG or
  MathML were minified aggressively (`remove_ws=True`), destroying the
  whitespace that SVG/MathML data URIs need to render. `csscompress` preserves
  whitespace inside `url(...)` patterns, so `data:image/svg+xml,...` CSS works
  after minification.
- Proper `__version__` attribute (upstream shipped a stale one).

## Usage

```python
from csscompress import compress

minified = compress("body { color: #ff0000; /* comment */ }")
```

There is also a CLI:

```console
$ python -m csscompress input.css > output.min.css
```

## API

- `compress(css: str) -> str` — minify a CSS stylesheet.
- `compress_partitioned(css: str) -> list[str]` — minify and return each
  top-level rule separately.

## License

BSD (revised) — see `LICENSE`. The original project is a Python port of the
YUI Compressor CSS minifier:

- Portions Copyright (c) 2013 Sprymix Inc.
- Author of the Python port: Yury Selivanov
- Original authors: Julien Lecomte, Isaac Schlueter, Stoyan Stefanov,
  and contributors; Portions Copyright (c) 2011-2013 Yahoo! Inc.
