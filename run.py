import pandas as pd

df = pd.read_csv("global air pollution dataset.csv")

df["Country"] = df["Country"].astype(str).fillna("Unknown")
df["City"] = df["City"].astype(str).fillna("Unknown")

aqi_columns = ["AQI Value", "CO AQI Value", "Ozone AQI Value", "NO2 AQI Value", "PM2.5 AQI Value"]
df[aqi_columns] = df[aqi_columns].apply(pd.to_numeric, errors="coerce")

print("\n===== Quick Overview =====")
print(df.head())
print(df.info())

print("\n===== Unique Counts =====")
print("Cities:", df["City"].nunique())
print("Countries:", df["Country"].nunique())

print("\n===== Average AQI by Country =====")
country_aqi = df.groupby("Country")["AQI Value"].mean().reset_index()
print(country_aqi.sort_values("AQI Value", ascending=False))

print("\n===== AQI Category Counts =====")
print(df["AQI Category"].value_counts())

print("\n===== Worst Cities =====")
worst_cities = df.sort_values("AQI Value", ascending=False).head(10)
print(worst_cities[["Country", "City", "AQI Value", "AQI Category"]])

print("\n===== Best Cities =====")
best_cities = df.sort_values("AQI Value").head(10)
print(best_cities[["Country", "City", "AQI Value", "AQI Category"]])

print("\n===== Dominant Pollutant =====")
pollutant_cols = ["CO AQI Value", "Ozone AQI Value", "NO2 AQI Value", "PM2.5 AQI Value"]
df["Dominant Pollutant"] = df[pollutant_cols].idxmax(axis=1)

print(df[["Country", "City", "AQI Value", "Dominant Pollutant"]].head())
print("\n===== Dominant Pollutant Counts =====")
print(df["Dominant Pollutant"].value_counts())