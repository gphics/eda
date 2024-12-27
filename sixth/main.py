import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

m_url = "sixth/Data/marketing_campaign.csv"
# m_url = "Data/marketing_campaign.csv"

w_url = "sixth/Data/website_survey.csv"
# w_url = "Data/website_survey.csv"

m_df = pd.read_csv(m_url)
m_df = m_df[
    [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
        "MntGoldProds",
        "NumDealsPurchases",
        "NumWebPurchases",
        "NumCatalogPurchases",
        "NumStorePurchases",
        "NumWebVisitsMonth",
    ]
]

print(m_df.isnull().sum())
