#!/usr/bin/env python3

# https://adventofcode.com/2020/day/1

# Returns list containing n entries that sum to desired total, otherwise None if none available
def find_n_entries_with_total(entries: list, n: int, target_total: int, _index: int = 0):
    if n == 1:
        for i in range(_index, len(entries)):
            if entries[i] == target_total:
                return [entries[i]]
        else:
            return None
    else:
        for i in range(_index, len(entries) - n + 1):
            result = find_n_entries_with_total(entries, n - 1, target_total - entries[i], i + 1)
            if result:
                result.insert(0, entries[i])
                return result
        return None

# Returns list containing n entries that sum to desired total, otherwise None if none available
def find_two_entries_with_total(entries: list, target_total: int):
    for i, i_val in enumerate(entries):
        for j in range(i + 1, len(entries)):
            j_val = entries[j]
            if i_val + j_val == target_total:
                return (i_val, j_val)
    return (None, None)

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        entries = [int(line.rstrip()) for line in file.readlines()]
    # Part 1
    (op_1, op_2) = find_n_entries_with_total(entries, 2, 2020)
    assert op_1 and op_2
    product_1 = op_1 * op_2
    print("Solution to Part 1 is: {}".format(product_1))

    # Part 2
    (op_1, op_2, op_3) = find_n_entries_with_total(entries, 3, 2020)
    assert op_1 and op_2 and op_3
    product_2 = op_1 * op_2 * op_3
    print("Solution to Part 2 is: {}".format(product_2))



    
    

