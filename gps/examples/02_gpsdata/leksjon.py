import haversine

class GPSPoint:
    #innhold
    
    #Konstruktør
    def __init__(self, time : str, lat: float, long: float, height: float):
        self.time = time
        self.lat = lat
        self.long = long
        self.height = height

    def avstand_til(self, other : 'GPSPoint'):
        return haversine.distance(self.lat, self.long, other.lat, other.long )


point = GPSPoint(time ="2017-08-13T09:06:11.000",
                 lat=60.367743,
                 long=5.249715,
                 height=53.7)


point2 = GPSPoint(time="2017-08-13T09:12:16.000",
                  lat=60.388325,
                  long=5.276237,
                  height=27.3)

resultat = point.avstand_til(point2)
print(f"Distansen mellom a og b : {resultat}",resultat)