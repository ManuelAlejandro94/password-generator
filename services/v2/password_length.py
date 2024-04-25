import secrets, string
from flask import Blueprint, current_app as app
from utils.logs import create_log_id
from api_responses.responses import ResponseOk as Ok

password_length_bp = Blueprint("/generate-password-length", __name__)

@password_length_bp.route("/generate-password-length/<len>", methods=['GET'])
def generate_exact_password(len):
    """Endpoint generate default password long=variable"""
    log_id = create_log_id()
    app.logger.info(f'LOGID: {log_id} - Lenght: {len}')
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(int(len)):
        password += secrets.choice(characters)

    app.logger.info(f'LOGID: {log_id} - OK(password="{password}") - HTTP 200')
    return Ok.with_results(
        code=0,
        message="Password successful generated",
        result=password
    )