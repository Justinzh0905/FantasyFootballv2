import pandas as pd

#strips characters in filter from a fle 
def cleanfile(filenames, filter):

    #copy file content into data and remove characters in filter
    for filename in filenames:
        with open(filename, 'r') as file:   
            data = file.read()
            for char in filter:
                data = data.replace(char, "")

        #rewrite the modified file content into the file
        with open(filename, 'w') as file:
            file.write(data)
        
        df = pd.read_csv(filename, index_col='PLAYER NAME')
        if "RK" in df.columns:
            df.drop("RK", axis=1, inplace= True)
        if "-9999" in df.columns:
            df.drop("-9999", axis=1, inplace= True)

        df.to_csv(filename)



files = ["Stats2022.csv", "Stats2021.csv", "Stats2020.csv", "Stats2019.csv", "Stats2018.csv"]
cleanfile(files, "*+")

