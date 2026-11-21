import pytest


def test_mahsulot_yaratish(client):
    response = client.post("/items/", json={"name": "Olma", "price": 12000})

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Olma"
    assert data["price"] == 12000
    assert "id" in data


def test_bosh_royxat(client):
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == []


def test_bitta_mahsulot(client, olma):
    response = client.get(f"/items/{olma['id']}")
    assert response.status_code == 200
    assert response.json() == olma


def test_mavjud_bolmagan_mahsulot(client):
    response = client.get("/items/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Mahsulot topilmadi"}


def test_pagination(client):
    for i in range(15):
        client.post("/items/", json={"name": f"Mahsulot {i}", "price": 1000 + i})

    assert len(client.get("/items/").json()) == 10
    assert len(client.get("/items/?limit=5").json()) == 5
    assert len(client.get("/items/?skip=10").json()) == 5


def test_put_toliq_yangilash(client, olma):
    response = client.put(f"/items/{olma['id']}", json={"name": "Nok", "price": 15000})
    assert response.status_code == 200
    assert response.json()["name"] == "Nok"
    assert response.json()["price"] == 15000


def test_patch_faqat_narx(client, olma):
    response = client.patch(f"/items/{olma['id']}", json={"price": 9000})
    assert response.status_code == 200
    assert response.json()["price"] == 9000
    assert response.json()["name"] == "Olma"


def test_put_mavjud_bolmagan(client):
    response = client.put("/items/99999", json={"name": "Nok", "price": 15000})
    assert response.status_code == 404


def test_ochirish(client, olma):
    response = client.delete(f"/items/{olma['id']}")
    assert response.status_code == 204

    response = client.get(f"/items/{olma['id']}")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "yuborilgan",
    [
        {"name": "Olma"},
        {"price": 12000},
        {"name": "A", "price": 12000},
        {"name": "Olma", "price": -5},
        {"name": "Olma", "price": 0},
        {"name": "Olma", "price": "qimmat"},
    ],
)
def test_notogri_malumot(client, yuborilgan):
    response = client.post("/items/", json=yuborilgan)
    assert response.status_code == 422

