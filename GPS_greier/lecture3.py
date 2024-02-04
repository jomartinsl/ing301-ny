

class GPSPoint:
    def __init__(self, time, lat, long , height):
        self.time = time
        self.lat = lat
        self.long = long
        self.height = height
        print("Dette er en konstuktør! :D")

    today = "lørdag"
    def say_hi():
        print("Hi!")



point = GPSPoint(
    time="2017-08-13T08:57:57.000", 
    lat = 60.376988, 
    long = 5.227082, 
    height = 105.5)

