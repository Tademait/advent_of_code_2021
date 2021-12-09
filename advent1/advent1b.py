with open("input.txt", "r") as f:
    content = f.read().splitlines()

increase_count = 0
previous_depth = 0

for i in range(len(content) - 2):
    depth_window = int(content[i]) + int(content[i+1]) + int(content[i+2])
    if depth_window > previous_depth:
        increase_count += 1
    previous_depth = depth_window
print(increase_count - 1) # decrement 1 for the first measurement with N/A info
