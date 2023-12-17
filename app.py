from flask import Flask
import secrets
import string

app = Flask(__name__)

@app.route("/generate-password", methods=['GET'])
def generate_simple_passwprd():
    """Endpoint generate default password long=16 chars"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(16):
        password += secrets.choice(characters)
    return {"password": password},200