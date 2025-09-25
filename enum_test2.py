# enum_test2.py
from enum import Enum
import time
import sys

# Define an enum for directions
class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

# Prepare test data
N = 5_000_000
string_values = ["NORTH"] * N
enum_values = [Direction.NORTH] * N

print("=== Basic Representation ===")
print("String sample:", string_values[0])
print("Enum sample:", enum_values[0], "| name:", enum_values[0].name, "| value:", enum_values[0].value)

# --- 1. Bulk comparisons ---
print("\n=== Bulk Comparisons ===")
start = time.time()
count = sum(1 for v in string_values if v == "NORTH")
print("String comparisons:", time.time() - start, "seconds")

start = time.time()
count = sum(1 for v in enum_values if v == Direction.NORTH)
print("Enum comparisons:", time.time() - start, "seconds")

# --- 2. Membership checks ---
print("\n=== Membership Checks ===")
def is_valid_string(val):
    return val in {"NORTH", "SOUTH", "EAST", "WEST"}

def is_valid_enum(val):
    return val in Direction

start = time.time()
count = sum(1 for v in string_values if is_valid_string(v))
print("String membership checks:", time.time() - start, "seconds")

start = time.time()
count = sum(1 for v in enum_values if is_valid_enum(v))
print("Enum membership checks:", time.time() - start, "seconds")

# --- 3. Memory footprint ---
print("\n=== Memory Footprint ===")
print("One string object:", sys.getsizeof("NORTH"), "bytes")
print("One enum object:", sys.getsizeof(Direction.NORTH), "bytes")
print("List of", N, "strings:", sys.getsizeof(string_values), "bytes (list overhead only)")
print("List of", N, "enums:", sys.getsizeof(enum_values), "bytes (list overhead only)")
