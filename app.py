from flask import Flask
import secrets
import string
from logging.config import dictConfig
from utils.logs import create_log_id
from services.v2.generate_password import generate_password_bp
from services.v2.password_customize import password_customize_bp
from services.v2.password_exact import password_exact_bp
from services.v2.password_length import password_length_bp
from flask_cors import CORS

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
CORS(app)

@app.route("/generate-password", methods=['GET'])
def generate_simple_password():
    """Endpoint generate default password long=16 chars"""
    log_id = create_log_id()
    app.logger.info(f'LOGID: {log_id}')
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(16):
        password += secrets.choice(characters)

    app.logger.info(f'LOGID: {log_id} - OK(password="{password}") - HTTP 200')
    return {"password": password},200

import services.password_length
import services.password_customize
import services.password_exact

app.register_blueprint(generate_password_bp, url_prefix="/v2")
app.register_blueprint(password_customize_bp, url_prefix="/v2")
app.register_blueprint(password_exact_bp, url_prefix="/v2")
app.register_blueprint(password_length_bp, url_prefix="/v2")