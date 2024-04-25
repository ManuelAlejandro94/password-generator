import secrets
import string
from flask import Blueprint
from utils.logs import create_log_id
from flask import current_app as app
from api_responses.responses import ResponseOk as Ok

generate_password_bp = Blueprint('generate-password', __name__)

@generate_password_bp.route('/generate-password', methods=['GET'])
def generate_password():
    """Endpoint generate default password long=16 chars"""
    log_id = create_log_id()
    app.logger.info(f'LOGID: {log_id}')
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(16):
        password += secrets.choice(characters)

    app.logger.info(f'LOGID: {log_id} - OK(password="{password}") - HTTP 200')
    return Ok.with_results(
        code=0,
        message="Password success generated",
        result=password
    )