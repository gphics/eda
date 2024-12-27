import numpy as np
import pandas as pd
import statistics
from scipy import stats
df_url = "one/Data/covid-data.csv"

df = pd.read_csv(df_url)

df = df[
    [
        "iso_code",
        "continent",
        "location",
        "date",
        "total_cases",
        "new_cases",
    ]
]

# tc_mean = np.mean(df["total_cases"])
# print(tc_mean)

# nc_median = np.median(df["new_cases"])
# print(stats.mode(df["new_cases"]))
# print(statistics.mode(df["new_cases"]))


# calculating variance
# nc_var = np.var(df["new_cases"])
# print(nc_var)


# calculating standard deviation
# nc_std = np.std(df["new_cases"])
# print(nc_std)


# calculating range
# nc_max = max(df["new_cases"])
# nc_min = np.min(df["new_cases"])
# print(nc_max)
# print(nc_min)


# working on percentiles

nc_70_p = np.percentile(df["new_cases"], 70)
print(nc_70_p)

nc_75_q = np.quantile(df["new_cases"], 0.75)
nc_iqr = stats.iqr(df["new_cases"])

print(nc_75_q)
print(nc_iqr)