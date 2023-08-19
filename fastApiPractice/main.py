from fastapi import FastAPI, HTTPException, Depends, status
from typing import Optional, Annotated
from pydantic import BaseModel;
import model
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

# Data Validation
class BatterCellsBase(BaseModel):
    battery_id: int
    cell_number: str
    capacity: str
    min_voltage: str     
    max_voltage: str
    current_SoC: str
    current_voltage: str

class BatteryBase(BaseModel):
    name: int
    description: str
    manufacturer: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated(Session, Depends(get_db))

  
        







