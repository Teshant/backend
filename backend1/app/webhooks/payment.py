from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import Depends
from app.db.session import get_db
from app.db.models import Order

router = APIRouter()

@router.post("/payment")
async def payment_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.json()
    order_id = payload.get("order_id")

    if not order_id:
        raise HTTPException(status_code=400, detail="Invalid payload")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = "paid"
    await db.commit()

    return {"status": "payment processed"}
