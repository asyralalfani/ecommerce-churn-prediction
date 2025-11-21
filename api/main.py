"""
FastAPI application for churn prediction
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

# Initialize FastAPI app
app = FastAPI(
    title="E-commerce Churn Prediction API",
    description="API for predicting customer churn probability",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "churn-prediction-api",
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "E-commerce Churn Prediction API",
        "docs": "/docs",
        "health": "/health"
    }

# Prediction endpoint (placeholder)
@app.post("/predict")
async def predict_churn(data: dict):
    """
    Predict customer churn probability
    
    This is a placeholder endpoint.
    Will be implemented after model training.
    """
    return {
        "status": "success",
        "message": "Model not yet trained. Coming soon!",
        "churn_probability": None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)