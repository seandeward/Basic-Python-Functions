#* my version of the function
def reverse_list(items):
    list_rev = []
    for i in range(int(len(items)), 0, -1):
        i -= 1
        list_rev.append(items[i])
    return list_rev

#* boot.dev's version of the function
def reverse_list(items):
    new_list = []
    for i in range(len(items) - 1, -1, -1):
        new_list.append(items[i])
    return new_list

#? The differences are directly lowering the length of the range by 1 in the range function and starting the range at -1 to compensate
