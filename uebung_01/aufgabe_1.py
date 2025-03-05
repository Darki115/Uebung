###########################################################
#*  Aufgabe 1
#*  Erstellen Sie eine Klasse Vector3, welche einen 
#*  dreidimensionalen Vektor repräsentiert. Über den 
#*  Konstruktor werden die Komponenten x, y und z definiert. 
#*  Wird nichts angegeben, so wird ein Null-Vektor erstellt.
#*  Entwickeln Sie eine Methode len, welche die Länge des 
#*  Vektors berechnet.  Mit einer Instanz von Vector3 soll 
#*  die Klasse getestet werden. 
###########################################################


class vector3():
    def __init__(self, _x, _y, _z):
        self._x = 0
        self._y = 0
        self._z = 0

    def leange(self):
        return (self._x**2 + self._y**2 + self._z**2)**0.5
    
    def set_x(self, _x):
        self._x = float(input("x = "))
    def set_y(self, _y):
        self._y = float(input("y = "))
    def set_z(self, _z):
        self._z = float(input("z = "))
    
vect = vector3(0, 0, 0)
vect.set_x(0)
vect.set_y(0)
vect.set_z(0)
print(vect.leange())