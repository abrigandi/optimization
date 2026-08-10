"""Generate sample facilities and customers for CFLP and save as JSON."""
import json
import random
import argparse
import os


def generate(n_facilities=10, n_customers=50, seed=42, out="test-run/data/sample_data.json"):
    random.seed(seed)
    facilities = []
    for j in range(n_facilities):
        capacity = random.randint(100, 300)
        fixed_cost = int(capacity * random.uniform(10, 30))
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        facilities.append({
            "id": j,
            "capacity": capacity,
            "fixed_cost": fixed_cost,
            "x": x,
            "y": y,
        })

    customers = []
    for i in range(n_customers):
        demand = random.randint(1, 20)
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        customers.append({
            "id": i,
            "demand": demand,
            "x": x,
            "y": y,
        })

    data = {"facilities": facilities, "customers": customers}
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote sample data to {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-facilities", type=int, default=10)
    parser.add_argument("--n-customers", type=int, default=50)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=str, default="test-run/data/sample_data.json")
    args = parser.parse_args()
    generate(args.n_facilities, args.n_customers, args.seed, args.out)
