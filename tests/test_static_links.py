from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ENTRYPOINTS = (
    "index.html",
    "index.prod.html",
    "nma-studio-standalone.html",
    "e156-submission/index.html",
    "e156-submission/assets/index.html",
    "e156-submission/assets/index.prod.html",
    "e156-submission/assets/nma-studio-standalone.html",
)

REQUIRED_ASSET_FILES = (
    "e156-submission/assets/app.js",
    "e156-submission/assets/app.min.js",
    "e156-submission/assets/js/utils/exports.js",
)


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.links.append(value)


def _is_external_or_fragment(link):
    parsed = urlparse(link)
    return (
        parsed.scheme in {"http", "https", "mailto", "tel", "data"}
        or link.startswith("#")
        or link.startswith("javascript:")
    )


def test_entrypoint_local_links_resolve_inside_repo():
    root = Path(__file__).resolve().parents[1]

    for relative in ENTRYPOINTS:
        html_path = root / relative
        assert html_path.is_file(), relative
        text = html_path.read_text(encoding="utf-8")
        assert "{{" not in text
        assert "C:\\" not in text and "D:\\" not in text and "/mnt/c/" not in text

        parser = LinkCollector()
        parser.feed(text)

        for link in parser.links:
            if _is_external_or_fragment(link):
                continue
            parsed = urlparse(link)
            target_part = unquote(parsed.path)
            target = (html_path.parent / target_part).resolve()
            assert root in target.parents or target == root, f"{relative} escapes repo: {link}"
            assert target.exists(), f"{relative} has broken local link: {link}"


def test_e156_asset_bundle_contains_runtime_dependencies():
    root = Path(__file__).resolve().parents[1]
    for relative in REQUIRED_ASSET_FILES:
        target = root / relative
        assert target.is_file(), relative
        assert target.stat().st_size > 1000, relative
