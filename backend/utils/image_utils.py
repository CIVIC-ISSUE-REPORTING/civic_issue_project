from PIL import Image
import os
import uuid

class ImageUtils:
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_SIZE = (1920, 1080)
    
    @staticmethod
    def allowed_file(filename):
        """Check if file extension is allowed"""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ImageUtils.ALLOWED_EXTENSIONS
    
    @staticmethod
    def save_image(file, upload_folder):
        """Save and process uploaded image"""
        if not ImageUtils.allowed_file(file.filename):
            raise ValueError('Invalid file type')
        
        # Generate unique filename
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4()}.{ext}"
        filepath = os.path.join(upload_folder, filename)
        
        # Open and resize image
        img = Image.open(file)
        img.thumbnail(ImageUtils.MAX_SIZE, Image.Resampling.LANCZOS)
        
        # Save image
        img.save(filepath, optimize=True, quality=85)
        
        return filename
    
    @staticmethod
    def delete_image(filepath):
        """Delete image file"""
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False
    
    @staticmethod
    def compress_image(image_path, quality=85):
        """Compress image to reduce file size"""
        img = Image.open(image_path)
        img.save(image_path, optimize=True, quality=quality)
