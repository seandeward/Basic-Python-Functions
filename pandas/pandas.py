import pandas as pd

myDataSet = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3,7,2]
}

myvar = pd.DataFrame(myDataSet)

print(myvar)