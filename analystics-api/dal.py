import mongo_connection as mongo

coll = mongo.collection

def alerts_border():
    query = 
    projection = {"border":1,"priority":1}     
    res = coll.find(query)
    return  res
def urgent_zones():
    query = {"$group":{"$_id":"$border","priority":},
             "$count":{""}}
    res = coll.find(query)
    return res
def distance():
    query = {"$group":{"$_id":"$border","priority":},
             "$count":{""}}
    res = coll.find(query)
    return res
def visibility_activity():
    query = {"$group":{"$_id":"$border","priority":},
             "$count":{""}}
    res = coll.find(query)
    return res
def hot_zones():
    query = {"$group":{"$_id":"$border","priority":},
             "$count":{""}}
    res = coll.find(query)
    return res