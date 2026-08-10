# Getting Started

## Installation

```bash
pip install optimization-toolkit
```

## Quick Start

```python
from src.algorithms import gradient_descent

# Define your objective function
def objective(x):
    return x**2

# Run optimization
result = gradient_descent(objective, initial_point=5.0)
```

## Next Steps

See the `examples/` directory for more use cases.
