from fastapi import APIRouter
from dal import *
from redis_connection import manager
router = APIRouter()

def data_to_fastapi(data:list):
    for doc in data:
        doc['_id'] = str(doc['_id'])

@router.get("/analytics/alerts-by-border-and-priority")
def alerts_by_border():
    data = manager.get("id_result")
    if data is None:
        data = alerts_border
        manager.setex("id_result",10,data)
    data_to_fastapi(data)
    return data

@router.get("/analytics/top-urgent-zones")
def top_urgent_zones():
    data = manager.get("id_result")
    if data is None:
        data =urgent_zones() 
        manager.setex("id_result",10,data)
    data_to_fastapi(data)
    return data
@router.get("/analytics/distance-distribution")
def distance_distribution():
    data = manager.get("id_result")
    if data is None:
        data = distance() 
        manager.setex("id_result",10,data)
    data_to_fastapi(data)
    return data
@router.get("/analytics/low-visibility-high-activity")
def low_visibility_high_activity():
    data = manager.get("id_result")
    if data is None:
        data = visibility_activity() 
        manager.setex("id_result",10,data)
    data_to_fastapi(data)
    return data
@router.get("/analytics/hot-zones")
def get_hot_zones():
    data = manager.get("id_result")
    if data is None:
        data = hot_zones() 
        manager.setex("id_result",10,data)
    data_to_fastapi(data)
    return data