# May crash when running...dont run
from pathlib import Path
import polars as pl
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from load_data import load_data

pairs, confidences = load_data("data/")
sizeCoreceted = (pairs.collect())["chain_pair_iptm_mean_corrected"]

# fig, ax = plt.subplots()
# plt.hist(sizeCoreceted, bins=100000, color='teal', edgecolor='black', alpha=0.5)
# ax.ticklabel_format(style='plain', axis='y')
# ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# plt.xlim(-0.015, 0.8)
# # Display the plot
# plt.show()

# filtering data
df_filtered = pairs.filter(pl.col("ipTM_size_corrected_mean") >= 0.061) 


max = (df_filtered.collect())["chain_pair_iptm_mean_corrected"].max()

top_edges3_normal = df_filtered.with_columns(
    (pl.col("chain_pair_iptm_mean_corrected")/max)
    )

print(len(top_edges3_normal.collect()))
print((top_edges3_normal.collect())["chain_pair_iptm_mean_corrected"].describe())
