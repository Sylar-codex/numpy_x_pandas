import numpy as np
import pandas as pd

# creating a series
series = pd.Series([1, 3, 5, np.nan, 6, 8])
print("creating series",series)

# creating dataframe with numpy array with a datetime index using date_range and labeled columns

# creating the datetime index
dates = pd.date_range("20130101",periods=6)
print("datetime index",dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=["A", "B", "C", "D"])
print("creating dataframe",df)

# creating dataframes using dictionary objects
df2 = pd.DataFrame(
     {
         "A": 1.0,
         "B": pd.Timestamp("20130102"),
         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
         "D": np.array([3] * 4, dtype="int32"),
         "E": pd.Categorical(["test", "train", "test", "train"]),
         "F": "foo",
     }
 )
 

print("creating dataframe using dictionary objects",df2)

# getting type of each column
print("types of each column", df2.dtypes)

# VIEWING DATA

# view top row
print("top row",df.head())

# view bottom row
print("bottom 3 row",df.tail(3))

# view just index
print("view just index",df.index)

# view just columns
print("view just columns", df.columns)

# return numpy representation
print("numpy representation", df.to_numpy())

# quick static summary
print("quick static summary", df.describe())

# Transposing data
print("Transposed data", df.T)

# SELECTION

# selecting a single column
print("selecting column A",df["A"])

# print first 3 rows
print("first three rows",df[0:3])

# print within the rangein the square bracket
print("rows within the range in the square bracket",df["20130102":"20130104"])

# Selection by label

# select a row matching a label
print("selecting a row that matches a label",df.loc[dates[0]])

# selecting all rows (:) with a select column labels
print("select all rows (:) with select column labels", df.loc[:,["A", "B"]])

# label slicing including both endpoints
print("label slcing where both endpoints are needed", df.loc["20130102":"20130104", ["A", "B"]])

# selecting a row and column to return a scalar
print("selecting row and column to return scalar", df.loc[dates[0], "A"])

# getting fast access to a scalar
print("getting fast access to a scalar", df.at[dates[0], "A"])

# Selection by position

# select via position of passed integers
print("selection via position of passed integers", df.iloc[3])

# integer slicing acting similar to numpy/python slicing
print("similar to numpy and python slicing", df.iloc[3:5, 0:2])

# list of integer position location
print("list of integer position location", df.iloc[[1, 2, 4], [0, 2]])

# slicing rows explicitly 
print("slicing rows explicitly",df.iloc[1:3, :])

# slicing column explicitly
print("slicing columns explicitly",df.iloc[:, 1:3])

# getting values explicitly
print("getting values explicitly", df.iloc[1, 1])

# fast access to a scalar
print("fast access to scalar",df.iat[1, 1])

# Bolean Indexing

# select rows where column A is greater than 0
print("rows where column A is > 0", df[df["A"] > 0])

# selecting values from a Dataframe where condition is met
print("selecting only values in the Dataframe that is > 0", df[df > 0])

# using isin() method
df3 = df.copy()
df3["E"] = ["one","one", "two", "three", "four", "three"]

print("df3 data", df3)

# filtering using isin()
print("filter rows with values in column E are two or four", df2[df2["E"].isin(["two", "four"])])