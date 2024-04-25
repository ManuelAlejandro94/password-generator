import secrets
import string
from flask import Blueprint, current_app as app, request
from utils.logs import create_log_id
from api_responses.responses import ResponseErrorBadRequest as BadRequest, ResponseOk as Ok
from utils.validate import validate_params

password_customize_bp = Blueprint("/generate-password-customize", __name__)

@password_customize_bp.route("/generate-password-customize", methods=['GET', 'POST'])
def password_customize():
    """Endpoint generate default password for customized counts of elements"""
    busqueda_params = request.get_json()
    PARAMS = [
        "len",
        "letters",
        "digits",
        "special_characters"
    ]

    log_id = create_log_id()
    app.logger.info(f'LOGID: {log_id} - Lenght: {len}')

    dif_params = validate_params(params=PARAMS, request=busqueda_params)
    if dif_params:
        app.logger.info(
            f'LOGID: {log_id} - BadRequest(error=-1, message="Request missing params", details="Params: {dif_params}") - HTTP 422')
        return BadRequest.with_results(
            error=-1,
            message="Request missing params",
            details=f"Params: {dif_params}"
        )

    if busqueda_params["len"] < (
            busqueda_params["letters"] + busqueda_params["digits"] + busqueda_params["special_characters"]):
        app.logger.info(
            f'LOGID: {log_id} - BadRequest(error=-2, message="The length can\'t be less than the letters, digits and special characters sum") - HTTP 422')
        return BadRequest.without_results(
            error=-2,
            message="The length can't be less than the letters, digits and special characters sum"
        )

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    while True:
        password = "".join(secrets.choice(characters) for _ in range(busqueda_params["len"]))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isalpha() for c in password) >= busqueda_params["letters"]
                and sum(c.isdigit() for c in password) >= busqueda_params["digits"]
                and sum(not c.isalpha() and not c.isdigit() for c in password) >= busqueda_params["special_characters"]
        ):
            break

    app.logger.info(f'LOGID: {log_id} - OK(password="{password}") - HTTP 200')
    return Ok.with_results(
        code=0,
        message="Password successful generated",
        result=password
    )