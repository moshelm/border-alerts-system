def sorting_alerts(data: list[dict]):
    for alert in data:
        if alert['weapons_count'] > 0 or alert['distance_from_fence_m'] <= 50 or alert['people_count'] >= 8 or alert['vehicle_type'] == 'truck':
            alert['priority'] = 'URGENT'
        elif (alert['vehicle_type'] == "jeep" and alert['people_count'] >= 3) or (alert['distance_from_fence_m'] <=150 and alert['people_count'] >= 4):
            alert['priority'] = 'URGENT'
        else:
            alert['priority'] = 'NORMAL'
