# 🛡️ Fraud Detection Pipeline

This project implements a complete fraud detection system, from data ingestion and processing to feature engineering, machine learning modeling, and evaluation. The goal is to accurately identify potentially fraudulent financial transactions using historical transaction data and engineered behavioral features.

## 📂 Project Structure
fraud-detection/
├── dags/ # Airflow DAGs for data ingestion
├── docker/ # Docker setup for local environment
├── notebooks/ # EDA, feature engineering, and modeling
├── scripts/ # Python utilities for feature generation and DB interaction
├── data/ # Raw .pkl data files
├── db/ # PostgreSQL setup
├── requirements.txt # Python dependencies
└── README.md # Project overview


## ⚙️ Technologies Used

- **Python 3.10+**
- **Docker & Docker Compose**
- **Apache Airflow** – for orchestrating data ingestion
- **PostgreSQL** – for structured storage
- **Pandas, NumPy** – for data manipulation
- **Scikit-learn, XGBoost** – for machine learning
- **DBeaver** – for querying the database
- **Matplotlib, Seaborn** – for data visualization

