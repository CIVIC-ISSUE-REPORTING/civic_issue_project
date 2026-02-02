#!/usr/bin/env python3
"""
Database seeding script for Civic Issue Management System
Creates sample data for testing and development
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from database.db import db
from database.models import User, Issue, Comment, Notification
from datetime import datetime, timedelta
import random

# Sample data
CATEGORIES = ['road', 'water', 'electricity', 'sanitation', 'parks', 'other']
SEVERITIES = ['low', 'medium', 'high', 'critical']
STATUSES = ['pending', 'in_progress', 'resolved', 'closed']

SAMPLE_ISSUES = [
    {'title': 'Pothole on Main Street', 'category': 'road', 'severity': 'high'},
    {'title': 'Water leak near Park Avenue', 'category': 'water', 'severity': 'medium'},
    {'title': 'Street light not working', 'category': 'electricity', 'severity': 'low'},
    {'title': 'Overflowing garbage bin', 'category': 'sanitation', 'severity': 'medium'},
    {'title': 'Damaged park bench', 'category': 'parks', 'severity': 'low'},
]

def create_users():
    """Create sample users"""
    users = [
        User(
            email='admin@civic.com',
            password_hash='hashed_password',  # In production, use proper hashing
            name='Admin User',
            phone='1234567890',
            role='admin'
        ),
        User(
            email='worker1@civic.com',
            password_hash='hashed_password',
            name='Worker One',
            phone='1234567891',
            role='worker'
        ),
        User(
            email='citizen1@civic.com',
            password_hash='hashed_password',
            name='Citizen One',
            phone='1234567892',
            role='citizen'
        ),
    ]
    
    for user in users:
        db.session.add(user)
    
    db.session.commit()
    print(f"Created {len(users)} users")
    return users

def create_issues(users):
    """Create sample issues"""
    issues = []
    citizen = [u for u in users if u.role == 'citizen'][0]
    
    for i, sample in enumerate(SAMPLE_ISSUES):
        issue = Issue(
            user_id=citizen.id,
            title=sample['title'],
            description=f"Description for {sample['title']}",
            category=sample['category'],
            severity=sample['severity'],
            status=random.choice(STATUSES),
            latitude=40.7128 + random.uniform(-0.1, 0.1),
            longitude=-74.0060 + random.uniform(-0.1, 0.1),
            address=f"{random.randint(1, 999)} Street {i+1}",
            deadline=datetime.now() + timedelta(days=random.randint(1, 14))
        )
        issues.append(issue)
        db.session.add(issue)
    
    db.session.commit()
    print(f"Created {len(issues)} issues")
    return issues

def create_comments(users, issues):
    """Create sample comments"""
    comments = []
    for issue in issues[:3]:
        comment = Comment(
            issue_id=issue.id,
            user_id=random.choice(users).id,
            content=f"Sample comment for issue {issue.id}"
        )
        comments.append(comment)
        db.session.add(comment)
    
    db.session.commit()
    print(f"Created {len(comments)} comments")

def seed_database():
    """Main seeding function"""
    print("Starting database seeding...")
    
    # Clear existing data (optional - be careful in production!)
    # db.drop_all()
    # db.create_all()
    
    users = create_users()
    issues = create_issues(users)
    create_comments(users, issues)
    
    print("Database seeding complete!")

if __name__ == '__main__':
    # Import app to get application context
    from app import app
    
    with app.app_context():
        seed_database()
