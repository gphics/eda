import numpy as np
from scipy import stats
import statistics
import math

# y = np.array([ 2 , 4  ,5 , 5 ,12 ,12 ,14, 14, 15, 15, 15 ,16])
# print(y.mean())
# print(np.median(y))
# print(stats.trim_mean(y, 0.1))

# x = [2,4,6,8,10]

# v = statistics.variance(x)
# print(statistics.mean(x))
# print(math.sqrt(v))
# print(statistics.stdev(x))

# ______--------_______

# ______--------_______

# ______--------_______

# Normal distribution
math_score = [
    83,
    91,
    91,
    85,
    80,
    53,
    74,
    60,
    92,
    55,
    56,
    65,
    81,
    83,
    79,
    88,
    59,
    51,
    71,
    51,
    56,
    55,
    50,
    56,
    75,
    58,
    65,
    73,
    90,
    77,
    64,
    72,
    81,
    66,
    94,
    85,
    69,
    52,
    83,
    88,
    72,
    79,
    71,
    94,
    69,
    55,
    55,
    59,
    84,
    75,
    86,
    65,
    52,
    71,
    81,
    80,
    52,
    59,
    66,
    83,
    68,
    77,
    80,
    93,
    77,
    86,
    64,
    54,
    83,
    63,
    52,
    88,
    52,
    58,
    78,
    52,
    75,
    52,
    76,
    66,
    71,
    60,
    92,
    61,
    57,
    62,
    77,
    89,
    50,
    69,
    85,
    73,
    67,
    94,
    59,
    74,
    64,
    92,
    62,
    70,
]
# y = 0
# for x in math_score:
#     if x < 60:
#         y = y +1
# print(y)
# 100
sample_size = len(math_score)
# 70
sample_mean = math.floor(np.mean(math_score))
sample_mean = round(np.mean(math_score), 2)
# 13
sample_std = math.floor(np.std(math_score))
sample_std = round(np.std(math_score), 2)

test_score = 60
max_score = 85
z_score = (test_score - sample_mean) / sample_std
sec = (max_score - sample_mean) / sample_std
prob = stats.norm.cdf(z_score)
s_p = stats.norm.cdf(sec)
percent_prob = round((s_p-prob) * 100, 2)
print(percent_prob)
