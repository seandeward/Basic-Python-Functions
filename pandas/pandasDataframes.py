import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

# print the entire DataFrame
print(df)

# print specific rows from the DataFrame
print(df.loc[0])