from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from database.db import init_db
from routes import auth_routes, issue_routes, admin_routes, worker_routes

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize database
init_db(app)

# Register blueprints
app.register_blueprint(auth_routes.bp, url_prefix='/api/auth')
app.register_blueprint(issue_routes.bp, url_prefix='/api/issues')
app.register_blueprint(admin_routes.bp, url_prefix='/api/admin')
app.register_blueprint(worker_routes.bp, url_prefix='/api/workers')

@app.route('/')
def index():
    return jsonify({
        'message': 'Civic Issue Management API',
        'version': '1.0.0',
        'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
