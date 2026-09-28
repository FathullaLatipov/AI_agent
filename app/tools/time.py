from datetime import datetime
from langchain_core.tools import tool

@tool
def get_current_time():
    """Возвращает текущее локальное время."""
    return datetime.now().strftime("%H:%M:%S")
