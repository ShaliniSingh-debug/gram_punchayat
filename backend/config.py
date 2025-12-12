from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()
# print(f"Loading environment variables from: {env_path}")
@dataclass
class Settings:
              secret_key = os.getenv("SECRET_KEY")
settings = Settings()
