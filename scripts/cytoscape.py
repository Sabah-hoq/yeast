# Writing script that will be used when viewing iptm/STRING data in cytoscape 
import pandas as pd
import os
import polars as pl
import pathlib as Path

df_final_comparison = Path("../data/final_comp.csv") 
output_dir = '../cytoscape'

#best
df_final_comparison_sig2 = df_final_comparison.filter([pl.col("combined_score").is_not_null() & (pl.col("combined_score") >= 400),
    (pl.col("chain_pair_iptm_best") >= 0.6)
])
output_path = os.path.join(output_dir, 'df_final_comparison_best.csv')
df_final_comparison_sig2.to_csv(output_path, index=False)

#mean
not_missing = df_final_comparison['combined_score'].is_not_null()

df_final_comparison_sig = df_final_comparison.filter([pl.col("combined_score").is_not_null() & (pl.col("combined_score") >= 400),
    (pl.col("chain_pair_iptm_mean") >= 0.6)
])
output_path = os.path.join(output_dir, 'df_final_comparison_mean.csv')
df_final_comparison_sig.to_csv(output_path, index=False)