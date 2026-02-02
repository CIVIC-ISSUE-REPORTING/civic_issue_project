import numpy as np
import tensorflow as tf

class IssueClassifier:
    def __init__(self, model_path='models/issue_classifier.h5'):
        try:
            self.model = tf.keras.models.load_model(model_path)
        except:
            self.model = None
        
        self.categories = [
            'road', 'water', 'electricity', 
            'sanitation', 'parks', 'other'
        ]
    
    def preprocess_text(self, text):
        """Preprocess text for model input"""
        # TODO: Implement text preprocessing
        return text
    
    def predict(self, description, image=None):
        """Classify issue based on description and optional image"""
        if self.model is None:
            # Fallback to keyword-based classification
            return self.keyword_classify(description)
        
        # TODO: Implement ML-based classification
        processed_text = self.preprocess_text(description)
        # prediction = self.model.predict(processed_text)
        return 'road'  # Mock response
    
    def keyword_classify(self, description):
        """Simple keyword-based classification fallback"""
        description_lower = description.lower()
        
        if any(word in description_lower for word in ['road', 'pothole', 'street', 'highway']):
            return 'road'
        elif any(word in description_lower for word in ['water', 'pipe', 'leak', 'drainage']):
            return 'water'
        elif any(word in description_lower for word in ['electricity', 'power', 'light', 'outage']):
            return 'electricity'
        elif any(word in description_lower for word in ['garbage', 'trash', 'waste', 'sanitation']):
            return 'sanitation'
        elif any(word in description_lower for word in ['park', 'garden', 'tree']):
            return 'parks'
        else:
            return 'other'
