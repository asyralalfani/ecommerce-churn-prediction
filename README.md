# 🎯 E-commerce Customer Churn Prediction

## Overview
Machine Learning project to predict customer churn in e-commerce using Deep Learning.

## Problem Statement
E-commerce companies lose 20-30% of customers annually. This project builds a predictive system to identify at-risk customers early, enabling proactive retention strategies.

## Tech Stack
- **ML/DL:** TensorFlow, Scikit-learn
- **API:** FastAPI
- **UI:** Streamlit
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose

## Quick Start

### Prerequisites
- Docker Desktop installed

### Setup & Run
```bash
# 1. Clone repository
git clone https://github.com/asyralalfani/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction

# 2. Download dataset
# Place dataset in data/raw/ folder
https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction


# 3. Build and start services
docker-compose up --build

# 4. Access services
# Jupyter: http://localhost:8888
# API: http://localhost:8000/docs
# Streamlit: http://localhost:8501
```

### Stop Services
```bash
docker-compose down
```

## Development Workflow

### Data Analysis
```bash
# Start Jupyter only
docker-compose up jupyter

# Access at http://localhost:8888
```

### API Development
```bash
# Start API + Database
docker-compose up postgres api

# Test at http://localhost:8000/docs
```

### Full Stack
```bash
# Start all services
docker-compose up
```
## Author
Moch Asyral Difa Alfani
