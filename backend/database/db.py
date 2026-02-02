from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

db = SQLAlchemy()
mongo_client = None
mongo_db = None

def init_db(app):
    """Initialize database connections"""
    # PostgreSQL
    db.init_app(app)
    
    # MongoDB
    global mongo_client, mongo_db
    mongo_client = MongoClient(app.config['MONGO_URI'])
    mongo_db = mongo_client.get_database()
    
    with app.app_context():
        db.create_all()

def get_mongo_db():
    """Get MongoDB database instance"""
    return mongo_db
