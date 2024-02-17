from functions import *
from tabulate import tabulate
import sys

stroke_min = sys[0]
stroke_max = sys[1]
num_nei_min = sys[2]
num_nei_max = sys[3]
logfreq_min = sys[4]
logfreq_max = sys[5]
N = sys[6]

#df = get_randomized_words(generate_nonwords(2, 15, 100, 200, 2, 6, N=10, random_state=42))
df = get_randomized_words(stroke_min, stroke_max, num_nei_min, num_nei_max, logfreq_min, logfreq_max, N, random_state=42)
table = tabulate(df, headers='keys', tablefmt='grid')
print(table)