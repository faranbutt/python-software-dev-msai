"""
Given many lists, count how many are safe
a list is safe if it's increasing or decreasing
and each pair of adjacent numbers differ by at most 3 and at least 1
"""

def process_input():
    with open("input.txt") as f:
        lines = f.readlines()
        all_lists = []
        for line in lines:
            all_lists.append(list(map(int, line.strip().split(' '))))

    return all_lists

def is_increasing(lst: list) -> bool:
    i = 0
    while i < len(lst) - 1:
        if lst[i] >= lst[i + 1]:
            return False
        i += 1
    return True

def is_decreasing(lst: list) -> bool:
    return is_increasing(list(reversed(lst)))

def is_safe(lst: list) -> bool:
    n = len(lst)
    for i in range(n - 1):
        if abs(lst[i] - lst[i + 1]) > 3 or abs(lst[i] - lst[i + 1]) < 1:
            return False
    if is_decreasing(lst) or is_increasing(lst):
        return True
    return False

def main():
    input_lists = process_input()
    counter = 0
    for lst in input_lists:
        if is_safe(lst):
            counter += 1

    print(counter)

main()