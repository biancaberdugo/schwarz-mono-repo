from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(__file__).parent / "api" / ".env" / ".local.env"
load_dotenv(dotenv_path=ENV_PATH)
