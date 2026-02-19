import mongo_connection as mongo

coll = mongo.collection

def alerts_border():
    query = [{'$group':{"_id":"$border","total":{"$sum":"$priority"}}}]        
    res = coll.aggregate(query)
    return  res
def urgent_zones():
    query = [{"$group":{"_id":"$zone","total":{"$sum":{"$priority":'URGENT'}}},
             },{"$sort":"total"},{"$limit":5}]
    res = coll.aggregate(query)
    return res

def distance():
    query = [{"$group":{"_id":"$"},
             "$count":{""}}]
    res = coll.aggregate(query)
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