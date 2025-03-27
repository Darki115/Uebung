import math

class Perimeter():
    def __init__(self):
        pass

    def dist(self, point1, point2):
        return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

    def perimeter(self, points):
        perimeter = 0.0
        num_points = len(points)

        if num_points < 3: #* Für kreis
            self.zentrum = points[0]
            self.radius = self.dist(points[0], points[1])
            perimeter = 2 * math.pi * self.radius
        else:
            for i in range(num_points):
                current_point = points[i]
                next_point_index = (i + 1) % num_points
                next_point = points[next_point_index]
                perimeter += self.dist(current_point, next_point)

        return perimeter

class Dreieck():
    def __init__(self, punkte):
        self.name = "Dreieck" #* Name of the class
        self.L_punkt = punkte
    
    def Umfang(self):
        return Perimeter().perimeter(self.L_punkt)

    def __str__(self):
        return f"name: {self.name} Umfang: {self.Umfang()}, Punkte: {self.L_punkt}"

class Rechteck():
    def __init__(self, punkte):
        self.name = "Rechteck" #* Name of the class
        self.L_punkt = punkte
    
    def Umfang(self):
        return Perimeter().perimeter(self.L_punkt)

    def __str__(self):
        return f"name: {self.name} Umfang: {self.Umfang()}, Punkte: {self.L_punkt}"
    
class Polygon():
    def __init__(self, punkte):
        self.name = "Polygon" #* Name of the class
        self.L_punkt = punkte
    
    def Umfang(self):
        return Perimeter().perimeter(self.L_punkt)

    def __str__(self):
        return f"name: {self.name} Umfang: {self.Umfang()}, Punkte: {self.L_punkt}"
    

class Kreis():
    def __init__(self, punkte):
        self.name = "Kreis" #* Name of the class
        self.L_punkt = punkte
        self.radius = Perimeter().dist(punkte[0], punkte[1])
        self.zentrum = punkte[0]
    
    def Umfang(self):
        return Perimeter().perimeter(self.L_punkt)

    def __str__(self):
        return f"name: {self.name} Umfang: {self.Umfang()}, Zentrum: {self.zentrum}, Radius: {self.radius}"
    

drei = Dreieck([(1, 1), (4, 1), (2, 3)])
print(drei)

rech = Rechteck([(0, 0), (0, 5), (5, 5), (5, 0)])
print(rech) 

poly = Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)])
print(poly)

kreis = Kreis([(0, 0), (0, 5)])
print(kreis)
