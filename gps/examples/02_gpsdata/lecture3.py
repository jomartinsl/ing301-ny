import haversine

class GPSPoint:
    def __init__(self, time: str, lat : float, long : float , height: float):
        self.time = time
        self.lat = lat
        self.long = long
        self.height = height

    today = "lørdag"
    def say_hi():
        print("Hi!")


def distance_to(self, other : GPSPoint):
    
    return haversine.distance(self.lat, self. long, other.lat, other.long)



point = GPSPoint(
    time="2017-08-13T08:57:57.000", 
    lat = 60.376988, 
    long = 5.227082, 
    height = 105.5)

point_b = GPSPoint(
    time="2017-08-13T09:04:11.000", 
    lat = 60.361153, 
    long = 5.243403, 
    height = 70.4
)

result = point.distance_to(point_b)
print("Distansen mellom punkt a til punkt b : ", result)


