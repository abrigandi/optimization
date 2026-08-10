"""Basic optimization example."""

from src.algorithms import gradient_descent

def main():
    """Run a basic optimization example."""
    
    # Define objective function
    def quadratic(x):
        return (x - 3) ** 2
    
    # Run optimization
    result = gradient_descent(
        objective_fn=quadratic,
        initial_point=0.0,
        learning_rate=0.01,
        iterations=100
    )
    
    print(f"Optimized point: {result}")

if __name__ == "__main__":
    main()
