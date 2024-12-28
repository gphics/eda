import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import style
import statistics

# pgs_url = "four/Data/penguins_size.csv"
pgs_url = "Data/penguins_size.csv"
hp_url = "four/Data/HousingPricesData.csv"
# hp_url = "Data/HousingPricesData.csv"
#####
#######
pg_size_df = pd.read_csv(pgs_url, usecols=["species", "culmen_length_mm"])
# hp_df = pd.read_csv(hp_url)
# hp_df = hp_df[["Zip", "Price", "Area", "Room"]]
# hp = hp_df["Price"]

# using histogram
# plt.style.use("seaborn-v0_8-whitegrid")
# fig = sns.histplot(data=pg_size_df, x="culmen_length_mm")
# fig.set_xlabel("Culmen length in mm", fontsize=15)
# fig.set_ylabel("Records count", fontsize=15)
# fig.set_title("Histogram", fontsize=20)


# using boxplot

# sns.boxplot(data=hp_df, x="Price")

# violin plot
# sns.violinplot(hp)
# count plot
# sns.countplot(pg_size_df, x="species")
# pie chart
# plt.subplots(figsize=(40, 18))
# sp_group = pg_size_df.groupby("species").count().reset_index()
# plt.subplot(1, 2, 1)
# plt.pie(sp_group["culmen_length_mm"], labels=sp_group["species"])


# x = pg_size_df.groupby("species").sum().reset_index()
# print(x.reset_index())
# print(labels=x["species"])
# plt.subplot(1, 2, 2)
# plt.pie(x["culmen_length_mm"], labels=x["species"])

# plt.show()
