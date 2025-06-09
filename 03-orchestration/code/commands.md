```bash
pip install mlflow jupyter pandas numpy scikit-learn xgboost hyperopt 
wget https://raw.githubusercontent.com/DataTalksClub/mlops-zoomcamp/refs/heads/main/02-experiment-tracking/duration-prediction.ipynb


jupyter notebook

mlflow server \
    --backend-store-uri sqlite:///mlflow.db
```


```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("nyc-taxi-experiment")
```

```python
URL = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-01.parquet'
```