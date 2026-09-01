# Optimization Toolkit

A small toolkit for prototyping optimization algorithms and solvers, including a test-run for a Capacitated Facility Location Problem (CFLP).

## Project layout

- config/ — configuration files and examples
- docs/ — design docs and API references
- examples/ — runnable examples
- src/ — Python package: algorithms, solvers, utils
- tests/ — unit tests
- test-run/ — self-contained CFLP test-run (data generator, SA heuristic, MIP comparison)

## Requirements

This project uses Python 3.8+. Install runtime requirements with:

```bash
pip install -r requirements.txt
```

The test-run uses numpy and PuLP (CBC solver by default). If you want to use another MIP solver, install and configure it separately.

## Test run (Codespaces)

These instructions assume you are running inside a GitHub Codespace (or any environment with Python available). They provide the exact commands to reproduce the CFLP test (data generation, simulated annealing, and MIP comparison).

1) Open this repository in a Codespace.

2) Open a terminal in the Codespace and create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate          # Windows
```

3) Install project requirements:

```bash
pip install -r requirements.txt
```

4) Generate sample data (example: 10 facilities, 50 customers):

```bash
python test-run/data/generate_sample_data.py \
  --n-facilities 10 \
  --n-customers 50 \
  --seed 42 \
  --out test-run/data/sample_data.json
```

This writes `test-run/data/sample_data.json` containing facility and customer records (coordinates, capacities, demands, fixed costs).

5) Run the CFLP test (Simulated Annealing + MIP comparison):

```bash
python test-run/run.py \
  --data test-run/data/sample_data.json \
  --out-dir test-run/results \
  --iters 2000 \
  --seed 42
```

What the script does:
- Loads facility and customer data
- Builds a greedy initial solution (simple heuristic)
- Runs Simulated Annealing (neighborhoods: open / close / swap)
- Prints the initial objective, SA best objective, and a sample of customer assignments
- Saves SA results to `test-run/results/sa_results.json`
- Attempts to solve the exact MIP using PuLP/CBC and saves results to `test-run/results/mip_results.json` (if solver is available)

6) Inspect results

- SA results: `test-run/results/sa_results.json` — contains `open_facilities`, `assignment` (customer -> facility), and `objective`.
- MIP results: `test-run/results/mip_results.json` — same schema if the MIP was solved.

You can compute the optimality gap as: `(SA_obj - MIP_obj) / MIP_obj * 100%` (if MIP_obj is available).

## Notes & tips

- PuLP ships with the CBC solver by default. If you have another solver (Gurobi, CPLEX, etc.) installed and configured with PuLP, the MIP solve may be faster and handle larger instances.
- Increase the `--iters` parameter passed to `test-run/run.py` to give SA more search time for larger instances.
- The test run supports Simulated Annealing (`--method sa`), hill climbing, Tabu Search, Iterated Local Search (`ils`), and Variable Neighborhood Search (`vns`).
- Use `--neighborhoods open,close,swap,double_swap,shake` to control the move mix. The available neighborhoods are documented in `test-run/README.md`.
- If you plan to run many experiments in Codespaces, consider adding a devcontainer that pre-installs dependencies and optionally a solver.

## Important: Deleting your Codespace

If you **delete the Codespace**, you will lose the `.venv` folder and all installed packages. When you open the repository again in a new Codespace, you will need to **repeat steps 1-3** (create venv, activate it, and install requirements):

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

After that, you can proceed with steps 4-5 to run the experiments.

## Running outside Codespaces

The same commands above work locally on your machine — simply clone the repo, create a virtual environment, install requirements, and run the data generator and `run.py`.

---

If you'd like, I can also add:
- a ready-to-use devcontainer for Codespaces that installs Python and the requirements (option 2),
- or a GitHub Actions workflow to run the test and upload results as artifacts.

Reply with `2` to add a devcontainer, `ci` to add an Actions workflow, or tell me which next step you prefer.
