#!/usr/bin/env python3
"""Dependency-free static checks for the approved AI Services assistant hero."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from typing import TypedDict
from urllib.parse import unquote, urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "index.html"
H1 = "Your AI assistant, working in your office."
SUPPORTING = (
    "Like adding a reliable team member—available 24/7, never off sick, and focused "
    "on the repetitive work that holds your business back."
)
OLD_H1 = "Practical tools for work that slows you down."
OLD_HERO_TERMS = ("real project screenshot", "working browser tool")
PANEL_LABEL = "Illustration of an AI assistant organising routine office tasks."


class Element(TypedDict):
    tag: str
    attrs: dict[str, str | None]
    ancestors: tuple[str, ...]
    id: str | None


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[Element] = []
        self.elements: list[Element] = []
        self.text_nodes: list[tuple[str, tuple[str, ...]]] = []
        self.h1_nodes: list[tuple[str, tuple[str, ...]]] = []
        self._active_h1: list[list[str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        ancestors = tuple(
            str(node["id"])
            for node in self.stack
            if node.get("id")
        )
        node: Element = {"tag": tag, "attrs": attr, "ancestors": ancestors, "id": attr.get("id")}
        self.elements.append(node)
        self.stack.append(node)
        if tag == "h1":
            self._active_h1.append([])

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if not data.strip():
            return
        ancestors = tuple(str(node["id"]) for node in self.stack if node.get("id"))
        self.text_nodes.append((data, ancestors))
        if self._active_h1:
            self._active_h1[-1].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1" and self._active_h1:
            text = " ".join("".join(self._active_h1.pop()).split())
            ancestors = tuple(str(node["id"]) for node in self.stack if node.get("id"))
            self.h1_nodes.append((text, ancestors))
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                return


def in_section(record: Element, section_id: str) -> bool:
    return section_id in record["ancestors"]


def local_targets(parser: PageParser) -> list[str]:
    failures: list[str] = []
    ignored_schemes = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")
    for element in parser.elements:
        attrs = element["attrs"]
        for attribute in ("href", "src"):
            value = attrs.get(attribute)
            if not value or value.startswith("#") or value.startswith(ignored_schemes):
                continue
            parsed = urlparse(value)
            if parsed.scheme or parsed.netloc:
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            candidate = ROOT / path.lstrip("/")
            if path.endswith("/"):
                candidate /= "index.html"
            if not candidate.exists():
                failures.append(f"Broken local {attribute}: {value}")
    return failures


def main() -> int:
    parser = PageParser()
    parser.feed(PAGE.read_text(encoding="utf-8"))
    failures: list[str] = []
    ids = {str(element["id"]) for element in parser.elements if element.get("id")}
    hero_elements = [element for element in parser.elements if in_section(element, "top")]
    hero_text = " ".join(text for text, ancestors in parser.text_nodes if "top" in ancestors)
    work_elements = [element for element in parser.elements if in_section(element, "work")]
    all_h1 = [text for text, _ in parser.h1_nodes]

    if all_h1 != [H1]:
        failures.append(f"Expected exactly one H1 with approved text; found {all_h1!r}")
    if hero_text.count(H1) != 1:
        failures.append("Approved H1 must occur exactly once in the intended hero")
    if hero_text.count(SUPPORTING) != 1:
        failures.append("Approved supporting line must occur exactly once in the intended hero")
    if OLD_H1 in hero_text or OLD_H1 in PAGE.read_text(encoding="utf-8"):
        failures.append("Old hero H1 remains in the page")
    if any(term in hero_text for term in OLD_HERO_TERMS):
        failures.append("Old hero screenshot caption remains in the hero")
    if any(element["tag"] == "img" for element in hero_elements):
        failures.append("Hero must not contain an image asset")
    if any("assets/portfolio/tennis-app.png" in str(element["attrs"].get("src", "")) for element in hero_elements):
        failures.append("Hero still references the tennis screenshot")
    if not any("assets/portfolio/tennis-app.png" in str(element["attrs"].get("src", "")) for element in work_elements):
        failures.append("Later working-examples tennis screenshot is missing")

    panels = [element for element in hero_elements if element["attrs"].get("aria-label") == PANEL_LABEL]
    if len(panels) != 1:
        failures.append("Hero needs one meaningful office-assistant panel label")
    decorative_classes = {"task-sheet", "desk-monitor", "status-marker"}
    for element in hero_elements:
        classes = set(str(element["attrs"].get("class", "")).split())
        if classes & decorative_classes and element["attrs"].get("aria-hidden") != "true":
            failures.append(f"Decorative illustration element is not hidden: {element['attrs'].get('class')}")

    ctas = {
        "Start a small project": "#one-off-projects",
        "See working examples": "#work",
    }
    for label, target in ctas.items():
        matches = [
            element for element in hero_elements
            if element["tag"] == "a" and element["attrs"].get("href") == target
        ]
        if not matches or target[1:] not in ids:
            failures.append(f"Hero CTA target failed: {label} -> {target}")

    failures.extend(local_targets(parser))
    page_text = PAGE.read_text(encoding="utf-8")
    if "AI Services" not in page_text:
        failures.append("AI Services branding is missing")
    public_text = " ".join(text for text, _ in parser.text_nodes)
    meta_values = " ".join(
        str(element["attrs"].get("content", ""))
        for element in parser.elements
        if element["tag"] == "meta"
    )
    if "Simon Fung" in public_text or "Simon Fung" in meta_values:
        failures.append("Simon’s name appears in visible copy or metadata")

    checks = 14
    if failures:
        print(f"FAIL: {len(failures)} of {checks} AI assistant hero checks failed")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print(f"PASS: {checks}/{checks} AI assistant hero static checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
