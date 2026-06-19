from flask import jsonify, request, make_response, abort
from service.models import Account
from service.common import status
from . import app


<<<<<<< HEAD
############################################################
# Health Endpoint
############################################################

@app.route("/health")
=======
@app.route("/health", methods=["GET"])
>>>>>>> 5feb753 (add security headers and cors)
def health():
    return jsonify(status="OK"), status.HTTP_200_OK


<<<<<<< HEAD
######################################################################
# GET INDEX
######################################################################

@app.route("/")
def index():
    """Root URL response"""
    return (
        jsonify(
            name="Account REST API Service",
            version="1.0",
        ),
        status.HTTP_200_OK,
    )


######################################################################
# CREATE A NEW ACCOUNT
######################################################################

@app.route("/accounts", methods=["POST"])
def create_accounts():
    """
    Creates an Account
    This endpoint will create an Account based the data in the body that is posted
    """
    app.logger.info("Request to create an Account")
    check_content_type("application/json")
=======
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
>>>>>>> 5feb753 (add security headers and cors)

    account = Account()
    account.deserialize(request.get_json())
    account.create()

<<<<<<< HEAD
    message = account.serialize()

    location_url = url_for("get_accounts", account_id=account.id, _external=True)

    return make_response(
        jsonify(message),
=======
    serialized = account.serialize()

    # REQUIRED by tests: Location header must exist
    location_url = f"/accounts/{account.id}"

    return (
        jsonify(serialized),
>>>>>>> 5feb753 (add security headers and cors)
        status.HTTP_201_CREATED,
        {"Location": location_url},
    )


<<<<<<< HEAD
######################################################################
# LIST ALL ACCOUNTS
######################################################################

=======
>>>>>>> 5feb753 (add security headers and cors)
@app.route("/accounts", methods=["GET"])
def list_accounts():
    accounts = Account.all()
<<<<<<< HEAD

    account_list = [account.serialize() for account in accounts]

    return jsonify(account_list), status.HTTP_200_OK


######################################################################
# READ AN ACCOUNT
######################################################################

=======
    return jsonify([a.serialize() for a in accounts]), status.HTTP_200_OK


>>>>>>> 5feb753 (add security headers and cors)
@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    account = Account.find(account_id)

    if not account:
<<<<<<< HEAD
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id [{account_id}] could not be found.",
        )
=======
        abort(status.HTTP_404_NOT_FOUND)
>>>>>>> 5feb753 (add security headers and cors)

    return jsonify(account.serialize()), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
<<<<<<< HEAD
    """
    Update an Account
    """
    account = Account.find(account_id)

    if not account:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id [{account_id}] could not be found.",
        )
=======
    if not request.headers.get("Content-Type") == "application/json":
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    account = Account.find(account_id)

    if not account:
        abort(status.HTTP_404_NOT_FOUND)
>>>>>>> 5feb753 (add security headers and cors)

    account.deserialize(request.get_json())
    account.update()

    return jsonify(account.serialize()), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
<<<<<<< HEAD
    """
    Delete an Account
    """
=======
>>>>>>> 5feb753 (add security headers and cors)
    account = Account.find(account_id)

    if account:
        account.delete()

<<<<<<< HEAD
    return "", status.HTTP_204_NO_CONTENT


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################

def check_content_type(media_type):
    """Checks that the media type is correct"""
    content_type = request.headers.get("Content-Type")

    if content_type and content_type == media_type:
        return

    app.logger.error("Invalid Content-Type: %s", content_type)

    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {media_type}",
    )
=======
    return "", status.HTTP_204_NO_CONTENT
>>>>>>> 5feb753 (add security headers and cors)
