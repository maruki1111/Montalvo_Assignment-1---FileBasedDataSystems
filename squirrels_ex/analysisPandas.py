#pandas approach: 
#https://codesignal.com/learn/courses/basics-of-numpy-and-pandas-with-titanic-dataset/lessons/mastering-pandas-a-deep-dive-into-dataframes-and-data-manipulation
#https://medium.com/data-science/olympics-kaggle-dataset-exploratory-analysis-part-2-understanding-sports-4b8d73a8ec30
import pandas as pd

# If you're using your uploaded file in this chat, use this path:
# filepath = "/mnt/data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260121.csv"

# Otherwise, keep your local filename:
filepath = "squirrel.csv"

df = pd.read_csv(filepath)

# whole dataset (not recommended to print all)
# print(df)

# first N rows (like slicing your list)
print(df.head(2))

# "first row"
print(df.iloc[0])

# slice rows 10..19 (like squirrels[10:20])
print(df.iloc[10:20])

# column names (like squirrels[0].keys())
print(df.columns)

# one column
print(df["Age"].head(10))

# multiple columns (prints the first 10 rows of each column)
print(df[["Age", "Primary Fur Color", "Foraging"]].head(10))

# X,Y locations of gray squirrels
gray_xy = df.loc[df["Primary Fur Color"] == "Gray", ["X", "Y"]]
print(gray_xy.head(10))

# how many gray squirrels?
gray_count = (df["Primary Fur Color"] == "Gray").sum()
print(gray_count)

# how many Adult vs Juvenile (overall)
print(df["Age"].value_counts(dropna=False))

# how many Adult vs Juvenile GRAY squirrels
gray_age_counts = df.loc[df["Primary Fur Color"] == "Gray", "Age"].value_counts(dropna=False)
print(gray_age_counts)

