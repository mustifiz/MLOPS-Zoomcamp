import os

import pandas as pd

S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL", "http://localhost:4566")

options = {"client_kwargs": {"endpoint_url": S3_ENDPOINT_URL}}

df = pd.DataFrame(
    [
        {
            "PULocationID": "-1",
            "DOLocationID": "-1",
            "tpep_pickup_datetime": pd.to_datetime("2023-01-01 01:01:00"),
            "tpep_dropoff_datetime": pd.to_datetime("2023-01-01 01:10:00"),
            "duration": 9.0,
        },
        {
            "PULocationID": "1",
            "DOLocationID": "1",
            "tpep_pickup_datetime": pd.to_datetime("2023-01-01 01:02:00"),
            "tpep_dropoff_datetime": pd.to_datetime("2023-01-01 01:10:00"),
            "duration": 8.0,
        },
    ],
)

# df.to_parquet("tmp.parquet", index=False, engine="pyarrow", compression=None)
in_path = "s3://nyc-duration/taxi_type=yellow/year=2023/month=01/input.parquet"

df.to_parquet(
    in_path,
    engine="pyarrow",
    compression=None,
    index=False,
    storage_options=options,
)

out_path = "s3://nyc-duration/taxi_type=yellow/year=2023/month=01/output.parquet"

os.system(
    "S3_ENDPOINT_URL=http://localhost:4566 "
    f"INPUT_FILE_PATTERN={in_path} "
    f"OUTPUT_FILE_PATTERN={out_path} "
    "python batch.py --year 2023 --month 1 "
    "--categorical PULocationID,DOLocationID"
)
