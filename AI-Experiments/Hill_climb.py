import random

def hill_climbing(objective_function, initial_state, neighbors_function, is_ascent=True, max_iterations=1000):
    current_state = initial_state
    current_value = objective_function(current_state)
    
    for iteration in range(max_iterations):
        neighbors = neighbors_function(current_state)
        if not neighbors:
            break
        
        next_state = None
        next_value = None

        for neighbor in neighbors:
            value = objective_function(neighbor)
            if (is_ascent and value > current_value) or (not is_ascent and value < current_value):
                next_state = neighbor
                next_value = value
        
        if next_state is None:  # No improvement found
            break
        
        current_state = next_state
        current_value = next_value
        
    return current_state, current_value

# Example usage:
def objective_function(x):
    # Example: Maximizing a simple quadratic function y = -x^2 + 4x
    return -x**2 + 4*x

def neighbors_function(x):
    # Example: Returning neighboring states with a step of 1
    step_size = 1
    return [x - step_size, x + step_size]

initial_state = random.randint(0, 10)
is_ascent = True  # Set to False for descent (minimization)

optimal_state, optimal_value = hill_climbing(objective_function, initial_state, neighbors_function, is_ascent)
print(f"Optimal State: {optimal_state}, Optimal Value: {optimal_value}")
