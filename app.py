from flask import Flask, request
from db_library import get_header_id, insert_detail_into_db

app = Flask(__name__)


@app.route("/detail", methods=["POST", "GET"])
def insert_detail():
    error = None
    if request.method == "POST":
        return str(
            insert_detail_into_db(
                get_header_id(request.form["identificador"]), request.form["idCatalogo"]
            )
        )
    return "<p>Invalid</p>"
