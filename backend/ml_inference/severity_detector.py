import numpy as np
from PIL import Image

class SeverityDetector:
    def __init__(self, model_path='models/severity_model.h5'):
        try:
            # self.model = tf.keras.models.load_model(model_path)
            self.model = None
        except:
            self.model = None
        
        self.severity_levels = ['low', 'medium', 'high', 'critical']
    
    def predict(self, description, image_path=None):
        """Detect severity based on description and image"""
        if self.model is None:
            return self.rule_based_severity(description)
        
        # TODO: Implement ML-based severity detection
        return 'medium'  # Mock response
    
    def rule_based_severity(self, description):
        """Rule-based severity detection fallback"""
        description_lower = description.lower()
        
        critical_keywords = ['emergency', 'dangerous', 'urgent', 'life-threatening', 'fire']
        high_keywords = ['severe', 'major', 'serious', 'hazardous']
        medium_keywords = ['moderate', 'significant', 'noticeable']
        
        if any(word in description_lower for word in critical_keywords):
            return 'critical'
        elif any(word in description_lower for word in high_keywords):
            return 'high'
        elif any(word in description_lower for word in medium_keywords):
            return 'medium'
        else:
            return 'low'
    
    def analyze_image(self, image_path):
        """Analyze image to assess severity"""
        # TODO: Implement image-based severity detection
        pass
