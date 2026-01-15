import pytest

@pytest.mark.asyncio
async def test_register_and_login(client):
    await client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "123456"
    })

    res = await client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "123456"
    })

    assert res.status_code == 200
    assert "access_token" in res.json()
