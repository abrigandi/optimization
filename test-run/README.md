# Test-run for Capacitated Facility Location Problem

This directory contains a self-contained test run for a capacitated facility location (CFL) problem.

Files:
- data/generate_sample_data.py — generates sample facilities and customers and writes test-run/data/sample_data.json
- run.py — loads data, builds an initial solution, applies neighborhood moves, runs simulated annealing, prints final solution, saves results to test-run/results/

Run locally:

python test-run/data/generate_sample_data.py --out test-run/data/sample_data.json
python test-run/run.py --data test-run/data/sample_data.json --out-dir test-run/results
