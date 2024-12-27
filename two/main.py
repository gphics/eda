import numpy as np
import pandas as pd
from scipy import stats

df_url = "two/Data/marketing_campaign.csv"

df = pd.read_csv(
    df_url,
    usecols=[
        "ID",
        "Year_Birth",
        "Education",
        "Marital_Status",
        "Income",
        "Kidhome",
        "Teenhome",
        "Dt_Customer",
        "Recency",
        "NumStorePurchases",
        "NumWebVisitsMonth",
    ],
)

# gbk = df.groupby("Kidhome")["NumStorePurchases"]
# mean_gbk = gbk.mean()
# median_gbk = gbk.median()

# print("MEAN: ", mean_gbk)
# print("MEDIAN: ", median_gbk)

# cor = np.corrcoef(df["Kidhome"], df["NumStorePurchases"])
# print(cor)

# gbe = df.groupby("Education")["Income"]

# print(gbe.mean())

# x = df.groupby("Education")
# x = df.groupby(["Education", "Income"])
# print(x)
# print(x.indices)
# for name, ent in x:
#     print("Rolling")
#     print(ent.head(3))

# print(x[["Income", "Kidhome"]].agg([np.sum, np.mean, np.std, np.var]))


#
#
#
# Concatenation
# df_concat_1 = pd.read_csv(
#     "two/Data/marketing_campaign_append1.csv",
#     usecols=[
#         "ID",
#         "Year_Birth",
#         "Education",
#         "Marital_Status",
#         "Income",
#         "Kidhome",
#         "Teenhome",
#         "Dt_Customer",
#         "Recency",
#         "NumStorePurchases",
#         "NumWebVisitsMonth",
#     ],
# )
# df_concat_2 = pd.read_csv(
#     "two/Data/marketing_campaign_append2.csv",
#     usecols=[
#         "ID",
#         "Year_Birth",
#         "Education",
#         "Marital_Status",
#         "Income",
#         "Kidhome",
#         "Teenhome",
#         "Dt_Customer",
#         "Recency",
#         "NumStorePurchases",
#         "NumWebVisitsMonth",
#     ],
# )

# print(df_concat_1.info)
# print("BREAKLINE ______-------_____")
# print("BREAKLINE ______-------_____")
# print("BREAKLINE ______-------_____")
# print(df_concat_2.info)

# app_df = pd.concat([df_concat_1, df_concat_2])
# print(app_df.info)

# data_1 = {
#     "school": ["Funaab", "UI", "Unilorin", "Unilag", "Uniabuja"],
#     "location": ["Abeokuta", "Ibadan", "Ilorin", "Lagos", "Abuja"],
# }
# data_2 = {
#     "population":[1000, 4000, 2000, 5000, 500]
# }
# data_1_df = pd.DataFrame(data_1)
# data_2_df = pd.DataFrame(data_2)

# conc_data_df = pd.concat([data_1_df, data_2_df], axis=1)
# print(conc_data_df)

# 09033449519 MTN 2gb


# Merging

# data_1 = {
#     "school": ["Funaab", "Fuoye", "Unilorin", "Unilag", "Uniabuja"],
#     "location": ["Abeokuta", "Oye-ekiti", "kwara", "Lagos", "Abuja"],
# }

# data_2 = {
#     "school": ["Funaab", "UI", "Unilorin", "Unilag", "Uniabuja"],
#     "location": ["Abeokuta", "Ibadan", "Ilorin", "Lagos", "Abuja"],
# }

# data_1_df = pd.DataFrame(data_1)
# data_2_df = pd.DataFrame(data_2)

# m_1 = pd.merge(data_1_df, data_2_df, how="left", on="location")
# print(m_1)


# data_1= {
#     "school": ["Funaab", "UI", "Unilorin", "Unilag", "Uniabuja"],
#     "location": ["Abeokuta", "Ibadan", "Ilorin", "Lagos", "Abuja"],
# }
# data_1_df = pd.DataFrame(data_1)

# sorted_df1 =data_1_df.sort_values("location", ascending=False)
# print()
# print(sorted_df1)


# Categorizig the data

# inc = df["Income"]

# cat_inc = pd.cut(x=inc, bins=[1000, 2000, 40000, 80000], labels=["Low", "Fair",  "Max"])

# print(cat_inc.head(5))

# removing duplicates
# data = df[["Education", "Marital_Status", "Kidhome", "Teenhome"]]
# dropped = data.drop_duplicates()
# print(dropped.shape)

# dropping column or row
# data = df[["Education", "Marital_Status", "Kidhome", "Teenhome", "NumStorePurchases"]]
# data_1 = data.head(10)
# data_2 = data_1.drop(labels = [4])
# print(data_2)

# changing type
inc_float = df["Income"]
inc_float = inc_float.fillna(0)
inc_int = inc_float.astype("int")

print(inc_float.head(5))
print(inc_int.head(5))