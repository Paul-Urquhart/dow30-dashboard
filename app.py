import streamlit as st
import pandas as pd
import plotly.graph_objects as go 
import datetime as dt 


# DJIA INDEX AND MA-20

df = pd.read_csv("data/gold_dow_index.csv")

# df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

latest_data_date = df['date'].max()
formatted_date = latest_data_date.strftime("%d-%B-%Y")
st.text(formatted_date)

# Create the OHLC chart
fig = go.Figure()

fig.add_trace(
    go.Ohlc(
        x=df["date"],
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"],
        name="Daily bars"
    )
)

fig.add_trace(
    go.Scatter(
        x=df["date"],
        y=df["ma20"],
        mode="lines",
        line=dict(color="orange", width=2),
        name="20‑Day MA"
    )
)


fig.update_layout(
    title="Dow Jones Industrial Average with 20-day moving average",
    xaxis_title="Date",
    yaxis_title="Price",
    xaxis_rangeslider_visible=False
)

st.plotly_chart(fig, width='stretch')


# YESTERDAY'S TOP 5

df_top5 = pd.read_csv("data/gold_top5.csv")

st.markdown(f"#### Top 5 performers from {formatted_date}")
st.write(df_top5)


# YESTERDAY'S BOTTOM 5

df_bottom5 = pd.read_csv("data/gold_bottom5.csv")

st.markdown(f"#### Bottom 5 performers from {formatted_date}")
st.write(df_bottom5)