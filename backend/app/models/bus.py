from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image_url = Column(String, nullable=True)

    routes = relationship(
        "BusRoute", back_populates="bus",
        cascade="all, delete-orphan", order_by="BusRoute.stop_order"
    )

class BusRoute(Base):
    __tablename__ = "bus_routes"

    id = Column(Integer, primary_key=True, index=True)

    bus_id = Column(Integer, ForeignKey("buses.id"), 
                    nullable=False)

    stop_order = Column(Integer, nullable=False)
    stop_name = Column(String, nullable=False)

    bus = relationship("Bus", back_populates="routes")