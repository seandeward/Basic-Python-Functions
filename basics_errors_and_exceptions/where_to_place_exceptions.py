
#! DON'T do this
# you don't want to put exceptions inside of a defined function. Instead, wrap the try-exception around the function's call
def craft_sword(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        if metal_bar == "iron":
            return "iron sword"
        if metal_bar == "steel":
            return "steel sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")

# * DO this!
try:
    craft_sword("gold bar")
except Exception as e:
    print(e)
