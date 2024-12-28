import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

air_url = "Data/SF_Air_Traffic_Passenger_Statistics_Transformed.csv"
# air_url = "seventh/Data/SF_Air_Traffic_Passenger_Statistics_Transformed.csv"


air_df = pd.read_csv(air_url)
air_df["Date"] = pd.to_datetime(air_df["Date"], format="%Y%m")

plt.plot(air_df["Date"], air_df["Total Passenger Count"], color="tab:red")
plt.ticklabel_format(style="plain", axis="y")
plt.show()
