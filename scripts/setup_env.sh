#!/bin/bash

# Setup script for Civic Issue Management System

echo "Setting up Civic Issue Management System..."

# Check Python version
python_version=$(python3 --version 2>&1 | grep -Po '(?<=Python )(.+)')
echo "Python version: $python_version"

# Create virtual environment for backend
echo "Creating virtual environment..."
cd backend
python3 -m venv venv
source venv/bin/activate

# Install backend dependencies
echo "Installing backend dependencies..."
pip install -r requirements.txt

# Setup database
echo "Setting up database..."
# TODO: Add database initialization commands

# Generate secret keys
echo "Generating secret keys..."
export SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
export JWT_SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')

# Create .env file
cat > .env << EOF
SECRET_KEY=$SECRET_KEY
JWT_SECRET_KEY=$JWT_SECRET_KEY
DATABASE_URL=postgresql://user:password@localhost:5432/civic_issues
MONGO_URI=mongodb://localhost:27017/civic_issues
REDIS_URL=redis://localhost:6379/0
DEBUG=True
EOF

echo ".env file created"

# Setup frontend
echo "Setting up frontend..."
cd ../frontend
# flutter pub get  # Uncomment if using Flutter

echo "Setup complete!"
echo "To run the backend:"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python app.py"
