import re

class SpamDetector:
    def __init__(self):
        self.spam_patterns = [
            r'\b(viagra|cialis|pharmacy)\b',
            r'\b(click here|limited time)\b',
            r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+){3,}',
            r'\b(free money|earn \$\d+)\b'
        ]
    
    def is_spam(self, text):
        """Detect if text is spam"""
        text_lower = text.lower()
        
        # Check for spam patterns
        for pattern in self.spam_patterns:
            if re.search(pattern, text_lower):
                return True
        
        # Check for excessive repetition
        if self.has_excessive_repetition(text):
            return True
        
        # Check for all caps (except short text)
        if len(text) > 20 and text.isupper():
            return True
        
        return False
    
    def has_excessive_repetition(self, text):
        """Check if text has excessive character or word repetition"""
        # Check for repeated characters
        if re.search(r'(.)\1{5,}', text):
            return True
        
        # Check for repeated words
        words = text.split()
        if len(words) > 5:
            unique_words = set(words)
            if len(unique_words) / len(words) < 0.3:
                return True
        
        return False
    
    def get_spam_score(self, text):
        """Calculate spam score (0-1)"""
        score = 0.0
        
        for pattern in self.spam_patterns:
            if re.search(pattern, text.lower()):
                score += 0.3
        
        if self.has_excessive_repetition(text):
            score += 0.4
        
        return min(score, 1.0)
