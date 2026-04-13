# Map Drawing with Python

This repository is upgraded into a reproducible map-rendering mini-project.
It keeps the original notebook while adding a scriptable ASCII map pipeline with tests.

## Features

- Load coordinate points from CSV
- Render points on an ASCII grid
- CLI output for quick map previews
- Unit tests for renderer and CLI behavior

## Usage

```bash
python3 cli.py --data data/sample_points.csv
```

## Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## License

MIT License. See `LICENSE`.
