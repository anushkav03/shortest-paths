# i don't anticipate needing more classes, but just in case
# all classes will be defined here

class StopNode():
    def __init__(self, stop_name, stop_lat, stop_lon):
        self.name = stop_name
        self.lat = stop_lat
        self.lon = stop_lon
        # later: arrival departure