import math

# Define the Alpha-Beta Pruning function
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta, max_depth):
    # If we reach the terminal node (leaf node) or the maximum depth
    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        max_eval = -math.inf
        # Recur for child nodes
        for i in range(2):
            eval_value = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        # Recur for child nodes
        for i in range(2):
            eval_value = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return min_eval

# Example Usage

# Define the tree values (leaf nodes)
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Maximum depth of the game tree
max_depth = math.log2(len(values))

# Initial values of alpha and beta
alpha = -math.inf
beta = math.inf

# Start Alpha-Beta Pruning
optimal_value = alpha_beta_pruning(0, 0, True, values, alpha, beta, int(max_depth))

print(f"The optimal value is: {optimal_value}")
