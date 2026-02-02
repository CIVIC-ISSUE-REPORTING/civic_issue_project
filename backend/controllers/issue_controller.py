from ml_inference.issue_classifier import IssueClassifier
from ml_inference.severity_detector import SeverityDetector
from ml_inference.spam_detector import SpamDetector
from services.routing_service import RoutingService

class IssueController:
    def __init__(self):
        self.classifier = IssueClassifier()
        self.severity_detector = SeverityDetector()
        self.spam_detector = SpamDetector()
        self.routing_service = RoutingService()
    
    def get_all_issues(self):
        # TODO: Implement database query
        return []
    
    def get_issue_by_id(self, issue_id):
        # TODO: Implement database query
        return None
    
    def create_issue(self, data, user_id):
        # Classify issue
        category = self.classifier.predict(data.get('description'))
        
        # Detect severity
        severity = self.severity_detector.predict(
            data.get('description'),
            data.get('image')
        )
        
        # Check for spam
        is_spam = self.spam_detector.is_spam(data.get('description'))
        
        if is_spam:
            return {'error': 'Issue flagged as spam'}, 400
        
        # Route to appropriate department
        department = self.routing_service.route_issue(category, data.get('location'))
        
        issue = {
            'user_id': user_id,
            'category': category,
            'severity': severity,
            'department': department,
            **data
        }
        
        # TODO: Save to database
        return issue
    
    def update_issue(self, issue_id, data):
        # TODO: Implement update logic
        return None
    
    def delete_issue(self, issue_id):
        # TODO: Implement delete logic
        return False
