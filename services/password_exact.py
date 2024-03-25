from flask import  request
from app import app
from utils.logs import create_log_id
from utils.validate import validate_params
from utils.responses import ResponseErrorBadRequest as BadRequest, ResponseOk as Ok
import string
import secrets
import random


@app.route("/generate-password-exact", methods=['GET', 'POST'])
def generate_exact_password():
    """Endpoint generate password with the exact elements"""
    busqueda_params = request.get_json()
    PARAMS = [
        "uppercase",
        "lowercase",
        "digits",
        "special_characters"
    ]

    log_id = create_log_id()
    app.logger.info(f'LOGID: {log_id} - Params: {busqueda_params}')

    dif_params = validate_params(params=PARAMS, request=busqueda_params)
    if dif_params:
        app.logger.info(
            f'LOGID: {log_id} - BadRequest(error=-1, message="Request missing params", details="Params: {dif_params}") - HTTP 422')
        return BadRequest.with_results(
            error=-1,
            message="Request missing params",
            details=f"Params: {dif_params}"
        )

    digits = "".join(secrets.choice(string.digits) for _ in range(busqueda_params["digits"]))
    punctuation = "".join(secrets.choice(string.punctuation) for _ in range(busqueda_params["special_characters"]))
    uppercase = "".join(secrets.choice(string.ascii_uppercase) for _ in range(busqueda_params["uppercase"]))
    lowercase = "".join(secrets.choice(string.ascii_lowercase) for _ in range(busqueda_params["lowercase"]))
    characters = digits + punctuation + uppercase + lowercase
    password = "".join(random.sample(characters, len(characters)))

    app.logger.info(f'LOGID: {log_id} - OK(password="{password}") - HTTP 200')
    return Ok.with_results(
        code=0,
        message="Password successful generated",
        result=password
    )