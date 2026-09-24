#!/usr/bin/env python3
"""Dependency-free release checks for the installable skill package."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "README.md",
    "README.zh-TW.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "docs/examples.md",
    "docs/examples.zh-TW.md",
    "docs/verification.md",
    "assets/social-preview.jpg",
)
SOF_MARKERS = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    require(data.startswith(b"\xff\xd8"), "social preview is not a JPEG")
    offset = 2
    while offset < len(data):
        require(data[offset] == 0xFF, "invalid JPEG marker")
        while data[offset] == 0xFF:
            offset += 1
        marker = data[offset]
        offset += 1
        if marker in (0xD8, 0xD9):
            continue
        if marker == 0xDA:
            break
        require(offset + 2 <= len(data), "truncated JPEG segment")
        length = int.from_bytes(data[offset : offset + 2], "big")
        require(length >= 2 and offset + length <= len(data), "invalid JPEG segment length")
        if marker in SOF_MARKERS:
            require(length >= 7, "truncated JPEG size segment")
            height = int.from_bytes(data[offset + 3 : offset + 5], "big")
            width = int.from_bytes(data[offset + 5 : offset + 7], "big")
            return width, height
        offset += length
    raise ValueError("JPEG dimensions not found")


def main() -> None:
    for name in REQUIRED:
        require((ROOT / name).is_file(), f"missing {name}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    require(skill.startswith("---\n"), "SKILL.md needs YAML frontmatter")
    pieces = skill.split("\n---\n", 1)
    require(len(pieces) == 2, "SKILL.md frontmatter is not closed")
    frontmatter = pieces[0]
    require(re.search(r"^name:\s*coordinate-codex-tasks\s*$", frontmatter, re.M) is not None, "unexpected skill name")
    require(re.search(r"^description:\s*\S", frontmatter, re.M) is not None, "missing skill description")
    require(re.search(r"\b(TODO|TBD|PLACEHOLDER)\b", skill, re.I) is None, "unfinished skill placeholder")

    for name in ("README.md", "README.zh-TW.md", "docs/examples.md", "docs/examples.zh-TW.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if link.startswith(("https://", "http://", "#")):
                continue
            require((ROOT / name).parent.joinpath(link).exists(), f"broken local link in {name}: {link}")

    image = (ROOT / "assets/social-preview.jpg").read_bytes()
    require(len(image) < 1_000_000, "social preview must be under 1 MB")
    require(jpeg_dimensions(image) == (1280, 640), "social preview must be 1280x640")
    print("Skill package is valid; social preview is 1280x640 and under 1 MB.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
