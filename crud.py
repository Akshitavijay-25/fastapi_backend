from sqlalchemy.orm import Session
from models import User, FoodItem, Order
from schemas import UserCreate, FoodItemCreate, OrderCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_food_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(FoodItem).offset(skip).limit(limit).all()

def create_food_item(db: Session, food_item: FoodItemCreate):
    db_food_item = FoodItem(**food_item.dict())
    db.add(db_food_item)
    db.commit()
    db.refresh(db_food_item)
    return db_food_item

def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
