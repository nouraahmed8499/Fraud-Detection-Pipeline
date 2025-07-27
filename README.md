# Fraud Detection Pipeline

This project implements a complete fraud detection system, from data ingestion and processing to feature engineering, machine learning modeling, and evaluation. The goal is to accurately identify potentially fraudulent financial transactions using historical transaction data and engineered behavioral features.

## Project Structure
fraud-detection-pipeline/\
├── dags/ # Airflow DAGs for data ingestion\
├── notebooks/ # EDA, feature engineering, and modeling\
|    ├── EDA.ipynb       # EDA + feature engineering in one place\
|    ├── Feature Engineering, Modeling and Evaluation.ipynb.ipynb # Baseline and advanced models, Metrics, plots, final notes\
├── scripts/ # Python utilities for feature generation and DB interaction\
├── data/ # Raw .pkl data files\
├── logs/ # Airflow logs\
├── .gitignore # ignoring unnecessary files and folders\
├── docker-compose.yaml # Docker setup for local environment\
├── requirements.txt # Python dependencies\
└── README.md # Project overview


## Technologies Used

- **Python 3.10+**
- **Docker & Docker Compose**
- **Apache Airflow** – for orchestrating data ingestion
- **PostgreSQL** – for structured storage
- **Pandas, NumPy** – for data manipulation
- **Scikit-learn, XGBoost** – for machine learning
- **DBeaver** – for querying the database
- **Matplotlib, Seaborn** – for data visualization


## Quick Start

### Prerequisites
- Docker and Docker Compose installed
- At least 4GB available RAM
- Python 3.10+ (for local development)

### Setup and Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fraud-detection-pipeline
   ```

2. **Build and start the Docker environment**
   ```bash
   docker-compose up --build
   ```

3. **Access the services**
   - **Airflow UI**: http://localhost:8080 (admin/admin)
   - **PostgreSQL**: localhost:5432 (fraud_db/fraud_user/fraud_pass)

4. **Run the data pipeline**
   - Navigate to Airflow UI
   - Enable and trigger the `fraud_detection_dag`
   - Monitor pipeline execution in the logs

### Data Pipeline Flow

1. **Data Ingestion**: Reads multiple .pkl files containing transaction data
2. **Data Aggregation**: Combines data into a unified DataFrame
3. **Data Validation**: Checks for data quality and consistency
4. **Database Storage**: Writes processed data to PostgreSQL
5. **Feature Engineering**: Generates behavioral and temporal features
6. **Model Training**: Trains fraud detection models
7. **Evaluation**: Assesses model performance and generates reports

## Key Features

### Engineered Features
- **Temporal Features**: Weekend and night transaction indicators
- **Customer Behavior**: Rolling window statistics (1, 7, 30 days)


### Model Performance
- **Precision**: Focus on minimizing false positives
- **Recall**: Capturing actual fraud cases
- **F1-Score**: Balanced performance metric
- **ROC-AUC**: Overall classification performance

## Database Schema

The PostgreSQL database contains the main transaction table with:
- Transaction identifiers and timestamps
- Customer and terminal information
- Transaction amounts and fraud labels
- Engineered behavioral features

## Development Workflow

1. **Data Exploration**: Use `EDA.ipynb` for initial analysis
2. **Feature Development**: Implement new features in`notebooks\Feature Engineering, Modeling and Evaluation.ipynb`
3. **Model Experimentation**: Test models in `notebooks\Feature Engineering, Modeling and Evaluation.ipynb`
4. **Pipeline Integration**: Update Airflow DAG for production workflow
5. **Evaluation**: Analyze results in `notebooks\Feature Engineering, Modeling and Evaluation.ipynb`

## Monitoring and Logging

- **Airflow Logs**: Available in `logs/` directory and Airflow UI
- **Database Monitoring**: Use DBeaver for data quality checks
- **Model Metrics**: Tracked in evaluation notebooks

## Deployment Considerations

- **Scalability**: Pipeline designed for horizontal scaling
- **Real-time Processing**: Architecture supports streaming data ingestion
- **Model Versioning**: Framework for model lifecycle management
- **Alert System**: Configurable thresholds for fraud detection

## Contributing

1. Follow PEP 8 style guidelines
2. Add unit tests for new features
3. Update documentation for significant changes
4. Test pipeline end-to-end before committing

## Troubleshooting

### Common Issues
- **Memory Issues**: Increase Docker memory allocation
- **Database Connection**: Verify PostgreSQL container is running
- **Airflow DAG Errors**: Check logs in Airflow UI
- **Feature Engineering**: Ensure proper date parsing and sorting

### Useful Commands
```bash
# View running containers
docker-compose ps

# Check container logs
docker-compose logs [service-name]

# Restart specific service
docker-compose restart [service-name]

# Clean up containers
docker-compose down -v
```
