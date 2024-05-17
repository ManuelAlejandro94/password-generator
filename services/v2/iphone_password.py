from flask import Blueprint, current_app as app
from utils.logs import create_log_id
from api_responses.responses import ResponseOk as Ok
import string, secrets

iphone_password_bp = Blueprint('iphone-password', __name__)


@iphone_password_bp.route('/iphone-password', methods=['GET'])
def new_person():
    """Endpoint for generate password like iPhone"""

    log_id = create_log_id()
    app.logger.info(f'LOGID: {log_id} - GET: /iphone-password')

    # Insert here your logical
    # Password example: X9r2-jk8p-Q5m4-vN7z
    characters = string.ascii_letters + string.digits
    password = ""

    for _ in range(4):
        for _ in range(4):
            password += secrets.choice(characters)
        password += "-"

    password = password[:-1]

    app.logger.info(f'LOGID: {log_id} - OK(code=0, message="Password generated", result={password}) - HTTP 200')
    return Ok.with_results(
        code=0,
        message="Password generated",
        result=password
    )
