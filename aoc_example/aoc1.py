"""
Given two lists in columns, pair the smallest on both list, the 2nd smallest
the 3rd smallest, ...
take the absolute differences
add them up
"""

def process_input():
    file = open('input.txt', 'r')
    lst1 = []
    lst2 = []

    for line in file.readlines():
        line = line.strip().split()

        first_number = int(line[0])
        second_number = int(line[-1])

        lst1.append(first_number)
        lst2.append(second_number)

    file.close()

    return lst1, lst2

def compute_manhattan(lst1, lst2):
    result = 0
    for x, y in zip(lst1, lst2):
        result += abs(y - x)
    return result

if __name__ == "__main__":
    lst1,lst2 = process_input()
    lst1.sort()
    lst2.sort()
    print(compute_manhattan(lst1, lst2))