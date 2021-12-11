def get_rates(file_content):
    ones_counts = [0 for x in range(12)]
    zeros_counts = [0 for x in range(12)]
    for line in file_content:
        for index, bit in enumerate(line):
            if int(bit) == 1:
                ones_counts[index] += 1
            if int(bit) == 0:
                zeros_counts[index] += 1
    binary_gamma_rate = ""
    binary_epsilon_rate = ""
    for i in range(12):
        if ones_counts[i] > zeros_counts[i]:
            binary_gamma_rate += str(1)
            binary_epsilon_rate += str(0)
        else:
            binary_gamma_rate += str(0)
            binary_epsilon_rate += str(1)
    
    return int(binary_gamma_rate, 2) * int(binary_epsilon_rate, 2)
      

with open("input.txt", "r") as f:
    content = f.read().splitlines()

print(get_rates(content))
