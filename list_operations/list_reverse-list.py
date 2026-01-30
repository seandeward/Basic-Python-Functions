def reverse_list(items):
    list_len = int(len(items))
    i = 0
    list_rev = []
    
    while i < list_len:
        item = range(i, 0, -1)
        print(item)
        list_rev.append(item)
        print(list_rev)
        
        i += 1

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    reverse_list(numbers)