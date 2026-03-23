#!/usr/bin/env python3
"""
Web Scraper Oast
Flask-based web application
"""

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

class WebScraperOastAPI:
    """Web web scraper oast built with Python"""
    
    def __init__(self):
        self.app = app
        self.setup_routes()
    
    def setup_routes(self):
        @app.route('/')
        def home():
            return jsonify({
                "service": "WebScraperOast",
                "status": "running",
                "timestamp": datetime.now().isoformat()
            })
        
        @app.route('/health')
        def health():
            return jsonify({"status": "healthy"})
    
    def run(self, host='0.0.0.0', port=5000):
        self.app.run(host=host, port=port, debug=False)

if __name__ == "__main__":
    api = web-scraper-oastAPI()
    api.run()
