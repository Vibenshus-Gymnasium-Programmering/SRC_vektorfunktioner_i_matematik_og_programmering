# [[file:Praesentation.org::*Cirklen][Cirklen:1]]
import arcade
import math
BREDDE = 800
HOEJDE = 600
SPORLAENGDE = 200

class Cirkel:
    def __init__(self, centrum, radius, vinkelhastighed, vinkel, farve, sporlaengde = None):
        self.centrum = centrum
        self.radius = radius
        self.vinkelhastighed = vinkelhastighed
        self.vinkel = vinkel
        self.punkt = centrum[0] + self.radius * math.cos(self.vinkel), centrum[1] + self.radius * math.sin(self.vinkel)
        self.farve = farve
        self.sporlaengde = sporlaengde
        if self.sporlaengde:
            self.spor = list()

    def updater(self, delta_tid):
        self.spor.append(self.punkt)
        if len(self.spor) >= self.sporlaengde:
            self.spor.pop(0)
        
        self.vinkel += self.vinkelhastighed * delta_tid
        self.punkt = self.centrum[0] + self.radius * math.cos(self.vinkel), self.centrum[1] + self.radius * math.sin(self.vinkel)

    def tegn(self):
        x, y = self.punkt
        arcade.draw_circle_filled(x, y, 5, self.farve)
        for punkt in self.spor:
            x, y = punkt
            arcade.draw_circle_filled(x, y, 2, self.farve)

class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    def setup(self):
        self.cirkel = Cirkel((400, 300), 100, 5, 0, arcade.csscolor.RED, 100)

    def update(self, delta_tid):
        self.cirkel.updater(delta_tid)

    def on_draw(self):
        self.clear()
        self.cirkel.tegn()

def main():
    vindue = Vindue(BREDDE, HOEJDE, "Cirkel som klasse")
    vindue.setup()

    arcade.run()

main()
# Cirklen:1 ends here
