###########################################################
#*  Erstellen Sie eine Klasse WGS84Coord welche folgende 
#*  Attribute hat:  
#*  _longitude (=Länge) 
#*  _latitude (=Breite)  
#*  latitude hat den Wertebereich [-90,90] und longitude 
#*  hat den Bereich [-180,180].
###########################################################

class WGS84_Koord():
    def __init__(self):
        self._longitude = 0
        self._latitude = 0
    
    def get_latitude(self):
        return self._latitude
    
    def get_longitude(self):
        return self._longitude
    
    def set_latitude(self, lat):
        if lat in range(-90, 90):
            self._latitude = lat
        else:
            print("Invalid latitude")

    def set_longitude(self, lot):
        if lot in range(-180, 180):
            self._longitude = lot
        else:
            print("Invalid longitude")


koord = WGS84_Koord()
print(koord.get_latitude())
print(koord.get_longitude())

koord.set_longitude(45)
koord.set_latitude(45)
print(koord.get_latitude())
print(koord.get_longitude())