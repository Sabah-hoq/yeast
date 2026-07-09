# yeast
Analyzing data from [GitHub repo](https://github.com/jurgjn/pooled-ppi-yeast). 

To pull data, run this line of code (approx. 30 GB). More information about the Docker Image can be found [here](https://hub.docker.com/r/jurgjn/pooled-ppi-yeast/tags).

```
docker run -p 8501:8501 jurgjn/pooled-ppi-yeast:v26.1
```
After running, the raw data of the proteins is most likely stored in `predictions-db`; the data I will extract/copy is `summary_confidences.parquet` and `summary_pairs.parquet` which are in `workspaces/data`.

```{shell}
> New-Item -Path "C:\yeast_data" -ItemType Directory -Force
> docker cp <container_name>:/workspace/data/summary_pairs.parquet C:\yeast_data\summary_pairs.parquet
> docker cp <container_name>:/workspace/data/summary_confidences.parquet C:\yeast_data\summary_confidences.parquet
> explorer C:\yeast_data
```

* yeast_data: A folder I made locally, replace with the folder you want the data in
Basic analysis of data will be in: 

If running into issues where the protein interface won't load after running the Dockerfile, try
```{shell}
docker run -d -p 8501:8501 --name <conatiner_name> jurgjn/pooled-ppi-yeast:v26.1
```
Comparing the STRING Scores with the AF3 ipTM scores is [here](https://github.com/Sabah-hoq/yeast/blob/main/graphs/graph.ipynb)
Analysis of Data is [here](tbd)
