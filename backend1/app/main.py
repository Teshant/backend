from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.orders.routes import router as orders_router
from app.webhooks.payment import router as webhook_router

app = FastAPI(title="FastAPI Backend Project")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(orders_router, prefix="/orders", tags=["Orders"])
app.include_router(webhook_router, prefix="/webhooks", tags=["Webhooks"])
