
from pydantic import BaseModel, Field



class DistanceRequest(BaseModel):
    
    lat1: float = Field(..., description="широта первой точки", ge=-90, le=90)
    lon1: float = Field(..., description="долгота первой точки", ge=-180, le=180)

    lat2: float = Field(..., description="широта второй точки", ge=-90, le=90)
    lon2: float = Field(..., description="долгота второй точки", ge=-180, le=180)



class DistanceResponse(BaseModel):

    distance_km: float = Field(..., description="Расстояние между точками в километрах")
    
