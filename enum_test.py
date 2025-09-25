# enum_test.py
from enum import Enum
import time

# Define an enum for directions
class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

# Using strings
string_direction = "NORTH"

# Using enums
enum_direction = Direction.NORTH

# Show what they look like
print("String version:", string_direction)
print("Enum version:", enum_direction)        # prints Direction.NORTH
print("Enum name:", enum_direction.name)      # "NORTH"
print("Enum value:", enum_direction.value)    # 1

# Compare performance of string vs enum comparisons
N = 1_000_000

start = time.time()
for _ in range(N):
    if string_direction == "NORTH":
        pass
print("String comparisons took:", time.time() - start, "seconds")

start = time.time()
for _ in range(N):
    if enum_direction == Direction.NORTH:
        pass
print("Enum comparisons took:", time.time() - start, "seconds")
