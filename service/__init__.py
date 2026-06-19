import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

from service import config
from service.common import log_handlers

app = Flask(__name__)
app.config.from_object(config)

# CRITICAL: stop Flask redirect behavior
app.url_map.strict_slashes = False
app.config["PREFERRED_URL_SCHEME"] = "http"

# Security Headers
talisman = Talisman(app, force_https=False)

# CORS
CORS(app)

from service import routes, models  # noqa: F401 E402
from service.common import error_handlers, cli_commands  # noqa: F401 E402

log_handlers.init_logging(app, "gunicorn.error")

try:
    models.init_db(app)
except Exception as error:
    app.logger.critical("%s: Cannot continue", error)
    sys.exit(4)
 