from app import app
from utils.logs import create_log_id
import string
import secrets

@app.route("/generate-password-length/<len>", methods=['GET'])
def generate_password_length(len):
    """Endpoint generate default password long=variable"""
    log_id = create_log_id()
    app.logger.info(f'LOGID: {log_id} - Lenght: {len}')
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(int(len)):
        password += secrets.choice(characters)

    app.logger.info(f'LOGID: {log_id} - OK(password="{password}") - HTTP 200')
    return {"password": password}, 200