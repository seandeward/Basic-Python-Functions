inputs = [1, 2, 3, 4, 5, 6]

def get_max_number(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far


if __name__ == "__main__":
    result = get_max_number(inputs)
    print(f"Max number is: {result}")