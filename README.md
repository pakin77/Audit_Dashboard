# 🛡️ Data Audit Dashboard

A simulation project for internal audit and IT risk analysis, built with **Python**, **Streamlit**, and **Plotly**.  
This dashboard allows auditors and data analysts to explore log and transaction data to detect anomalies, high-value risks, and unusual user behaviors.

## 📌 Project Overview

This project mimics a real-world internal audit scenario using synthetic data:
- `system_logs.csv`: User login, failed access, and data modification activities  
- `transactions.csv`: Simulated financial transactions requiring approvals

The goal is to demonstrate how data analytics can enhance audit effectiveness, uncover risks, and support governance.

## ✨ Features

- 📋 **System Log Analytics** – View and filter user activities (login, failed login, file changes)
- 💰 **Transaction Review** – Highlight high-value transactions above threshold
- 📈 **Interactive Visuals** – Real-time graphs with Plotly
- 🔍 **Anomaly Filtering** – Use sidebar to customize insights

## 🗃️ Sample Data

| File                | Description                              |
|---------------------|------------------------------------------|
| `data/system_logs.csv` | Simulated log events (user activity)    |
| `data/transactions.csv` | Simulated financial transactions        |

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/data-audit-dashboard.git
cd data-audit-dashboard
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
.env\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard

```bash
streamlit run app/dashboard.py
```

## 🛠 Tech Stack
- **Python 3.10+**
- **Streamlit** – lightweight app framework
- **Pandas** – data processing
- **Plotly** – interactive charts
- **Faker** – mock data generator

## 👤 Author
**[Pakin Lerdwichitwatthana]**  
Internal Auditor with 17+ years of experience, passionate about data analytics, Python, and continuous process improvement.
- 💼 LinkedIn: [linkedin.com/in/pakin-lerdwichitwatthana-39401ab5]


