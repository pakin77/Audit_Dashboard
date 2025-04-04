import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df_logs = pd.read_csv("data/system_logs.csv", parse_dates=["timestamp"])
df_transactions = pd.read_csv("data/transactions.csv", parse_dates=["timestamp"])

# ------------------ UI ------------------
st.set_page_config(page_title="Data Audit Dashboard", layout="wide")
st.title("🛡️ Data Audit Dashboard")
st.markdown("Monitor system activity and transactions to support internal audit analysis.")

# ------------------ Sidebar Filters ------------------
st.sidebar.header("🔎 Filter Options")

log_event_filter = st.sidebar.multiselect(
    "Select Log Event Types:",
    options=df_logs["event_type"].unique(),
    default=df_logs["event_type"].unique()
)

high_value_threshold = st.sidebar.slider(
    "Transaction High-Value Threshold:",
    min_value=100,
    max_value=5000,
    value=3000,
    step=100
)

# ------------------ Filtered Data ------------------
df_logs_filtered = df_logs[df_logs["event_type"].isin(log_event_filter)]
df_high_value = df_transactions[df_transactions["amount"] > high_value_threshold]

# ------------------ Log Event Summary ------------------
st.header("📋 System Log Events")
log_counts = df_logs_filtered["event_type"].value_counts().reset_index()
log_counts.columns = ["event_type", "count"]

fig_log = px.bar(log_counts, x="event_type", y="count", title="Log Events Summary")
st.plotly_chart(fig_log, use_container_width=True)

# ------------------ Transaction Overview ------------------
st.header("💰 Transactions")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Transaction Amount Distribution")
    fig_trans = px.histogram(df_transactions, x="amount", nbins=30, title="Transaction Histogram")
    st.plotly_chart(fig_trans, use_container_width=True)

with col2:
    st.subheader("High-Value Transactions")
    st.write(f"Transactions above ${high_value_threshold:,}")
    st.dataframe(df_high_value.sort_values(by="amount", ascending=False), use_container_width=True)
