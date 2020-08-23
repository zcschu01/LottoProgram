import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use("bmh")

# Set data frame to CSV file
picker = input("Powerball or MegaMillions: ")
if(
    picker.lower() == "powerball" or
    picker.lower() == "power" or
    picker.lower() == "ball" or
    picker.lower() == "p"   
):
    df = pd.read_csv("ModifiedPBResults.csv")
    title = "Powerball Numbers Frequency"
else:
    df = pd.read_csv("ModifiedMMResults.csv")
    title = "MegaMillions Numbers Frequency"

# Set a mask for start and end dates to filter by
start_date = input("Enter a start date (2015-01-01): ")
end_date = input("Enter an end date (2020-12-31): ")
mask = (df["draw_date"] > start_date) & (df["draw_date"] <= end_date)

# Assign mask to data frame
df = df.loc[mask]

# Combine the columns of df to create new data frame
df1 = pd.DataFrame(df["First"], dtype=np.int64)
df1 = df1.rename(columns={"First":"Values"})
df2 = pd.DataFrame(df["Second"], dtype=np.int64)
df2 = df2.rename(columns={"Second":"Values"})
df3 = pd.DataFrame(df["Third"], dtype=np.int64)
df3 = df3.rename(columns={"Third":"Values"})
df4 = pd.DataFrame(df["Fourth"], dtype=np.int64)
df4 = df4.rename(columns={"Fourth":"Values"})
df5 = pd.DataFrame(df["Fifth"], dtype=np.int64)
df5 = df5.rename(columns={"Fifth":"Values"})
data = [df1, df2, df3, df4, df5]
combined_df = pd.concat(data, axis=0)
count_list = combined_df["Values"].value_counts().tolist()
value_list = combined_df["Values"].value_counts().index.tolist()
# print(count_list)
# print(value_list)

# Plotting the numbers
plt.figure(figsize=(16,8))
plt.title(title, fontsize=20)
plt.xlabel("Numbers", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.bar(x=value_list, height=count_list, align="center")
plt.xticks(np.arange(min(value_list), max(value_list) + 1, 1.0), fontsize=8)
plt.show()
# pd.value_counts(combined_df["Values"]).plot.bar()
