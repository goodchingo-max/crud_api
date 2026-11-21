# FastAPI + PostgreSQL CRUD & Testing

Ushbu loyiha **"FastAPI API'ni tekshirish — qatorma-qator darslik"** va **"FastAPI + PostgreSQL CRUD"** darsliklari asosida to'liq yig'ilgan va sozlangan.

## Loyiha tuzilmasi

```
crud_api/
├── app/
│   ├── __init__.py
│   ├── database.py       # DB ulanish, sessiya, get_db
│   ├── models.py         # SQLAlchemy ItemModel jadvali
│   ├── schemas.py        # Pydantic v2 sxemalari (ItemCreate, ItemUpdate, ItemResponse)
│   ├── crud.py           # Baza operatsiyalari (get, create, update, delete)
│   └── main.py           # FastAPI routerlari va endpointlar
├── tests/
│   ├── __init__.py
│   ├── conftest.py       # Fixture'lar, override_get_db, alohida shop_test_db
│   ├── test_birinchi.py  # 1-avtomatik test
│   └── test_items.py     # 15 ta CRUD va parametrize validatsiya testlari
├── .env                  # PostgreSQL ulanish satri (shop_db)
├── pytest.ini            # pytest qidiruv va pythonpath sozlamalari
├── requests.http         # VS Code REST Client so'rovlar to'plami
├── requirements.txt      # Barcha bog'liqliklar
└── README.md
```

## Ishga tushirish (Uvicorn)

Virtual muhitni faollashtiring va serverni yoqing:

```powershell
cd C:\Users\user\.gemini\antigravity\scratch\crud_api
.\.venv\Scripts\activate
uvicorn app.main:app --reload
```

Brauzerda Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Testlarni ishga tushirish

Barcha testlarni tekshirish (16 ta test):

```powershell
.\.venv\Scripts\pytest -v
```

100% test qamrovini (coverage) ko'rish:

```powershell
.\.venv\Scripts\pytest --cov=app --cov-report=term-missing
```

HTML hisobot yaratish:

```powershell
.\.venv\Scripts\pytest --cov=app --cov-report=html
start htmlcov/index.html
```

