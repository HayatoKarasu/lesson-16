class Turtle(object):
    
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
        return self.y
        
    
    def go_down(self):
        self.y -= self.s
        return self.y
    
    
    def go_left(self):
        self.x -= self.s
        return self.x
        
        
    def go_right(self):
        self.x += self.s
        return self.x
    
    
    def evolve(self):
        self.s += 1
        return self.s
        
        
    def degrade(self):
        if self.s <= 0:
            print("Ошибка!")
        else:
            self.s -= 1
            return self.s
            
            
    def count_moves(self, x2, y2):
        return self.x - x2 // self.s, self.y - y2 // self.s
             
                
dvig = Turtle(14, 5, 38)

print(dvig.go_up())

print(dvig.go_down())

print(dvig.go_left())

print(dvig.go_right())

print(dvig.evolve())

print(dvig.degrade())

print(dvig.count_moves(32, 52))
