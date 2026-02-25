import pandas as pd

itens = pd.read_csv('olist_order_items_dataset.csv')
produtos = pd.read_csv('olist_products_dataset.csv')

df_vendas = pd.merge(itens, produtos[['product_id', 'product_category_name']], on='product_id', how='left')
df_vendas.dropna(inplace=True)
df_vendas['price'] = df_vendas['price'].astype(float)
df_vendas.to_csv('vendas_limpas.csv', index=False, encoding='utf-8')