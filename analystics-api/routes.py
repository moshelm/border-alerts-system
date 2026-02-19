from fastapi import APIRouter
from dal import *

router = APIRouter()

def data_to_fastapi(data:list):
    for doc in data:
        doc['_id'] = str(doc['_id'])

@router.get("/analytics/alerts-by-border-and-priority")
def alerts_by_border():
    data = alerts_border
    data_to_fastapi(data)
    return data

@router.get("/analytics/top-urgent-zones")
def top_urgent_zones():
    data =urgent_zones() 
    data_to_fastapi(data)
    return data
@router.get("/analytics/distance-distribution")
def distance_distribution():
    data = distance() 
    data_to_fastapi(data)
    return data
@router.get("/analytics/low-visibility-high-activity")
def low_visibility_high_activity():
    data = visibility_activity() 
    data_to_fastapi(data)
    return data
@router.get("/analytics/hot-zones")
def get_hot_zones():
    data = hot_zones() 
    data_to_fastapi(data)
    return data