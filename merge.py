import pandas as pd

df1 = pd.read_csv("avg_betcent_per_poly.csv")
df2 = pd.read_csv("avg_node_w_degree.csv")
df3 = pd.read_csv("avg_page_rank_per_poly.csv")

df_test = pd.merge(df1, df2, on='poly')

df_final = pd.merge(df_test, df3, on='poly')
#print(df_final)
df_final.to_csv("avg_betcent_pagerank_degree.csv", index=False)