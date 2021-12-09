with open("input.txt", "r") as f:
    content = f.read().splitlines()

previous_depth = 0
increase_count = 0

for line in content:
    if int(line) > previous_depth:
        increase_count += 1
    previous_depth = int(line)
print(increase_count - 1) # decrement 1 for the first measurement with N/A info
