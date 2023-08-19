from sqlalchemy import Boolean, Column, Integer, String
from database import BASE

class Battery(BASE):
    __tablename__ = 'batteries'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(500))
    manufacturer = Column(String(50))

class BatteryCells(BASE):
    __tablename__ = 'battery_cells'

    id = Column(Integer, primary_key=True, index=True)
    battery_id = Column(Integer)
    cell_number = Column(String(500))
    capacity = Column(String(50))
    min_voltage = Column(String(50))
    max_voltage = Column(String(50))
    current_SoC = Column(String(50))
    current_voltage = Column(String(50))



