"""CLI for rendering ASCII map from CSV coordinates."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from map_draw.renderer import render_ascii_map


def load_points(path: Path) -> list[tuple[str, int, int]]:
    points: list[tuple[str, int, int]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            points.append((row["name"], int(row["x"]), int(row["y"])))
    return points


def main() -> int:
    parser = argparse.ArgumentParser(description="Render ASCII map from coordinate CSV.")
    parser.add_argument("--data", type=Path, required=True)
    args = parser.parse_args()
    points = load_points(args.data)
    print(render_ascii_map(points))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
