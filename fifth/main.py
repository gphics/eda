import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pg_url = "Data/penguins_size.csv"
# pg_url = "fifth/Data/penguins_size.csv"
# for scatter plot
pg_df = pd.read_csv(pg_url, usecols=["species", "culmen_length_mm", "body_mass_g"])
# for crosstab
pg_df = pd.read_csv(
    pg_url, usecols=["species", "culmen_length_mm", "body_mass_g", "sex"]
)
pg_df = pg_df[["culmen_length_mm", "body_mass_g"]]

# Scatter plot
# fig = sns.scatterplot(
#     data=pg_df, x="culmen_length_mm", y="body_mass_g", hue="sex"
# )
# fig.set_title("Scatter plot of culmen length and body mass")


# crosstab
# ct = pd.crosstab(index=pg_df["species"], columns=pg_df["sex"])
# print(ct)

# pivot table
# pt = pd.pivot_table(pg_df, values="body_mass_g", index="sex", aggfunc="mean")
# print(pt)

# pairplot
# sns.pairplot(data=pg_df, hue="sex")

# Bar plot (catrgorical data / numerical data)
# sns.barplot(data = pg_df, x = "species", y="body_mass_g", estimator=np.mean, hue="sex")
# Box plot (catrgorical data / numerical data)
# sns.boxplot(data = pg_df, x = "species",y="culmen_length_mm", hue="sex")

# histogram

# male = pg_df[pg_df["sex"] == "MALE"]
# female = pg_df[pg_df["sex"] == "FEMALE"]

# sns.histplot(data = male, x = "culmen_length_mm", alpha = 0.5, color = "blue")
# sns.histplot(data = female, x = "culmen_length_mm", alpha = 0.5, color = "red")
# plt.legend(["Male", "Female"], loc="upper left")


# correlation and heatmap
corr = pg_df.corr()
sns.heatmap(corr, vmin=-1, vmax=1, annot = True)
