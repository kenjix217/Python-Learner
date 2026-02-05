from flask import Flask, jsonify
import os

# Initialize Flask app
app = Flask(__name__)

# Load configuration from environment variables
# In production, these are set in the OS or container
APP_ENV = os.environ.get('APP_ENV', 'development')
DEBUG_MODE = os.environ.get('DEBUG', 'False').lower() == 'true'
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-key')

# Configure app
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DEBUG'] = DEBUG_MODE

print(f"Starting app in {APP_ENV} mode...")

@app.route('/')
def home():
    """Root endpoint"""
    return jsonify({
        "message": "Welcome to the Production Ready App!",
        "environment": APP_ENV,
        "status": "online"
    })

@app.route('/health')
def health_check():
    """Health check endpoint for load balancers"""
    return jsonify({
        "status": "healthy",
        "version": "1.0.0"
    }), 200

if __name__ == '__main__':
    # Get port from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
