from pathlib import Path
from subprocess import run
import unittest

from map_draw.renderer import render_ascii_map


class MapRendererTests(unittest.TestCase):
    def test_render_contains_points(self) -> None:
        drawing = render_ascii_map([("A", 1, 1), ("B", 2, 2)], width=5, height=5)
        self.assertIn("#", drawing)

    def test_cli(self) -> None:
        result = run(
            ["python3", "cli.py", "--data", "data/sample_points.csv"],
            check=True,
            text=True,
            capture_output=True,
        )
        self.assertIn("#", result.stdout)


if __name__ == "__main__":
    unittest.main()
