# Spras ready file script 
import os
from pathlib import Path
import polars as pl
import argparse
import networkx as nx
from load_data import load_data as ld 

def load_data(data_dir_path):
    data_dir = Path(data_dir_path)
    data = pl.scan_csv(str(data_dir / "final_comp.csv"))
    data = data.select(pl.col(["protein1","protein2","chain_pair_iptm_best", "chain_pair_iptm_mean", "combined_score"]))

    pairs, confidences = ld("data/")

    # make the uniprot IDs uppercase ~ protein1 & protein2
    data = data.with_columns(
        pl.col("protein1").str.to_uppercase(),
        pl.col("protein2").str.to_uppercase()
    )
    # Decide how ipTM will be judge as weight for spras (maybe use ipTM in confidence file)
    # Google said do iptm/ipsae
    
    # data = data.with_columns(weight=pl.lit())

    # Make undirected and directed edges use combined score + iptm
    data = data.with_columns(direction=pl.lit("U"))
    return data


if __name__ == "__main__":
    print("Running yeast_spras.py directly for testing...")
    data = load_data("data/")
    print("data rows:", data.select(pl.len()).collect().item())
    print("data schema:", data.collect_schema())
    print(type(data))
    print(data.collect().head())
    G = nx.Graph()
    print(G)

# output_dir = Path('../output/spras')
# output_dir.mkdir(parents=True, exist_ok=True)
# output_path = os.path.join(output_dir, 'yeast_spras.txt')