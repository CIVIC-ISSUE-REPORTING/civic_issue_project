# Backend - Civic Issue Management API

Flask/FastAPI backend server for the civic issue management system.

## Technology Stack

- Flask / FastAPI
- PostgreSQL / MongoDB
- Redis (caching)
- Celery (background tasks)

## Features

- RESTful API
- Authentication & Authorization
- Issue management
- Admin controls
- Worker assignment
- AI-powered routing and classification
- Real-time notifications

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

## API Endpoints

- `/api/auth/*` - Authentication
- `/api/issues/*` - Issue management
- `/api/admin/*` - Admin operations
- `/api/workers/*` - Worker operations
