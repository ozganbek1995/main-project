from geopy.distance import geodesic
from .models import * 
def get_distance(point_a: tuple, point_b: tuple):
    distance_km = float(0.00)
    if point_a and point_b:
        distance_km = geodesic(point_a, point_b).kilometers
    return round(distance_km, 3)


def get_object_by_radius(user_coordinate):
    matches_obj = None
    try:
        qs = Shop.objects.all()
        print('in qs.....', qs)
        if qs.exists():
            distances = []
            for obj in qs:
                distance = get_distance(point_a=(obj.latitude, obj.longitude), point_b=user_coordinate)
                print('distanse..........', distance)
                distances.append({"id": obj.id, "m": distance})
            min_distance = min(distances, key=lambda x: x["m"])
            print("min_distance.......", min_distance)
            # matches_obj = Object.objects.get(id=min_distance['id'])
            if min_distance['m'] < 50:  # m
                matches_obj = Shop.objects.get(id=min_distance['id'])
            else:
                raise 'Buyerda obyekt joylashuvi noto\'gri, iltimos obyektga yaqinroq joydan harakat qilib ko\'ring'

        return matches_obj
    except Exception as e:
        print("get_package_by_radius.......", e.args)
        return None