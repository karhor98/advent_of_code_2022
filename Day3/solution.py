
import numpy as np
from functools import partial, reduce


def find_compartment_errors(rucksack: str) -> str:
    # Assume rucksack has even number of items
    com_1, com_2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    lookups = set(com_1)
    for item in com_2:
        if item in com_1 :
            return item 

def priority_map(c: str) -> int:
    if str.isupper(c):
        return ord(c) - 38
    else:
        return ord(c) - 96

if __name__ == "__main__":

    with open("Day3/input.txt", "r") as f :
        data = f.read().split("\n")

    # Part 1 : Find common item type among 2 compartment within racksack.
    priority_sum = sum( map(lambda x : priority_map(find_compartment_errors(x)), data ))
    print(f"the sum of the priorities of those item types : {priority_sum}")

    # Part 2 : Find common item type among 3 racksack.
    f = lambda x : priority_map(reduce(np.intersect1d, map(list, x))[0])

    priority_sum_p2 = sum( [ f(data[i : i+3]) for i in range(0, len(data), 3) ] )
    print(f"the sum of the priorities of those item types : {priority_sum_p2}")


    
