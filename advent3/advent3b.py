def filter_by_col_oxygen(index, content):
    ones_count = 0
    zeros_count = 0

    for line in content:
        if int(line[index]) == 1:
            ones_count += 1
        if int(line[index]) == 0:
            zeros_count += 1

    filtered_values = []
    if ones_count >= zeros_count:
        # keep only the ones with 1 in the first position
        for line in content:
            if int(line[index]) == 1:
                filtered_values.append(line)
        return filtered_values
    else:
        for line in content:
            if int(line[index]) == 0:
                filtered_values.append(line)
        return filtered_values


def filter_by_col_co2(index, content):
    ones_count = 0
    zeros_count = 0

    for line in content:
        if int(line[index]) == 1:
            ones_count += 1
        if int(line[index]) == 0:
            zeros_count += 1

    filtered_values = []
    if ones_count >= zeros_count:
        # keep only the ones with 0 in the first position
        for line in content:
            if int(line[index]) == 0:
                filtered_values.append(line)
        return filtered_values
    else:
        for line in content:
            if int(line[index]) == 1:
                filtered_values.append(line)
        return filtered_values


def get_oxygen_value(content):
    input_number_length = 12
    for index in range(input_number_length):
        if len(content) <= 1:
            break
        content = filter_by_col_oxygen(index, content)
    return int(content[0], 2)


def get_co2_value(content):
    input_number_length = 12
    for index in range(input_number_length):
        if len(content) <= 1:
            break
        content = filter_by_col_co2(index, content)
    return int(content[0], 2)


with open("input.txt", "r") as f:
    file_content = f.read().splitlines()

file_content_copy = file_content[:]  # for a copy instead of reference
print(get_oxygen_value(file_content) * get_co2_value(file_content_copy))
