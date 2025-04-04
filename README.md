# 🛡️ Data Audit Dashboard
การทำโปรเจกต์ผ่าน VS Code

## 🚀 Getting Started

✅ STEP 1: เตรียมเครื่องมือ
1. ติดตั้ง Python
ตรวจสอบด้วย:
python --version

2. ติดตั้ง VS Code
แนะนำให้ติดตั้ง Extension:

✅ Python (โดย Microsoft)

✅ Pylance

✅ Jupyter (ถ้าจะใช้ notebook)

✅ Git

---------
🗂️ STEP 2: สร้างโปรเจกต์ใน D:\
เปิด VS Code → กด File > Open Folder...

เลือก D:\ → กด New Folder ตั้งชื่อว่า data-audit-dashboard

คลิก Select Folder

-------
🧪 STEP 3: เปิด Terminal แล้วสร้าง Virtual Environment
ใน VS Code → กด `Ctrl + `` เพื่อเปิด Terminal

python -m venv venv
.\venv\Scripts\activate

เมื่อ activate สำเร็จ จะมี (venv) ขึ้นหน้า prompt
---------
📦 STEP 4: ติดตั้งไลบรารีที่ใช้
pip install streamlit pandas plotly

แล้วสร้างไฟล์ requirements.txt:
streamlit
pandas
plotly

สามารถใช้ Ctrl + N เพื่อสร้างไฟล์ใหม่ แล้วบันทึกชื่อว่า requirements.txt
------------
📁 STEP 5: สร้างโฟลเดอร์และไฟล์โปรเจกต์
คลิกขวาใน Explorer → New Folder → สร้าง 2 โฟลเดอร์:

app/

data/

คลิกขวาที่ app/ → New File → ตั้งชื่อ dashboard.py

สร้างไฟล์ README.md

----------
📥 STEP 6: วาง Mock Data
ดาวน์โหลดจากลิงก์:

📥 system_logs.csv

📥 transactions.csv

วางไว้ในโฟลเดอร์: D:\data-audit-dashboard\data\
-----------
🧠 STEP 7: วางโค้ดใน app/dashboard.py
Start->//

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

//<-End
----------------
🚀 STEP 8: รันโปรเจกต์ผ่าน VS Code
ใน Terminal VS Code:

streamlit run app/dashboard.py

✅ จะเปิดเบราว์เซอร์แสดง Dashboard ของคุณทันที

ถ้าไม่เปิด ต้อง Activate virtual environment ก่อน

พิมพ์คำสั่ง .\venv\Scripts\activate ใน Terminal
จากนั้นจะเห็น (venv) ขึ้นที่ด้านหน้าของบรรทัดคำสั่ง
แล้วลองรันอีกครั้ง:
streamlit run app/dashboard.py

ใน Terminal จะปรากฎข้อความ
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8502
  Network URL: http://192.168.1.125:8502

แล้วจะแสดง dashboard ในหน้าต่างใหม่

-----------------


## 🛠 Data Mock
- **https://faker.readthedocs.io/en/master/**


## 👤 Author
**[Pakin Lerdwichitwatthana]**  
Internal Auditor with 17+ years of experience, passionate about data analytics, Python, and continuous process improvement.
- 💼 LinkedIn: [linkedin.com/in/pakin-lerdwichitwatthana-39401ab5]


