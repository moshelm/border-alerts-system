import mongo_connection as mongo

coll = mongo.collection

def alerts_border():
    query = [{"$group":{"_id":"$border",
"total_event":{"$count":{}},
"urgent_only_count": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$priority", "URGENT"]}, 
                        1, 
                        0]}},
"normal_only_count": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$priority", "NORMAL"]}, 
                        1, 
                        0]}}}},
            {"$sort":{"urgent_only_count": -1}}]        
    result = list(coll.aggregate(query))
    return  result

def urgent_zones():
    query = [
        {
            "$match":{"priority":"URGENT"}
        }
        ,
        {
            "$group":{
                "_id":"$zone", "total_urgent_alerts": {"$sum":-1}
            }
        },
        {
            "$project":{
                "_id":1,
                "zone":"$_id",
                "total_urgent_alerts":1}
        },
        {
            "$sort":{"total_urgent_alerts":1}
        },
        {
            "$limit":5
        }

    ]
    
    res = list(coll.aggregate(query))
    return res

def distance():
    query = [
        {
            "$facet":{
                "closer":[
                    {
                        "$match":{"distance_from_fence_m":{"$gte":1,"$lte":300}}
                     },
                     {"$count":"total"}
                ],
                "medium":[
                    {
                        "$match":{"distance_from_fence_m":{"$gte":301,"$lte":800}}
                     },
                     {"$count":"total"}
                ],
                "far":[
                    {
                        "$match":{"distance_from_fence_m":{"$gte":801,"$lte":1500}}
                     },
                     {"$count":"total"}
                ],
            }
        }
    ]
    res = list(coll.aggregate(query))
    return res

def visibility_activity():
    query = [{"$group":{"_id":"$"},
             "$count":{""}}]
    res = coll.aggregate(query)
    return res
def hot_zones():
    query = [{"$group":{"_id":"$"},
             "$count":{""}}]
    res = coll.aggregate(query)
    return res