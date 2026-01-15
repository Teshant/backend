import pytest

@pytest.mark.asyncio
async def test_create_order(client):
    login = await client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "123456"
    })

    token = login.json()["access_token"]

    res = await client.post(
        "/orders/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200
