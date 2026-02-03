planets = {}
#print(planets["Pluto"]) # ! Prints KeyError (since there's no value set to the key "Pluto" yet)

planets["Pluto"] = False # ? Declaring that Pluto = False
print(planets["Pluto"]) # Prints False

# * if you assign a new value to an existing key, it updates
planets["Pluto"] = True
print(planets["Pluto"]) # Prints True