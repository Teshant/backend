from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.orders.service import create_order

router = APIRouter()

@router.post("/")
async def place_order(
    db: AsyncSession = Depends(get_db),
    user = Depends(get_current_user),
):
    order = await create_order(db, user.id)
    return {"order_id": order.id, "status": order.status}
