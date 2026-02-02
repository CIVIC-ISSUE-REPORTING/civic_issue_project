import os
from datetime import timedelta

class Config:
    # Flask config
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    
    # Database config
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://user:password@localhost:5432/civic_issues'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # MongoDB config
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/civic_issues')
    
    # JWT config
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # Redis config
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # File upload config
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # ML model paths
    MODEL_PATH = 'ml_inference/models/'
    
    # AWS S3 config
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', '')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', '')
    S3_BUCKET = os.getenv('S3_BUCKET', 'civic-issues-bucket')
    
    # Firebase config
    FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS', '')
