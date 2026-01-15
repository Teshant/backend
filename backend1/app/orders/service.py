from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Order

async def create_order(db: AsyncSession, user_id: int):
    order = Order(user_id=user_id)
    db.add(order)
    await db.commit()
    return order
