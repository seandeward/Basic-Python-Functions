nums = "1 2 3".split()

print("Duplicating strings...")
for num in nums:
    dbl_num = num * 2
    print(f"Before: {num} After: {dbl_num}")

print("Duplicating numbers...")
for num in nums:
    dbl_num = int(num) * 2
    print(f"Before: {num} After: {dbl_num}")