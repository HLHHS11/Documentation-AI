import os

from dotenv import load_dotenv


load_dotenv(verbose=True)

dotenv_path = os.path.join(os.path.dirname(__file__), '../', '.env')
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
