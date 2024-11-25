# Define the knowledge base and inference rules
knowledge_base = {
    "A": True,  # Fact: A is true
    "B": False,
    "C": False,
    "D": False,
}

rules = {
    "B": ["A"],  # Rule: If A is true, then B is true
    "C": ["B"],  # Rule: If B is true, then C is true
    "D": ["C"],  # Rule: If C is true, then D is true
}


# Forward Chaining function
def forward_chaining(kb, rules):
    inferred = set()
    changes = True

    while changes:
        changes = False
        for conclusion, premises in rules.items():
            if all(kb.get(premise, False) for premise in premises) and not kb.get(conclusion):
                kb[conclusion] = True
                inferred.add(conclusion)
                changes = True

    return list(inferred)


# Backward Chaining function
def backward_chaining(goal, kb, rules):
    if goal in kb and kb[goal]:  # Goal is already in the KB and true
        return True

    if goal in rules:  # Goal has a rule
        for premise in rules[goal]:
            if not backward_chaining(premise, kb, rules):
                return False
        kb[goal] = True  # If all premises are true, set the goal as true
        return True

    return False


# Resolution Strategy (simple example)
def resolution(query, kb):
    # Negate the query and try to derive a contradiction
    neg_query = not kb.get(query, False)
    return neg_query == False  # Returns True if the negated query cannot hold


# Testing the algorithms
forward_chaining_result = forward_chaining(knowledge_base.copy(), rules)
backward_chaining_result = backward_chaining("D", knowledge_base.copy(), rules)
resolution_result = resolution("D", knowledge_base.copy())

# Display results
print("Forward Chaining Result:", forward_chaining_result)
print("Backward Chaining Result:", backward_chaining_result)
print("Resolution Result:", resolution_result)
