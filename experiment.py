import numpy as np
import time
import matplotlib.pyplot as plt

# Standard implementation using lists
def standard_approach(n):
    data = [i for i in range(n)]
    total = 0
    for value in data:
        total += value
    return total

# Optimized implementation using NumPy for cache efficiency
def optimized_approach(n):
    data = np.arange(n, dtype=np.int64)  # Ensures contiguous memory allocation
    return np.sum(data)

# List of increasing data sizes for testing scalability
data_sizes = [10**5, 10**6, 5*10**6, 10**7, 2*10**7]

# Store execution times for each method
standard_times = []
optimized_times = []

# Measure performance for each data size
for size in data_sizes:
    start = time.time()
    standard_approach(size)
    end = time.time()
    standard_times.append(end - start)

    start = time.time()
    optimized_approach(size)
    end = time.time()
    optimized_times.append(end - start)

# ---- GRAPH 1: Execution Time Comparison ----
plt.figure(figsize=(8, 5))
plt.bar(["Standard Approach", "Optimized Approach"], [standard_times[-1], optimized_times[-1]], color=['red', 'green'])
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison: Standard vs. Optimized Approach")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ---- GRAPH 2: Performance Over Increasing Data Sizes ----
plt.figure(figsize=(8, 5))
plt.plot(data_sizes, standard_times, marker='o', linestyle='-', color='red', label="Standard Approach")
plt.plot(data_sizes, optimized_times, marker='s', linestyle='-', color='green', label="Optimized Approach")
plt.xlabel("Data Size (Number of Elements)")
plt.ylabel("Execution Time (seconds)")
plt.title("Scalability of Standard vs. Optimized Approach")
plt.legend()
plt.grid(True)
plt.show()

# ---- GRAPH 3: Memory Access Pattern Representation ----
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Simulated Data Layouts
list_layout = np.random.choice([0, 1], size=(10, 10), p=[0.7, 0.3])
numpy_layout = np.ones((10, 10))

# Visualization of scattered (list-based) vs. contiguous (NumPy) storage
ax[0].imshow(list_layout, cmap="coolwarm", aspect="auto")
ax[0].set_title("Standard List (Scattered Memory)")
ax[0].set_xticks([])
ax[0].set_yticks([])

ax[1].imshow(numpy_layout, cmap="coolwarm", aspect="auto")
ax[1].set_title("Optimized NumPy (Contiguous Memory)")
ax[1].set_xticks([])
ax[1].set_yticks([])

plt.suptitle("Memory Access Patterns: Standard vs. Optimized Approach")
plt.show()