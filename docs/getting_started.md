# Getting Started

## Installation

### Prerequisites
- Python 3.10+
- CMake 3.20+
- C++17 compiler

### Install from source

```bash
git clone https://github.com/PanSoulas/OrbSim.git
cd OrbSim
pip install -e ".[dev]"
```

## Usage

### CLI

Simulate the ISS ground track for 90 minutes:

```bash
orbsim simulate --satellite ISS --duration 90 --step 1
```

Or use a local TLE file:

```bash
orbsim simulate --tle iss.txt --duration 90 --step 1
```

### Python API

```python
from orbsim.core import Satellite
from orbsim.core.tle import fetch_tle
from orbsim.analysis.ground_track import compute_ground_track
from orbsim.viz.renderer_3d import render_ground_track
from datetime import datetime, timedelta

tle = fetch_tle("ISS")
sat = Satellite("ISS", 25544, tle)
start = datetime.utcnow()
end = start + timedelta(minutes=90)
track = compute_ground_track(sat, start, end, step_minutes=1.0)
render_ground_track(track)
```