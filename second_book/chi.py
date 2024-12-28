import pandas as pd
import scipy.stats as st

data_url = "second_book/Data/netflix_content_2023.csv"

df = pd.read_csv(
    data_url,
    usecols=[
        "Language Indicator",
        "Content Type",
    ],
)


# language indicator :['English' 'Korean' 'Non-English' 'Japanese' 'Hindi' 'Russian']
# content type :['Show' 'Movie']

# pre operation
movie = {
    "English": 0,
    "Korean": 0,
    "Non-English": 0,
    "Japanese": 0,
    "Hindi": 0,
    "Russian": 0,
}
show = {
    "English": 0,
    "Korean": 0,
    "Non-English": 0,
    "Japanese": 0,
    "Hindi": 0,
    "Russian": 0,
}


# operation
def calc(x):
    ct = x["Content Type"]
    li = x["Language Indicator"]
    if ct == "Movie":
        movie[li] = movie[li] + 1
    else:
        show[li] = show[li] + 1


df.apply(calc, axis=1)


# post operation
movie = {
    "English": 9605,
    "Korean": 949,
    "Non-English": 2144,
    "Japanese": 1098,
    "Hindi": 287,
    "Russian": 21,
}
show = {
    "English": 7663,
    "Korean": 633,
    "Non-English": 1108,
    "Japanese": 1199,
    "Hindi": 87,
    "Russian": 18,
}
# Movie                      14104
# Show                       10708

# pre operation
data = [
    ["ct", "en", "kr", "ne", "jp", "hd", "rs", "total"],
    ["movie", 9605, 949, 2144, 1098, 287, 21, 14104],
    ["show", 7663, 633, 1108, 1199, 87, 18, 10708],
]

# processing
x = data[1][1:]
y = data[2][1:]
z = []
for i in range(len(x)):
    z.append(x[i]+y[i])
# post operation
# observered value
data = [
    ["movie", 9605, 949, 2144, 1098, 287, 21, 14104],
    ["show", 7663, 633, 1108, 1199, 87, 18, 10708],
    ["Total", 17268, 1582, 3252, 2297, 374, 39, 24812],
]

new_df = pd.DataFrame(data, columns=["ct", "en", "kr", "ne", "jp", "hd", "rs", "total"])

