with open("input.txt", "r") as f:
    content = f.read().splitlines()

horizontal_positions = 0
depth = 0

for line in content:
    command, value = line.split()
    if command == "forward":
        horizontal_positions += int(value)
    if command == "down":
        depth += int(value)
    if command == "up":
        depth -= int(value)

print(f"horizontal_positions = {horizontal_positions}, depth = {depth}")
print(f"the result is: {horizontal_positions * depth}")
