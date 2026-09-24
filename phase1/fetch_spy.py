import yfinance as yf

df = yf.download("SPY", period="5y", interval="1d", auto_adjust=False, multi_level_index=False)
df.to_csv("data/SPY_daily.csv")
print(len(df), "rows written")