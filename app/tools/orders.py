from pydantic import BaseModel, Field, ValidationError
from data.fake_db import ORDERS
import json

class GetOrdersArgs(BaseModel):
    customer_name: str = Field(min_length=1)
    limit: int = Field(default=5, ge=1, le=50)

def get_orders(customer_name: str, limit: int = 5) -> str:
    result = [order for order in ORDERS if order['customer'] == customer_name]
    result = result[:limit]
    if not result:
        return f"Заказы для клиента {customer_name} не найдены."
    text = json.dumps(result, ensure_ascii=False)
    if text:
        return text
    return 'No info'