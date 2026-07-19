# Orbsim

A hybrid Python/C++ Satellite orbit simulation library with 3D ground track visualization.

## Features

- SGP4 orbit propagation with C++ core for performance
- TLE ingestion from files or strings
- Coordinate transforms: ECI → ECEF → Geographic
- Ground track computation over a configurable time window
- Interactive 3D globe visualization via Plotly
- Satellite conjunction (close approach) detection
- Ground station pass prediction
- CLI interface - orbsim simulate
- Extensible plugin architecture for custom propagators 

## Installation

1. Prerequisites:
a) Python 3.10+
b) CMake 3.20+
c) C++ 17 compiler

2. Install commands:

```bash
# Install from PyPI (coming soon)
pip install orbsim

# Install from source (development)
git clone https://github.com/PanSoulas/OrbSim.git
cd OrbSim
pip install -e ".[dev]"
```

## Usage

### CLI

Simulate a satellite ground track from a TLE file:

```bash
orbsim simulate --tle iss.txt --duration 90 --step 1
```

Options:
- `--tle` — path to a TLE file
- `--duration` — simulation duration in minutes (default: 90)
- `--step` — time step in minutes (default: 1)

## Architecture

```
ORBSIM/
├── README.md
├── pyproject
├── CMakeLists.txt
├── iss.txt
├── CHANGELOG.md
├── .python-version
├── .gitignore
├── .github/workflows/
    ├── ci.yml
    ├──release.yml
├── docs/
    ├── api/
    ├── getting_started.md
    ├── index.md
├── src/
    ├──_core/
        ├──bindings.cpp
        ├──CMakeLists.txt
        ├──coords.cpp
        ├──coords.hpp
        ├──sgp4.cpp
        ├──sgp4.hpp
    ├──orbsim
        ├──__init__.py
        ├──analy
```