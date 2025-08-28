from flask import Flask, render_template
from .auth import auth_bp
from .analysis import analysis_bp
import os
import logging
from dotenv import load_dotenv

def create_app():
    """
    Application Factory Pattern: Creates and configures the Flask app and Celery.
    """
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = os.getenv("SECRET_KEY")
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

    # Setup logging
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(analysis_bp, url_prefix='/')

    @app.errorhandler(413)
    def too_large(e):
        return render_template("index.html", summary="❌ File too large. Max size 20MB."), 413

    return app