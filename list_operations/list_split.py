nums = ['hello goodbye', 'testing 123', 'here is a message', 'this is the last message']

for num in nums:
    split_num = num.split(',')
    print(split_num)

    # prints the following:
        # ['hello goodbye']
        # ['testing 123']
        # ['here is a message']
        # ['this is the last message']