from fastapi import APIRouter
from app.utils.geo import haversine
from app.schemas.location import DistanceRequest, DistanceResponse


router = APIRouter()


@router.post("/calculate-distance/", response_model=DistanceResponse)
def calculate_distance(data: DistanceRequest):

    # вызов функции из utils
    dist = haversine(data.lat1, data.lon1, data.lat2, data.lon2)
    return {"distance_km": dist}