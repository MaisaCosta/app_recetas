from flask import Flask
import re

app = Flask(__name__)
app.secret_key = "esto es secreto"

BASE_DATOS = "bd_recetas"
EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
