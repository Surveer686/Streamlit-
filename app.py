import pandas as pd
import streamlit as st

st.set_page_config(page_title="AQI Dashboard", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv("global air pollution dataset.csv")
    df["Country"] = df["Country"].astype(str).fillna("Unknown")
    df["City"] = df["City"].astype(str).fillna("Unknown")

    aqi_cols = ["AQI Value", "CO AQI Value", "Ozone AQI Value",
                "NO2 AQI Value", "PM2.5 AQI Value"]
    df[aqi_cols] = df[aqi_cols].apply(pd.to_numeric, errors="coerce")

    df["AQI Category"] = df["AQI Category"].astype(str).fillna("Unknown")

    return df

df = load_data()

st.title("Air Quality Index Dashboard")

st.sidebar.header("Filters")

countries = ["All"] + sorted(df["Country"].unique().tolist())
selected_country = st.sidebar.selectbox("Country", countries)

categories = sorted(df["AQI Category"].unique().tolist())
selected_categories = st.sidebar.multiselect(
    "AQI Category", categories, default=categories
)

filtered = df.copy()

if selected_country != "All":
    filtered = filtered[filtered["Country"] == selected_country]

filtered = filtered[filtered["AQI Category"].isin(selected_categories)]

"""st.subheader("Filtered Data")
st.dataframe(filtered, use_container_width=True)"""

col1, col2, col3 = st.columns(3)
col1.metric("Number of Cities", filtered["City"].nunique())
col2.metric("Average AQI", round(filtered["AQI Value"].mean(), 1))
col3.metric("Max AQI", int(filtered["AQI Value"].max()))

st.subheader("Top 10 Most Polluted Cities")
top_cities = filtered.sort_values("AQI Value", ascending=False).head(10)
st.bar_chart(top_cities.set_index("City")["AQI Value"], use_container_width=True)

st.subheader("Average AQI by Country")
country_aqi = (
    filtered.groupby("Country")["AQI Value"]
    .mean()
    .sort_values(ascending=False)
)
st.bar_chart(country_aqi, use_container_width=True)

st.subheader("Dominant Pollutant (Based on AQI)")
pollutant_cols = ["CO AQI Value", "Ozone AQI Value",
                  "NO2 AQI Value", "PM2.5 AQI Value"]

filtered["Dominant Pollutant"] = filtered[pollutant_cols].idxmax(axis=1)

st.dataframe(
    filtered[["Country", "City", "AQI Value", "Dominant Pollutant"]],
    use_container_width=True    
)

