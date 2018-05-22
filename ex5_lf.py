from ex4_alt import tsv, legend_list
from statkraft.ltm.io.converter import to_pandas

df, pip = to_pandas(tsv)
df = df.magnitude
df.columns = legend_list + [df.columns[-1]]
df.to_csv("mean_daily_prices.csv")
