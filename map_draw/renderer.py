"""Simple ASCII map renderer for geospatial points."""

from __future__ import annotations


def render_ascii_map(points: list[tuple[str, int, int]], width: int = 40, height: int = 20) -> str:
    canvas = [["." for _ in range(width)] for _ in range(height)]
    for _, x, y in points:
        if 0 <= x < width and 0 <= y < height:
            canvas[height - 1 - y][x] = "#"
    return "\n".join("".join(row) for row in canvas)
