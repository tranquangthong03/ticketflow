from pydantic import BaseModel, Field

class EventCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: int = Field(ge=0)
    available_quantity: int = Field(ge=0)