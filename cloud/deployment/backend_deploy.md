# Backend Deployment Guide

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Redis server
- AWS account (for S3)
- Firebase account (for notifications)

## Deployment Options

### Option 1: Heroku

```bash
# Login to Heroku
heroku login

# Create app
heroku create civic-issue-api

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Add Redis
heroku addons:create heroku-redis:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY=your_secret_key
heroku config:set JWT_SECRET_KEY=your_jwt_secret

# Deploy
git push heroku main
```

### Option 2: AWS EC2

```bash
# SSH into EC2 instance
ssh -i key.pem ubuntu@ec2-ip

# Install dependencies
sudo apt update
sudo apt install python3-pip nginx postgresql redis-server

# Clone repository
git clone https://github.com/your-repo/civic-issue-project.git

# Setup virtual environment
cd civic-issue-project/backend
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Setup Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Option 3: Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

```bash
# Build image
docker build -t civic-issue-api .

# Run container
docker run -p 5000:5000 civic-issue-api
```

## Environment Variables

```
SECRET_KEY=
JWT_SECRET_KEY=
DATABASE_URL=
MONGO_URI=
REDIS_URL=
AWS_ACCESS_KEY=
AWS_SECRET_KEY=
S3_BUCKET=
FIREBASE_CREDENTIALS=
```

## Post-Deployment

1. Run database migrations
2. Create admin user
3. Test all endpoints
4. Monitor logs
5. Set up auto-scaling
