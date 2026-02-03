def rearrange(list_array):
    part1 = list_array[:4]
    part2 = sorted(list_array[4:], reverse=True)
    result = part2 + part1
    
    #print(f"[-] part1 = {part1}")
    #print(f"[-] part2 = {part2}")

    return result

def rearrange_v2(list_array):
    part1 = sorted(list_array[-3:], reverse=True)
    #print(part1)
    del list_array[3:]
    return part1 + list_array
    
    



if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
        # we want the end result of [7, 6, 5, 1, 2, 3, 4]
    array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # we want the end result of [10, 9, 8, 1, 2, 3, 4. 5, 6, 7]
    
    print(f" Result for array: {rearrange_v2(array)}")
    print(f" Result for array2: {rearrange_v2(array2)}")


# there could be another way to do this by just using one part, taking that, and removing it from the main list if we only want the 3 numbers taken, making it more flexible