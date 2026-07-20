Description of Scripts
---

`load_data.py`: This is the first script you want to run. This loads the AF3 data so you have the two files ready: pairs, and confident.

`string_downloader.py`: Download the STRING files into the correct folder, `data`.

`final_comp.py`: Makes the dataframe that has all ipTM and STRING scores. A csv file will be saves to `outputs\pr_roc` and a parquet file will be saved to `data`after running the line below.
    run this line: 
    
    ```{shell} 
    python scripts/final_comp.py --data-dir ./data 
    ```   

`figures.py`: Making the figures in the `output` folder

`data_analyzer.py`:

---
Each script has its own purpose for preforming certain actions.

After extracting the `summary_pairs.parquet` and `summary_confidences.parquet` from the docker image:

1) Run `load_data.py` to have LazyFrames for each parquet file

2) Run `string_downloader.py` to have the STRING files in your data folder

3) Run `final_comp.py` to have the csv file used for the PR and ROC curves

4) Run `cytoscape.py` to create the csv files to use in Cytoscape 

*Optional:*

5) Run `data_analyzer` to have the specific Dataframes ready to use for `figures.py` 
