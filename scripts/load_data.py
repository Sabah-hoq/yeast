from pathlib import Path
import polars as pl


def load_data(data_dir_path):
    data_dir = Path(data_dir_path)
    pairs = pl.scan_parquet(str(data_dir / "summary_pairs.parquet"))
    confidences = pl.scan_parquet(str(data_dir / "summary_confidences.parquet"))

    pairs = pairs.drop_nulls(subset=["af3_id1", "af3_id2"])
    return pairs, confidences


if __name__ == "__main__":
    print("Running data_loader.py directly for testing...")
    pairs, confidences = load_data("data/")
    print("pairs rows:", pairs.select(pl.len()).collect().item())
    print("confidences rows:", confidences.select(pl.len()).collect().item())
    print("pairs schema:", pairs.collect_schema())
    print("confidences schema:", confidences.collect_schema())