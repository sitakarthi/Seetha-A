import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
GEMINI_MODEL=os.getenv("GEMINI_MODEL")
LOCAL_EXPLAINER=os.getenv("LOCAL_EXPLAINER")
LOCAL_EXPLAINER_MODEL=os.getenv("LOCAL_EXPLAINER_MODEL")
MAX_INPUT_CHARS=os.getenv("MAX_INPUT_CHARS")