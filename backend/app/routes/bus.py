from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload

from ..database import get_db
from ..models import Bus

router = APIRouter(prefix="/api/buses", tags=["buses"])

@router.get("/")
def get_buses(db: Session = Depends(get_db)):
    buses = (
        db.query(Bus)
        .options(joinedload(Bus.routes))
        .all()
    )
    return buses

@router.get("/{bus_id}")
def get_bus(bus_id: int, db: Session = Depends(get_db)):
    bus = (
        db.query(Bus)
        .options(joinedload(Bus.routes))
        .filter(Bus.id == bus_id)
        .first()
    )
    if not bus:
        return {"error": "Bus not found"}
    return bus