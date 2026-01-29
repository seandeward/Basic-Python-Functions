# append() is used to add items to the end of a list.
    # This method is especially useful when you need to populate an initially empty list within a loop or other iterative process. Each call to append() adds a single element to the list, modifying it in place


def get_odd_numbers(num):
    odd_numbers = []
    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers


if __name__ == "__main__":
    print(get_odd_numbers(10)) # prints [1, 3, 5, 7, 9]