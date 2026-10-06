import json
from pathlib import Path

from app.database import Base, engine, SessionLocal
from app.models import Bus, BusRoute

DATA_FILE = Path(__file__).parent / "data" / "buses.json"

def parse_stop(raw: str):
    # "1\tGabtoli (গাবতলি)" -> (1, "Gabtoli")
    order, name = raw.split("\t", 1)
    name = name.split(" (")[0].strip()
    return int(order), name

def seed_buses():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        buses = json.loads(DATA_FILE.read_text(encoding="utf-8"))

        for item in buses:
            if db.query(Bus).filter(Bus.name == item["bus_name"]).first():
              print(f"skip {item['bus_name']} (already exists)")
              continue 

            bus = Bus(name=item["bus_name"], image_url=item.get("image"))

            for raw in item["routes"]:
                order, name = parse_stop(raw)
                bus.routes.append(BusRoute(stop_order=order, stop_name=name))

            db.add(bus)
            print(f"added {bus.name} ({len(bus.routes)} stop)")

        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    seed_buses()