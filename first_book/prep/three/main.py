import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# data_url = "three/Data/HousingPricesData.csv"
data_url = "Data/HousingPricesData.csv"

df = pd.read_csv(data_url, usecols=["Zip", "Price", "Area", "Room"])
df["Pricepersqm"] = df["Price"] / df["Area"]
sorted_df = df.sort_values("Price", ascending=False)

# Matplotlib
# plt.subplots(figsize=(50, 30))
# x = sorted_df["Zip"][0:10]
# y = sorted_df["Price"][0:10]
# y1 = sorted_df["Pricepersqm"][0:10]
# plt.subplot(1, 2, 1)
# plt.bar(x, y)
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel("Zip", fontsize=24)
# plt.ylabel("Price", fontsize=24)
# plt.subplot(1, 2, 2)
# plt.bar(x, y1)
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel("Zip", fontsize=24)
# plt.ylabel("Price", fontsize=24)
# plt.show()


# seaborn
_, ax = plt.subplots(1, 2, figsize=(40, 18))
fig = sns.barplot(data=sorted_df[0:10], x="Zip", y="Price", ax=ax[0])
fig.set_xlabel("Zip")
fig.set_ylabel("Price")


fig2 = sns.barplot(data=sorted_df[0:10], x= "Zip", y ="Pricepersqm", ax=ax[1])
fig2.set_xlabel("Zip")
fig2.set_ylabel("Price")
