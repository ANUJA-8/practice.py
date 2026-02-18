class Fridge:
    # color=null
    # size=null
    # style=null

    def __init__(self, color, size, style):
        self.color = color
        self.size = size
        self.style = style

    def cooling(self):
        return "The fridge is cooling your food."
    def storage(self):
        return "The fridge is storing your food."
    def icing(self):
        return "The fridge is making ice cubes."
    
my_godrje=Fridge("white", "large", "double-door")
print(my_godrje.cooling())
