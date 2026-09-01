# Simulated Annealing Review

## Overview

Simulated Annealing (SA) is a meta-heuristic used to search for good solutions in large combinatorial optimization problems. It is inspired by annealing in physics, where a material is heated and then cooled slowly so that it can settle into a low-energy configuration.

For facility-location problems, SA is useful because the solution space is large and local greedy moves can get stuck in poor local optima. SA allows occasional moves to worse states in order to escape local minima.

---

## Key idea

The algorithm maintains a current solution and a temperature value T.

At each iteration:
1. Generate a neighbor solution.
2. Evaluate the objective value.
3. If the new solution is better, accept it.
4. If it is worse, accept it with probability
   
   $$
   P(\text{accept}) = e^{-\Delta / T}
   $$
   
   where $\Delta = \text{new cost} - \text{current cost}$.
5. Lower the temperature gradually.

This balances exploration early in the search with exploitation later.

---

## Why the exponential acceptance rule matters

The formula

$$
P(\text{accept}) = e^{-\Delta / T}
$$

is critical because it gives the right behavior:

- If the new solution is better, $\Delta < 0$, so the move is always accepted.
- If the new solution is worse, $\Delta > 0$, but it may still be accepted depending on temperature.
- At high temperature, worse moves are accepted more often.
- At low temperature, worse moves are rarely accepted.

This allows the algorithm to escape local minima early, while becoming more conservative as the run proceeds.

### Examples

If $\Delta = 100$ and $T = 1000$:

$$
P = e^{-100/1000} = e^{-0.1} \approx 0.905
$$

So there is about a 90% chance to accept this slightly worse move.

If $\Delta = 1000$ and $T = 1000$:

$$
P = e^{-1000/1000} = e^{-1} \approx 0.368
$$

So a much worse move is accepted only with about a 37% probability.

This makes the algorithm explore broadly at first and then settle down.

---

## Temperature and cooling schedule

Temperature is usually reduced using a multiplicative rule such as:

$$
T_{k+1} = \alpha T_k
$$

where $0 < \alpha < 1$.

Example:
- start with $T_0 = 1000$
- use $\alpha = 0.995$
- then temperature drops gradually:
  - $T_1 = 995$
  - $T_2 = 990.025$
  - etc.

The cooling parameter controls the speed of the search:

- larger $\alpha$ means slower cooling and more exploration
- smaller $\alpha$ means faster cooling and quicker convergence

In this project, the code uses:

```python
iters=5000
T = 1000.0
alpha = 0.995
```

This is a standard and reasonable annealing setup.

---

## Neighborhood exploration

A neighborhood is a set of nearby candidate solutions reachable from the current one.

For facility-location problems, a good neighborhood must explore different facility sets, not just simple swaps.

### Three move types in this project

1. OPEN
   - add a closed facility
   - explores solutions with more open facilities

2. CLOSE
   - remove an open facility
   - explores solutions with fewer open facilities

3. SWAP
   - replace one open facility with one closed facility
   - keeps facility count fixed
   - explores alternative facility combinations at the same size

This is a strong choice because the optimal number of open facilities is not known in advance. Restricting the search to swaps alone would make the algorithm too narrow.

---

## Why OPEN/CLOSE/SWAP is better than swap-only

Using only swaps is not the same as using all three moves.

A swap-only neighborhood explores solutions with the same number of open facilities.

For example, if the current solution has 3 open facilities, a swap-only search can produce states like:

- {0, 3, 8}
- {1, 3, 8}
- {0, 5, 8}

but not:

- {0, 3, 8, 2}  (requires OPEN)
- {0, 3}        (requires CLOSE)

In facility-location problems, the best solution may require a different number of facilities. Because of that, OPEN and CLOSE moves are essential for a richer neighborhood.

---

## Review of the code pattern in this project

The implementation in [test-run/run.py](../test-run/run.py) follows a clean SA structure.

### Key functions

- `objective(...)`: computes total cost
- `reassign_to_nearest(...)`: repairs candidate solutions to feasibility
- `neighborhood_move(...)`: generates a neighboring open-set
- `simulated_annealing(...)`: runs the annealing process

### Acceptance logic in the code

```python
delta = cand_obj - current_obj
if delta < 0 or random.random() < math.exp(-delta / max(1e-9, T)):
    current_open = cand_open
    current_assignment = cand_assignment
    current_obj = cand_obj
```

This is the standard SA rule.

- If the move improves the objective, accept it.
- If it worsens the objective, accept it probabilistically.
- The probability decreases as the cost increase grows.
- The probability increases when the temperature is high.

That is exactly the desired behavior.

---

## Code review comments

### Strengths

- The neighborhood is meaningful and not too narrow.
- The use of OPEN/CLOSE/SWAP is appropriate for facility-location problems.
- The acceptance rule matches standard SA theory.
- Temperature reduction is simple and standard.
- The algorithm tracks the best solution seen so far, which is essential.

### Good implementation choices

- `max(1e-9, T)` avoids division by zero.
- `best_obj` keeps the best solution found over the run.
- the repair function ensures candidate states remain feasible.

### Review note

The implementation is heuristic, not exact. It is meant to find good solutions, not prove optimality. That is appropriate for SA.

---

## Summary

Simulated Annealing is a search method that deliberately allows uphill moves with a probability controlled by temperature. The exponential acceptance rule is the core mechanism that gives it its behavior. In this project, the implementation is a good example of the standard approach:

- generate a candidate neighbor,
- repair to feasibility,
- evaluate the objective,
- accept better moves or probabilistically accept worse moves,
- cool down over time,
- remember the best solution found.

This is a solid, easy-to-understand SA design for a facility-location optimization problem.

---

## Suggested next topics

This review can be extended to other meta-heuristics:

- Tabu Search
- Variable Neighborhood Search
- Large Neighborhood Search
- Genetic Algorithms
- GRASP

For each, the same comparison questions are useful:

- What is the neighborhood?
- How are candidates generated?
- How are they accepted or rejected?
- What memory or tabu mechanism is used?
- What parameter controls search intensity?

---

## Personal notes

This note is meant to be a durable review artifact for future study. It is saved here so the work is not lost when chat sessions reset or when the discussion is interrupted across devices.
