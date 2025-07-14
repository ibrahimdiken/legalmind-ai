from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)

    from app.routes     import main
    from app.mcp.server import mcp_bp

    app.register_blueprint(main)
    app.register_blueprint(mcp_bp, url_prefix="/mcp")

    return app
