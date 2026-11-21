from pydantic import BaseModel, ConfigDict, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)


class ItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    price: float | None = Field(default=None, gt=0)


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

    model_config = ConfigDict(from_attributes=True)

