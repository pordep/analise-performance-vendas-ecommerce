import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('vendas_limpas.csv')

engine = create_engine('mysql+pymysql://root:123localhost:3306/olist_dataset')

df.to_sql('vendas_ecommerce', con=engine, if_exists='replace', index=False)
