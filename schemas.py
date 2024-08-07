from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class FoodItemBase(BaseModel):
    name: str
    description: str
    price: float

class FoodItemCreate(FoodItemBase):
    pass

class FoodItem(FoodItemBase):
    id: int

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    user_id: int
    food_item_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    user: User
    food_item: FoodItem

    class Config:
        from_attributes = True
