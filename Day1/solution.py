
import numpy as np



if __name__ == "__main__":

    with open("Day1/input.txt", "r") as f :
        data = f.read().split("\n")
    
    elf_food = []
    tmp = []
    for i in range(len(data)):
        if data[i] != '':
            tmp += [int(data[i])]
        else :
            elf_food.append(sum(tmp))
            tmp = []

    # part 1 solution
    print(f"elf number {np.argmax(elf_food) + 1} has {max(elf_food)} total calories" )
    
    # part 2 solution
    # Sorting and return top 3
    sorted_elf_food = sorted(elf_food)
    print(f"sum of top 3 most calories {sum(sorted_elf_food[-3:])}" )
    
    
    
    