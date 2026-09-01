# Test-run for Capacitated Facility Location Problem

This directory contains a self-contained test run for a capacitated facility location (CFL) problem.

Files:
- data/generate_sample_data.py — generates sample facilities and customers and writes test-run/data/sample_data.json
- run.py — loads data, builds an initial solution, applies neighborhood moves, runs a selectable metaheuristic, prints the final solution, and saves results to test-run/results/

Run locally:

python test-run/data/generate_sample_data.py --out test-run/data/sample_data.json
python test-run/run.py --data test-run/data/sample_data.json --out-dir test-run/results

# Try another metaheuristic and neighborhood set
python test-run/run.py --method tabu --neighborhoods swap,double_swap --iters 5000

Available methods:
- `sa` — Simulated Annealing
- `hill_climbing` — randomized local search
- `tabu` — Tabu Search with short-term memory
- `ils` — Iterated Local Search with perturbation
- `vns` — Variable Neighborhood Search

Available neighborhoods:
- `open` — open one closed facility
- `close` — close one open facility when reassignment remains feasible
- `swap` — close one facility and open one closed facility
- `double_swap` — replace two open facilities with two closed facilities
- `shake` — replace several facilities to perturb a local optimum

The default method is `sa`, and the default neighborhood list includes all five neighborhoods. Results use the same JSON schema as before, with the output filename based on the selected method (for example, `tabu_results.json`).
