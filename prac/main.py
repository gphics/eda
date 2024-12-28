import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

df_url = "Data/netflix_content_2023.csv"
# df_url = "prac/Data/netflix_content_2023.csv"

df = pd.read_csv(df_url)
df["Hours Viewed"] = df["Hours Viewed"].replace(",", "", regex=True).astype("int")
row_shape = df.shape[0]
percentage_missing_values = df.isnull().sum() * 100 / row_shape
# columns
# ['Title', 'Available Globally?', 'Release Date', 'Hours Viewed','Language Indicator', 'Content Type']

# removing release date columns
df.drop(columns=["Release Date"], inplace=True)

num_data_str = "Hours Viewed"
# group by content type to determine the viewers response to either show or movie base on hours viewed
gbc = df.groupby("Content Type")[num_data_str]
# Base on the mean derived, it is confirmed that people spent more time spent on shows than movies
gbc_mean_dict = {
    "Show": gbc.mean()["Show"],
    "Movie": gbc.mean()["Movie"],
}
gbc_mean = gbc.mean().reset_index("Content Type")
gbc_sum = gbc.sum().reset_index("Content Type")

_, ax = plt.subplots(nrows=1, ncols=2, figsize=(40, 20))

sns.set(font_scale=2)
# bar1 = sns.barplot(data=gbc_mean, x="Content Type", y=num_data_str, ax=ax[0])
# bar1.set_title("bar plot of content type against mean hour viewed".title(), fontsize=20)
# bar1.set_xlabel("Content type", fontsize=20)
# bar1.set_ylabel("Mean Hour Viwed", fontsize=20)

plt.subplot(1, 2, 1)
plt.bar(gbc_mean["Content Type"], gbc_mean[num_data_str])
plt.ticklabel_format(axis="y", style="plain")
plt.xlabel("Content Type", fontsize=20)
plt.ylabel("Hours Viewd", fontsize=20)
plt.title("bar plot of content type against mean hour viewed".title(), fontsize=20)

# 
# 
plt.subplot(1, 2, 2)
plt.bar(gbc_sum["Content Type"], gbc_sum[num_data_str])
plt.ticklabel_format(axis="y", style="plain")
plt.xlabel("Content Type", fontsize=20)
plt.ylabel("Hours Viewd", fontsize=20)
plt.title("bar plot of content type against sum hour viewed".title(), fontsize=20)
plt.show()
