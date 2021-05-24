from dotenv import load_dotenv
import os

environPath = None

flask_env = os.environ.get('FLASK_ENV')
environPath = f"{'development' if flask_env is None else flask_env}.env"

load_dotenv(environPath)