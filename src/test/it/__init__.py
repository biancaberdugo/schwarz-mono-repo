from pathlib import Path

from dotenv import load_dotenv

BASE_PATH = Path(__file__).parent.parent.parent
env_file = BASE_PATH / "api" / ".env" / ".local.env"

load_dotenv(dotenv_path=env_file)
