import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("nyc_air_bnb.csv")
engine = create_engine("mysql+pymysql://root:12335424@localhost:3306/airbnb")
df.to_sql("airbnb_table", engine, index=False, if_exists="replace")

