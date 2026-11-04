from fastapi import Query
from fastapi import FastAPI, status, HTTPException
from app.schemas import EventCreate
app = FastAPI(title="TicketFlow API")

events = []
@app.get("/health")
def heal_check():
    return { "status": "ok" }

@app.post("/events", status_code=status.HTTP_201_CREATED)
def booking_create(event: EventCreate):
    new_event = {
        "id": len(events) + 1,
        "name": event.name,
        "price": event.price,
        "available_quantity": event.available_quantity,
    }
    events.append(new_event)

    return new_event

@app.get("/events")
def get_events():
    return events

@app.get("/events/{event_id}")
def get_event(event_id: int):
    # TODO 1: Duyệt qua danh sách events
    for event in events:
        if event["id"] == event_id:
            return event
    raise HTTPException(
        status_code = 404,
        detail = f"Không tìm thấy sự kiện có ID là {event_id}"

    )

@app.get("/events/filter")
def filter_events(min_price: int = Query(ge=0)):
    # TODO: Trả về các sự kiện có giá >= min_price
    return [event for event in events if event["price"]>=min_price]

@app.put("/events/{event_id}")
def update_event(
    event_id: int,
    data: EventCreate
):
    for event in events:
        if event["id"] == event_id:
            event["name"] = data.name
            event["price"] = data.price
            event["available_quantity"] = data.available_quantity
        return event
    raise HTTPException(
        status_code=404,
        detail="Event not found"
    )

@app.delete("/events/{event_id}")
def delete_event(
    event_id: int
):
    for event in events:
        if event["id"] == event_id:
            events.remove(event)
            raise HTTPException(
                status_code=200,
                detail="Event deleted successfully"
            )
    raise HTTPException(
        status_code=404,
        detail="Không tìm thấy sự kiện cần xóa"
    )