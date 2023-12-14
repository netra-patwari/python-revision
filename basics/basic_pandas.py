import pandas as pd

# !Pandas Series

# !series
# a = [1,2,3,4]
# b = pd.Series(a)
# print(b[2])

# a = [1,2,3,4]
# b = pd.Series(a, index = ["x", "y", "z" , '!'])
# print(b)


# calories = {"day1": 420, "day2": 380, "day3": 390}
# c = pd.Series(calories, index = ["day1", "day2"])

# print(c)

# !DataFrames
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford" , "Maruti"],
#   'passings': [3, 7, 2 , 4]
# }

# myvar = pd.DataFrame(mydataset)

# # print(myvar)


# # !
# #refer to the row index:
# print(myvar.loc[0])

# #use a list of indexes:
# print(myvar.loc[[0, 1]])

# ! named index
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford" , "Maruti"],
#   'passings': [3, 7, 2 , 4]
# }

# myvar = pd.DataFrame(mydataset , index=['car1' ,'car2','car3','car4'])

# # print(myvar)


# # !
# #refer to the row index:
# print(myvar.loc["car2"])

# !Pandas Read CSV

# df = pd.read_csv('basics/demo_csv_file.csv')
# # pd.options.display.max_rows = 9999 #without to_string()
# print(df.to_string())  #use to_string() to print the entire DataFrame.

# !Pandas Read JSON
# to_string() to print the entire DataFrame.
# f = pd.read_json('basics/data.json')
# print(f.to_string())

# If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
# n = pd.DataFrame(n)

# !
# df = pd.read_csv('basics/demo_csv_file.csv')
# print(df.head()) #first 5
# print(df.tail()) #last 5
# print(df.info()) #size,space,dtype

# df.fillna("YOLO", inplace = True) # method allows us to replace empty cells with a value
# print(df)
