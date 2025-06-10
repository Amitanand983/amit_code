import time
import os

# Violation 1: time.sleep() in loop (wastes CPU cycles)
def process_data():
    results = []
    for i in range(100):
        time.sleep(0.1)  # Bad: Blocking sleep in loop
        results.append(i * 2)
    return results

# Violation 2: Inefficient string concatenation in loop
def build_big_string():
    s = ""
    for i in range(1000):
        s += str(i)  # Bad: Creates new string each iteration
    return s

# Violation 3: Unnecessary file operations in loop
def write_temp_files():
    for i in range(50):
        with open(f"temp_{i}.txt", "w") as f:  # Bad: Many I/O operations
            f.write("test")

# Violation 4: Memory-inefficient large list
def generate_huge_list():
    return [x**2 for x in range(1000000)]  # Bad: Unbounded memory usage

# Violation 5: CPU-intensive busy wait
def busy_wait():
    start = time.time()
    while time.time() - start < 1:  # Bad: Actively consumes CPU
        pass

# Violation 6: Unoptimized imports
import math  # Bad: Imported but unused
import sys   # Bad: Imported but unused

# Violation 7: Redundant computations in loop
def calculate_stats():
    data = [x for x in range(1000)]
    for x in data:
        avg = sum(data) / len(data)  # Bad: Recomputes same value
        if x > avg:
            print(x)

if __name__ == "__main__":
    process_data()
    build_big_string()
    write_temp_files()
    big_list = generate_huge_list()
    busy_wait()
    calculate_stats()