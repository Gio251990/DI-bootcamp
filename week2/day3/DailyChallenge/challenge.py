import math

class Circle:
    def __init__(self, radius):
        self.radius = radius        
    
    @property
    def circle_area(self):
        self.circle_area = math.pi*self.radius**2
        
    def __str__(self):
        self.circumference = f"The circumference of the circle is {math.pi*2*self.radius}"
        return self.circumference
    
    def __add__(self, second_circle):
        total_radius = self.radius + second_circle.radius
        return Circle(total_radius)
    
    def __gt__ (self,second_circle):
        return self.radius > second_circle.radius
    
    def __eq__(self, second_circle):
        return self.radius == second_circle.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __repr__(self):
        self.circumference = f"{math.pi*2*self.radius}"
        return self.circumference


c1 = Circle(10)
c2 = Circle(15)
c3 = Circle(8)
c4 = Circle(17)
list = [c1, c2, c3, c4]
print(c1+c2)
print(c1>c2)
print(c1==c2)
print(sorted(list))






    
    

    
    
    

    
    