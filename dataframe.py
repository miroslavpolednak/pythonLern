# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %%
df = pd.read_csv(
    "/Users/miroslavpolednak/VSCodeProject/PythonDataScience/DataScience-Python3/PastHires.csv")
# df.head(9)
# read last 5 row
df.tail(5)
# return names of column
df.columns
# return number of rows and column
df.shape
# %%
