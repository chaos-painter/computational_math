import pandas as pd

def backward_differences_table(y):
    size = len(y)
    table = pd.DataFrame({'y': y})  # Start with given values
    diffs = y[:]  # Copy input values

    for i in range(1, size):  # Compute backward differences
        diffs = [diffs[j] - diffs[j - 1] for j in range(1, len(diffs))]
        table[f"Δ^{i}y"] = pd.Series(diffs)  # Add column to DataFrame

    return table

# Example usage
y = [1, 3, 6, 10, 15]  # Example data
table = backward_differences_table(y)
print(table)
