names_dict = {
    "jack": "bronson",
    "jill": "mccarty",
    "joe": "denver"
}

del names_dict["joe"] # ? deletes the key and value of "joe"

print(names_dict) # Prints: {'jack': 'bronson', 'jill': 'mccarty'}

# ! if you attempt to delete a key that doesn't exist, you will get an Error
    # * if you're unsure if a key is in a dictionary, use the 'in' keyword