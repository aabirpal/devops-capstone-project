from flask import jsonify, request, make_response, abort
from service.models import Account
from service.common import status
from . import app


@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="OK"), status.HTTP_200_OK


@app.route("/", methods=["GET"])
def index():
    return jsonify(
        name="Account REST API Service",
        version="1.0"
    ), status.HTTP_200_OK


@app.route("/accounts", methods=["POST"])
def create_accounts():
    if request.headers.get("Content-Type") != "application/json":
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    account = Account()
    account.deserialize(request.get_json())
    account.create()

    return (
        jsonify(account.serialize()),
        status.HTTP_201_CREATED,
        {"Location": f"/accounts/{account.id}"}
    )


@app.route("/accounts", methods=["GET"])
def list_accounts():
    accounts = Account.all()
    return jsonify([a.serialize() for a in accounts]), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    account = Account.find(account_id)

    if not account:
        abort(status.HTTP_404_NOT_FOUND)

    return jsonify(account.serialize()), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    if request.headers.get("Content-Type") != "application/json":
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    account = Account.find(account_id)

    if not account:
        abort(status.HTTP_404_NOT_FOUND)

    account.deserialize(request.get_json())
    account.update()

    return jsonify(account.serialize()), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    account = Account.find(account_id)

    if account:
        account.delete()

    return "", status.HTTP_204_NO_CONTENT


def check_content_type(media_type):
    content_type = request.headers.get("Content-Type")

    if content_type != media_type:
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)