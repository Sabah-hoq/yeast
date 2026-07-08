# yeast
Analyzing data from [GitHub repo](https://github.com/jurgjn/pooled-ppi-yeast). 

To pull data, run this line of code (approx. 30 GB). More information about the Docker Image can be found [here](https://hub.docker.com/r/jurgjn/pooled-ppi-yeast/tags).

```
docker run -p 8501:8501 jurgjn/pooled-ppi-yeast:v26.1
```
After running, the raw data of the proteins is most likely stored in `predictions-db`; the data I will extract/copy is `summary_confidences.parquet` and `summary_pairs.parquet` which are in `workspaces/data`.

```
> New-Item -Path "C:\yeast_data" -ItemType Directory -Force
> docker cp yeast_yuh:/workspace/data/summary_pairs.parquet C:\yeast_data\summary_pairs.parquet
> docker cp yeast_yuh:/workspace/data/summary_confidences.parquet C:\yeast_data\summary_confidences.parquet
> explorer C:\yeast_data
```
Basic analysis of data will be in: 


Comparing the STRING Scores with the AF3 ipTM scores is [here](https://github.com/Sabah-hoq/yeast/blob/main/graphs/graph.ipynb)
